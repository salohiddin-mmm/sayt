"""IshTopar backend: hisoblar, parol, SMS kod orqali tasdiqlash, profil.

Ishga tushirish:  python app.py   ->  http://127.0.0.1:5000
"""
import hashlib
import hmac
import json
import os
import re
import secrets
import sqlite3
import time
from datetime import timedelta

from urllib.parse import urlparse

from flask import Flask, g, jsonify, request, send_from_directory, session
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.security import check_password_hash, generate_password_hash

try:  # .env faylidagi sozlamalarni o'qiydi (pip install python-dotenv)
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from sms import SmsError, send_sms  # noqa: E402  (dotenv'dan keyin import qilinadi)
import tg  # noqa: E402

# ---------- Sozlamalar ----------
CODE_TTL = 120          # kod necha soniya amal qiladi
RESEND_WAIT = 60        # qayta yuborish uchun kutish (soniya)
MAX_ATTEMPTS = 5        # bitta kod uchun noto'g'ri urinishlar
PER_PHONE_HOUR = 3      # bir raqamga 1 soatda eng ko'pi bilan nechta SMS
PER_IP_HOUR = 10        # bir IP'dan 1 soatda eng ko'pi bilan nechta SMS
LOGIN_FAILS = 5         # shuncha xato paroldan keyin vaqtincha bloklanadi
LOGIN_WINDOW = 300      # ... oxirgi 5 daqiqa ichida
RESET_TTL = 600         # parolni tiklash ruxsati necha soniya amal qiladi
MIN_PW, MAX_PW = 8, 128 # MAX_PW: juda uzun parol bilan serverni qiynashdan himoya
DB_PATH = os.environ.get("DB_PATH", "ishtopar.db")
PURPOSES = ("register", "login", "reset")
CATEGORIES = {"sales", "transport", "edu", "office", "it", "service", "build"}
JTYPES = {"full", "part", "intern"}
EXTRAS = {"", "bonus", "food", "weekly", "deal"}
JOB_TTL = 30 * 86400    # e'lon tasdiqlangandan keyin 30 kun ko'rinadi
REPORT_HIDE = 3         # shuncha turli odam shikoyat qilsa, e'lon avtomatik yashiriladi
MAX_JOBS_DAY = 10       # bir foydalanuvchi sutkada eng ko'pi bilan nechta e'lon yuboradi
PROD = os.environ.get("PRODUCTION") == "1"

app = Flask(__name__, static_folder="static", static_url_path="/static")
secret = os.environ.get("SECRET_KEY")
if not secret:
    secret = secrets.token_hex(32)
    print("OGOHLANTIRISH: SECRET_KEY berilmagan, vaqtinchalik kalit ishlatilmoqda "
          "(server qayta ishga tushsa sessiyalar o'chadi). .env faylini to'ldiring.")
app.config.update(
    SECRET_KEY=secret,
    SESSION_COOKIE_HTTPONLY=True,    # JavaScript cookie'ni o'qiy olmaydi
    SESSION_COOKIE_SAMESITE="Lax",   # boshqa saytlardan yashirin so'rovdan himoya
    SESSION_COOKIE_SECURE=os.environ.get("PRODUCTION") == "1",  # faqat HTTPS
    PERMANENT_SESSION_LIFETIME=timedelta(days=30),
    MAX_CONTENT_LENGTH=300 * 1024,   # so'rov hajmi 300 KB dan oshmasin
)
if PROD:
    # nginx ortida ishlaganda: haqiqiy IP va HTTPS ni to'g'ri aniqlash.
    # TRUSTED_PROXIES = oldingizda nechta proxy turgani (odatda 1: faqat nginx).
    app.config["SESSION_COOKIE_NAME"] = "__Host-ishtopar"  # faqat HTTPS, faqat shu domen
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=int(os.environ.get("TRUSTED_PROXIES", "1")), x_proto=1, x_host=1)
DUMMY_HASH = generate_password_hash("dummy-password-for-timing")


# ---------- Ma'lumotlar bazasi ----------
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    with sqlite3.connect(DB_PATH) as db:
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS users(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              phone TEXT UNIQUE NOT NULL,
              name TEXT NOT NULL,
              role TEXT NOT NULL CHECK(role IN ('seeker','employer')),
              company TEXT NOT NULL DEFAULT '',
              pw_hash TEXT NOT NULL,
              email TEXT NOT NULL DEFAULT '',
              region TEXT NOT NULL DEFAULT '',
              district TEXT NOT NULL DEFAULT '',
              field TEXT NOT NULL DEFAULT '',
              tg TEXT NOT NULL DEFAULT '',
              about TEXT NOT NULL DEFAULT '',
              site TEXT NOT NULL DEFAULT '',
              co_about TEXT NOT NULL DEFAULT '',
              notify INTEGER NOT NULL DEFAULT 0,
              photo TEXT NOT NULL DEFAULT '',
              created_at INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS otp_codes(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              phone TEXT NOT NULL,
              purpose TEXT NOT NULL,
              code_hash TEXT NOT NULL,
              created_at INTEGER NOT NULL,
              expires_at INTEGER NOT NULL,
              attempts INTEGER NOT NULL DEFAULT 0,
              used INTEGER NOT NULL DEFAULT 0,
              sent INTEGER NOT NULL DEFAULT 1,
              ip TEXT);
            CREATE INDEX IF NOT EXISTS i_otp_phone ON otp_codes(phone, created_at);
            CREATE INDEX IF NOT EXISTS i_otp_ip ON otp_codes(ip, created_at);
            CREATE TABLE IF NOT EXISTS pending_regs(
              phone TEXT PRIMARY KEY,
              payload TEXT NOT NULL,
              created_at INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS login_fails(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              phone TEXT NOT NULL,
              ip TEXT,
              ts INTEGER NOT NULL);
            CREATE INDEX IF NOT EXISTS i_fail_phone ON login_fails(phone, ts);
            CREATE TABLE IF NOT EXISTS jobs(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              owner_id INTEGER NOT NULL,
              title TEXT NOT NULL, company TEXT NOT NULL,
              category TEXT NOT NULL, jtype TEXT NOT NULL,
              region TEXT NOT NULL DEFAULT '', district TEXT NOT NULL DEFAULT '',
              remote INTEGER NOT NULL DEFAULT 0,
              smin REAL, smax REAL, sextra TEXT NOT NULL DEFAULT '',
              description TEXT NOT NULL, requirements TEXT NOT NULL DEFAULT '',
              contact TEXT NOT NULL, search TEXT NOT NULL DEFAULT '',
              status TEXT NOT NULL DEFAULT 'pending',
              created_at INTEGER NOT NULL, approved_at INTEGER, expires_at INTEGER);
            CREATE INDEX IF NOT EXISTS i_jobs_status ON jobs(status, expires_at);
            CREATE INDEX IF NOT EXISTS i_jobs_owner ON jobs(owner_id, created_at);
            CREATE TABLE IF NOT EXISTS job_reports(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              job_id INTEGER NOT NULL, reporter TEXT NOT NULL, reason TEXT NOT NULL DEFAULT '',
              ip TEXT, created_at INTEGER NOT NULL,
              UNIQUE(job_id, reporter));
            CREATE TABLE IF NOT EXISTS tg_links(
              phone TEXT PRIMARY KEY, chat_id INTEGER NOT NULL, linked_at INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS tg_tokens(
              token TEXT PRIMARY KEY, phone TEXT NOT NULL, chat_id INTEGER,
              created_at INTEGER NOT NULL, done INTEGER NOT NULL DEFAULT 0, ip TEXT);
            """
        )
        cols = [r[1] for r in db.execute("PRAGMA table_info(users)")]
        if "consent_at" not in cols:  # eski bazani yangilash
            db.execute("ALTER TABLE users ADD COLUMN consent_at INTEGER NOT NULL DEFAULT 0")


init_db()


# ---------- Yordamchi funksiyalar ----------
def err(code, message, status, **extra):
    """Xato javobi. `code` ni sayt o'z tiliga tarjima qiladi, `message` esa zaxira matn."""
    return jsonify(ok=False, code=code, error=message, **extra), status


def normalize_phone(value):
    """'+998 90 123 45 67' yoki '901234567' -> '998901234567'. Noto'g'ri bo'lsa None."""
    d = re.sub(r"\D", "", str(value or ""))
    if len(d) == 9:
        d = "998" + d
    return d if re.fullmatch(r"998\d{9}", d) else None


def hash_code(phone, purpose, code):
    # Kodni bazada oddiy ko'rinishda saqlamaymiz, faqat HMAC hash'ini.
    msg = f"{phone}:{purpose}:{code}".encode()
    return hmac.new(app.config["SECRET_KEY"].encode(), msg, hashlib.sha256).hexdigest()


def clean(value, limit):
    return str(value or "").strip()[:limit]


def user_json(row):
    return {
        "id": row["phone"], "name": row["name"], "role": row["role"], "company": row["company"],
        "email": row["email"], "region": row["region"], "district": row["district"],
        "field": row["field"], "tg": row["tg"], "about": row["about"], "site": row["site"],
        "coAbout": row["co_about"], "notify": bool(row["notify"]), "photo": row["photo"],
        "isAdmin": row["phone"] in admin_phones(),
    }


def current_user():
    uid = session.get("uid")
    if not uid:
        return None
    return get_db().execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()


def login_session(user_row):
    session.clear()  # eski sessiyani tashlab yangisini beramiz (session fixation'dan himoya)
    session["uid"] = user_row["id"]
    session.permanent = True


@app.before_request
def require_json():
    # Oddiy HTML forma orqali yuborilgan (CSRF) so'rovlarni rad etamiz.
    if request.method in ("POST", "PUT") and request.path.startswith("/api/") and not request.is_json:
        return err("json_required", "Content-Type: application/json kerak", 415)


@app.before_request
def check_origin():
    # Boshqa saytdan yuborilgan o'zgartiruvchi so'rovlarni rad etamiz (CSRF'dan ikkinchi himoya qatlami).
    if request.method in ("POST", "PUT", "DELETE") and request.path.startswith("/api/"):
        origin = request.headers.get("Origin")
        if origin and urlparse(origin).netloc != request.host:
            return err("bad_origin", "Ruxsat yo'q", 403)


@app.after_request
def security_headers(resp):
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Referrer-Policy"] = "same-origin"
    resp.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    resp.headers["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self'; "
        "frame-ancestors 'none'; base-uri 'self'; form-action 'self'")
    if PROD:
        resp.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    if request.path.startswith("/api/"):
        resp.headers["Cache-Control"] = "no-store"
    return resp


# ---------- SMS kod ----------
def provider():
    return os.environ.get("SMS_PROVIDER", "console")


def admin_phones():
    raw = os.environ.get("ADMIN_PHONES", "")
    return {n for n in (normalize_phone(x) for x in raw.split(",")) if n}


def need_bot(phone):
    """Telegram rejimida raqam hali botga ulanmagan: sayt foydalanuvchiga bot havolasini beradi."""
    ip = request.remote_addr or "?"
    now = int(time.time())
    db = get_db()
    db.execute("DELETE FROM tg_tokens WHERE created_at < ?", (now - 86400,))
    hour = now - 3600
    n_ip = db.execute("SELECT COUNT(*) FROM tg_tokens WHERE ip=? AND created_at>?", (ip, hour)).fetchone()[0]
    n_phone = db.execute("SELECT COUNT(*) FROM tg_tokens WHERE phone=? AND created_at>?", (phone, hour)).fetchone()[0]
    if n_ip >= PER_IP_HOUR or n_phone >= 5:
        return err("rate_limited", "Juda ko'p so'rov. Keyinroq urinib ko'ring", 429)
    token = secrets.token_urlsafe(16)
    db.execute("INSERT INTO tg_tokens(token, phone, created_at, ip) VALUES(?,?,?,?)", (token, phone, now, ip))
    db.commit()
    bot = os.environ.get("BOT_USERNAME", "").lstrip("@")
    return jsonify(ok=True, need_bot=True, token=token, bot_url=f"https://t.me/{bot}?start={token}")


@app.get("/api/tg/status")
def tg_status():
    token = request.args.get("token", "")[:64]
    row = get_db().execute("SELECT done, created_at FROM tg_tokens WHERE token=?", (token,)).fetchone()
    return jsonify(ok=True, linked=bool(row and row["done"]))


def issue_code(phone, purpose, deliver=True):
    """Kod yaratadi, cheklovlarni tekshiradi va SMS yuboradi.

    deliver=False: raqam bazada yo'q (login/reset). Cheklovlar baribir xuddi shunday
    ishlaydi va javob bir xil, shunda begona odam "bu raqam ro'yxatdan o'tganmi"
    degan savolga javob topa olmaydi.
    """
    ip = request.remote_addr or "?"
    now = int(time.time())
    db = get_db()
    db.execute("DELETE FROM otp_codes WHERE created_at < ?", (now - 86400,))
    link = None
    if provider() == "telegram":
        link = db.execute("SELECT chat_id FROM tg_links WHERE phone=?", (phone,)).fetchone()
        if not link:
            return need_bot(phone)  # raqam begona bo'lsa ham javob xuddi shunday: raqam borligi sezilmaydi
    db.execute("DELETE FROM pending_regs WHERE created_at < ?", (now - 3600,))

    last = db.execute("SELECT created_at FROM otp_codes WHERE phone=? ORDER BY id DESC LIMIT 1",
                      (phone,)).fetchone()
    if last and now - last["created_at"] < RESEND_WAIT:
        wait = RESEND_WAIT - (now - last["created_at"])
        return err("too_soon", "Biroz kutib, qayta urinib ko'ring", 429, retry_after=wait)
    hour = now - 3600
    n_phone = db.execute("SELECT COUNT(*) FROM otp_codes WHERE phone=? AND created_at>?",
                         (phone, hour)).fetchone()[0]
    n_ip = db.execute("SELECT COUNT(*) FROM otp_codes WHERE ip=? AND created_at>?",
                      (ip, hour)).fetchone()[0]
    if n_phone >= PER_PHONE_HOUR or n_ip >= PER_IP_HOUR:
        return err("rate_limited", "Juda ko'p so'rov. Keyinroq urinib ko'ring", 429)

    code = f"{secrets.randbelow(900000) + 100000}"
    cur = db.execute(
        "INSERT INTO otp_codes(phone, purpose, code_hash, created_at, expires_at, sent, ip)"
        " VALUES(?,?,?,?,?,?,?)",
        (phone, purpose, hash_code(phone, purpose, code), now, now + CODE_TTL, 1 if deliver else 0, ip))
    db.commit()

    if deliver:
        text = f"IshTopar: tasdiqlash kodi {code}. Kodni hech kimga bermang."
        try:
            if link:
                tg.send_message(link["chat_id"], text)
            else:
                send_sms(phone, text)
        except SmsError:
            app.logger.exception("SMS yuborilmadi")
            db.execute("DELETE FROM otp_codes WHERE id=?", (cur.lastrowid,))
            db.commit()
            return err("sms_failed", "SMS yuborib bo'lmadi, keyinroq urinib ko'ring", 502)
    elif provider() == "console":
        print(f"[DEV] +{phone} ro'yxatdan o'tmagan: SMS yuborilmadi (sayt buni foydalanuvchiga bildirmaydi).",
              flush=True)

    # Kodning o'zi javobga QO'SHILMAYDI.
    return jsonify(ok=True, expires_in=CODE_TTL, resend_in=RESEND_WAIT)


@app.get("/api/config")
def config():
    # Sayt shu orqali "sinov rejimi"ni (kod terminalda chiqishini) biladi.
    channel = os.environ.get("CHANNEL_URL", "").strip()
    if not re.fullmatch(r"https://t\.me/[A-Za-z0-9_+/-]{3,64}", channel):
        channel = ""  # noto'g'ri yoki bo'sh bo'lsa, tugma ko'rsatilmaydi
    return jsonify(ok=True, provider=provider(), dev_sms=provider() == "console", channel=channel)


@app.post("/api/register/start")
def register_start():
    d = request.get_json(silent=True) or {}
    phone = normalize_phone(d.get("phone"))
    password = str(d.get("password") or "")
    role = d.get("role")
    company = clean(d.get("company"), 100)
    if not phone:
        return err("bad_phone", "Telefon raqam noto'g'ri", 400)
    if d.get("consent") is not True:
        return err("consent_required", "Maxfiylik siyosatiga rozilik kerak", 400)
    if not (MIN_PW <= len(password) <= MAX_PW):
        return err("weak_password", "Parol kamida 8 ta belgi bo'lsin", 400)
    if role not in ("seeker", "employer"):
        return err("bad_role", "Rol noto'g'ri", 400)
    if role == "employer" and not company:
        return err("company_required", "Kompaniya nomini kiriting", 400)
    db = get_db()
    if db.execute("SELECT 1 FROM users WHERE phone=?", (phone,)).fetchone():
        return err("exists", "Bu raqam allaqachon ro'yxatdan o'tgan", 409)
    payload = {"name": clean(d.get("name"), 80), "role": role,
               "company": company if role == "employer" else "",
               "pw_hash": generate_password_hash(password)}  # parol faqat hash holida saqlanadi
    db.execute("INSERT OR REPLACE INTO pending_regs(phone, payload, created_at) VALUES(?,?,?)",
               (phone, json.dumps(payload), int(time.time())))
    db.commit()
    return issue_code(phone, "register")


@app.post("/api/sms/send")
def sms_send():
    """Kodni qayta yuborish yoki SMS orqali kirish / parolni tiklash uchun kod so'rash."""
    d = request.get_json(silent=True) or {}
    phone = normalize_phone(d.get("phone"))
    purpose = d.get("purpose")
    if not phone or purpose not in PURPOSES:
        return err("bad_phone", "Telefon raqam noto'g'ri", 400)
    db = get_db()
    if purpose == "register":
        exists = db.execute("SELECT 1 FROM pending_regs WHERE phone=?", (phone,)).fetchone()
        if not exists:
            return err("bad_code", "Avval ro'yxatdan o'tishni boshlang", 400)
        return issue_code(phone, "register")
    exists = db.execute("SELECT 1 FROM users WHERE phone=?", (phone,)).fetchone()
    return issue_code(phone, purpose, deliver=bool(exists))


@app.post("/api/sms/verify")
def sms_verify():
    d = request.get_json(silent=True) or {}
    phone = normalize_phone(d.get("phone"))
    purpose = d.get("purpose")
    code = str(d.get("code") or "").strip()
    if not phone or purpose not in PURPOSES or not re.fullmatch(r"\d{6}", code):
        return err("bad_code", "Kod noto'g'ri yoki muddati tugagan", 400)

    now = int(time.time())
    db = get_db()
    row = db.execute(
        "SELECT * FROM otp_codes WHERE phone=? AND purpose=? AND used=0 AND expires_at>?"
        " ORDER BY id DESC LIMIT 1", (phone, purpose, now)).fetchone()
    if not row:
        return err("bad_code", "Kod noto'g'ri yoki muddati tugagan", 400)
    if row["attempts"] >= MAX_ATTEMPTS:
        return err("code_attempts", "Urinishlar tugadi. Yangi kod so'rang", 429)

    good = hmac.compare_digest(row["code_hash"], hash_code(phone, purpose, code))  # doimiy vaqtda
    if not good or not row["sent"]:
        db.execute("UPDATE otp_codes SET attempts=attempts+1 WHERE id=?", (row["id"],))
        db.commit()
        return err("bad_code", "Kod noto'g'ri yoki muddati tugagan", 400)

    db.execute("UPDATE otp_codes SET used=1 WHERE id=?", (row["id"],))  # kod faqat bir marta ishlaydi

    if purpose == "register":
        pend = db.execute("SELECT payload FROM pending_regs WHERE phone=?", (phone,)).fetchone()
        if not pend:
            db.commit()
            return err("bad_code", "Kod noto'g'ri yoki muddati tugagan", 400)
        p = json.loads(pend["payload"])
        try:
            db.execute(
                "INSERT INTO users(phone, name, role, company, pw_hash, created_at, consent_at) VALUES(?,?,?,?,?,?,?)",
                (phone, p["name"] or f"+{phone}", p["role"], p["company"], p["pw_hash"], now, now))
        except sqlite3.IntegrityError:
            db.commit()
            return err("exists", "Bu raqam allaqachon ro'yxatdan o'tgan", 409)
        db.execute("DELETE FROM pending_regs WHERE phone=?", (phone,))
        db.commit()
        user = db.execute("SELECT * FROM users WHERE phone=?", (phone,)).fetchone()
        login_session(user)
        return jsonify(ok=True, user=user_json(user))

    user = db.execute("SELECT * FROM users WHERE phone=?", (phone,)).fetchone()
    db.commit()
    if not user:
        return err("bad_code", "Kod noto'g'ri yoki muddati tugagan", 400)
    if purpose == "login":
        login_session(user)
        return jsonify(ok=True, user=user_json(user))
    session.clear()  # purpose == "reset": faqat yangi parol o'rnatishga ruxsat beramiz
    session["reset_uid"] = user["id"]
    session["reset_at"] = now
    return jsonify(ok=True, next="new_password")


@app.post("/api/password/reset")
def password_reset():
    d = request.get_json(silent=True) or {}
    password = str(d.get("password") or "")
    uid, at = session.get("reset_uid"), session.get("reset_at", 0)
    if not uid or time.time() - at > RESET_TTL:
        return err("reset_expired", "Ruxsat muddati tugadi. Qaytadan boshlang", 403)
    if not (MIN_PW <= len(password) <= MAX_PW):
        return err("weak_password", "Parol kamida 8 ta belgi bo'lsin", 400)
    db = get_db()
    db.execute("UPDATE users SET pw_hash=? WHERE id=?", (generate_password_hash(password), uid))
    db.commit()
    user = db.execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()
    login_session(user)
    return jsonify(ok=True, user=user_json(user))


# ---------- Parol bilan kirish ----------
@app.post("/api/login")
def login():
    d = request.get_json(silent=True) or {}
    phone = normalize_phone(d.get("phone"))
    password = str(d.get("password") or "")[:MAX_PW]
    if not phone:
        return err("bad_phone", "Telefon raqam noto'g'ri", 400)
    ip = request.remote_addr or "?"
    now = int(time.time())
    db = get_db()
    since = now - LOGIN_WINDOW
    fails = db.execute("SELECT COUNT(*), MIN(ts) FROM login_fails WHERE phone=? AND ts>?",
                       (phone, since)).fetchone()
    ip_fails = db.execute("SELECT COUNT(*) FROM login_fails WHERE ip=? AND ts>?", (ip, since)).fetchone()[0]
    if fails[0] >= LOGIN_FAILS or ip_fails >= LOGIN_FAILS * 4:
        wait = max(1, LOGIN_WINDOW - (now - (fails[1] or now)))
        return err("locked", "Juda ko'p urinish. Keyinroq urinib ko'ring", 429, retry_after=wait)

    user = db.execute("SELECT * FROM users WHERE phone=?", (phone,)).fetchone()
    # Raqam topilmasa ham hash tekshiramiz, shunda javob vaqti bilan raqam borligini bilib bo'lmaydi.
    ok = check_password_hash(user["pw_hash"] if user else DUMMY_HASH, password)
    if not (user and ok):
        db.execute("INSERT INTO login_fails(phone, ip, ts) VALUES(?,?,?)", (phone, ip, now))
        db.commit()
        return err("bad_credentials", "Telefon raqam yoki parol noto'g'ri", 401)
    db.execute("DELETE FROM login_fails WHERE phone=?", (phone,))
    db.commit()
    login_session(user)
    return jsonify(ok=True, user=user_json(user))


# ---------- Sessiya va profil ----------
@app.get("/api/me")
def me():
    user = current_user()
    if not user:
        return err("unauth", "Kirmagansiz", 401)
    return jsonify(ok=True, user=user_json(user))


@app.post("/api/logout")
def logout():
    session.clear()
    return jsonify(ok=True)


@app.put("/api/profile")
def profile_update():
    user = current_user()
    if not user:
        return err("unauth", "Kirmagansiz", 401)
    d = request.get_json(silent=True) or {}
    email = clean(d.get("email"), 120)
    if email and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return err("bad_email", "Email noto'g'ri", 400)
    photo = str(d.get("photo") or "")
    if photo and (len(photo) > 150_000 or not re.match(r"^data:image/(jpeg|png|webp);base64,[A-Za-z0-9+/=]+$", photo)):
        return err("bad_photo", "Rasm noto'g'ri yoki juda katta", 400)
    company = clean(d.get("company"), 100) if user["role"] == "employer" else ""
    if user["role"] == "employer" and not company:
        company = user["company"]
    db = get_db()
    db.execute(
        "UPDATE users SET name=?, email=?, region=?, district=?, field=?, tg=?, about=?, site=?,"
        " co_about=?, notify=?, photo=?, company=? WHERE id=?",
        (clean(d.get("name"), 80) or user["name"], email, clean(d.get("region"), 60),
         clean(d.get("district"), 60), clean(d.get("field"), 30), clean(d.get("tg"), 60),
         clean(d.get("about"), 300), clean(d.get("site"), 120), clean(d.get("coAbout"), 400),
         1 if d.get("notify") else 0, photo, company, user["id"]))
    db.commit()
    return jsonify(ok=True, user=user_json(db.execute("SELECT * FROM users WHERE id=?", (user["id"],)).fetchone()))


# ---------- E'lonlar ----------
def num(v):
    """Maosh (mln so'm): bo'sh bo'lsa None, noto'g'ri bo'lsa ValueError."""
    if v in (None, ""):
        return None
    f = float(v)
    if not (0 <= f <= 1000):
        raise ValueError
    return round(f, 2)


def job_json(r, owner_view=False):
    now = int(time.time())
    base = r["approved_at"] or r["created_at"]
    out = {"id": r["id"], "t": r["title"], "c": r["company"], "cat": r["category"], "type": r["jtype"],
           "reg": r["region"], "dist": r["district"], "remote": bool(r["remote"]),
           "s": [r["smin"], r["smax"]] if r["smin"] is not None else None, "x": r["sextra"],
           "hours": max(0, (now - base) // 3600), "d": r["description"], "r": r["requirements"],
           "contact": r["contact"], "a": r["about"] or ""}
    if owner_view:
        out["status"] = r["status"]
    return out


JOB_SELECT = "SELECT j.*, u.co_about AS about FROM jobs j JOIN users u ON u.id=j.owner_id"


def job_stats(db, now):
    total = db.execute("SELECT COUNT(*) FROM jobs WHERE status='approved' AND expires_at>?", (now,)).fetchone()[0]
    today = db.execute("SELECT COUNT(*) FROM jobs WHERE status='approved' AND expires_at>? AND approved_at>?",
                       (now, now - 86400)).fetchone()[0]
    return {"total": total, "today": today}


@app.get("/api/jobs")
def jobs_list():
    a = request.args
    now = int(time.time())
    db = get_db()
    where, args = ["j.status='approved'", "j.expires_at>?"], [now]
    if a.get("ids"):
        ids = [int(x) for x in a["ids"].split(",")[:100] if x.strip().isdigit()]
        if not ids:
            return jsonify(ok=True, jobs=[], total=0, stats=job_stats(db, now))
        where.append("j.id IN (%s)" % ",".join("?" * len(ids)))
        args += ids
    q = clean(a.get("q"), 80).lower()
    if q:
        esc = q.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
        where.append("j.search LIKE ? ESCAPE '\\'")
        args.append(f"%{esc}%")
    if a.get("cat") in CATEGORIES:
        where.append("j.category=?"); args.append(a["cat"])
    types = [x for x in a.get("type", "").split(",") if x in JTYPES]
    if types:
        where.append("j.jtype IN (%s)" % ",".join("?" * len(types))); args += types
    for key, col in (("region", "j.region"), ("district", "j.district"), ("company", "j.company")):
        v = clean(a.get(key), 100)
        if v:
            where.append(f"{col}=?"); args.append(v)
    if a.get("remote") == "1":
        where.append("j.remote=1")
    try:
        smin, smax = num(a.get("smin")), num(a.get("smax"))
    except ValueError:
        smin = smax = None
    if smin is not None or smax is not None:
        where.append("j.smin IS NOT NULL AND j.smax>=? AND j.smin<=?")
        args += [smin if smin is not None else 0, smax if smax is not None else 1e9]
    if a.get("sal") == "1":
        where.append("j.smin IS NOT NULL")
    order = "COALESCE(j.smax,0) DESC, j.approved_at DESC" if a.get("sort") == "salary" else "j.approved_at DESC"
    try:
        limit = max(1, min(int(a.get("limit", 20)), 50)); offset = max(0, int(a.get("offset", 0)))
    except ValueError:
        limit, offset = 20, 0
    cond = " AND ".join(where)
    total = db.execute(f"SELECT COUNT(*) FROM jobs j WHERE {cond}", args).fetchone()[0]
    rows = db.execute(f"{JOB_SELECT} WHERE {cond} ORDER BY {order} LIMIT ? OFFSET ?", args + [limit, offset]).fetchall()
    return jsonify(ok=True, jobs=[job_json(r) for r in rows], total=total, stats=job_stats(db, now))


@app.post("/api/jobs")
def job_create():
    user = current_user()
    if not user:
        return err("unauth", "Kirmagansiz", 401)
    admin = user["phone"] in admin_phones()
    if user["role"] != "employer" and not admin:
        return err("employer_only", "E'lonni faqat ish beruvchi joylay oladi", 403)
    now = int(time.time())
    db = get_db()
    if db.execute("SELECT COUNT(*) FROM jobs WHERE owner_id=? AND created_at>?", (user["id"], now - 86400)).fetchone()[0] >= MAX_JOBS_DAY:
        return err("rate_limited", "Sutkalik e'lon limiti tugadi", 429)
    d = request.get_json(silent=True) or {}
    title, desc = clean(d.get("title"), 100), clean(d.get("description"), 2000)
    company = clean(d.get("company"), 100) or user["company"]
    contact = clean(d.get("contact"), 100)
    cat, jtype, extra = d.get("category"), d.get("type"), d.get("extra") or ""
    try:
        smin, smax = num(d.get("smin")), num(d.get("smax"))
    except (ValueError, TypeError):
        return err("bad_salary", "Maosh noto'g'ri", 400)
    if smin is None and smax is not None:
        smin = smax
    if smax is None and smin is not None:
        smax = smin
    if smin is not None and smin > smax:
        return err("bad_salary", "Maosh noto'g'ri", 400)
    if len(title) < 3 or len(company) < 2 or len(desc) < 10 or len(contact) < 3:
        return err("bad_job", "Majburiy maydonlarni to'ldiring", 400)
    if cat not in CATEGORIES or jtype not in JTYPES or extra not in EXTRAS:
        return err("bad_job", "Soha yoki ish turi noto'g'ri", 400)
    region, district = clean(d.get("region"), 60), clean(d.get("district"), 60)
    if not region:
        return err("bad_job", "Hududni tanlang", 400)
    req = clean(d.get("requirements"), 1000)
    status = "approved" if admin else "pending"
    cur = db.execute(
        "INSERT INTO jobs(owner_id,title,company,category,jtype,region,district,remote,smin,smax,sextra,description,"
        "requirements,contact,search,status,created_at,approved_at,expires_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (user["id"], title, company, cat, jtype, region, district, 1 if d.get("remote") else 0, smin, smax, extra, desc,
         req, contact, f"{title} {company} {desc}".lower(), status, now,
         now if admin else None, now + JOB_TTL if admin else None))
    db.commit()
    row = db.execute(f"{JOB_SELECT} WHERE j.id=?", (cur.lastrowid,)).fetchone()
    return jsonify(ok=True, job=job_json(row, True))


@app.get("/api/my/jobs")
def my_jobs():
    user = current_user()
    if not user:
        return err("unauth", "Kirmagansiz", 401)
    rows = get_db().execute(f"{JOB_SELECT} WHERE j.owner_id=? ORDER BY j.created_at DESC LIMIT 100", (user["id"],)).fetchall()
    return jsonify(ok=True, jobs=[job_json(r, True) for r in rows])


@app.delete("/api/jobs/<int:jid>")
def job_delete(jid):
    user = current_user()
    if not user:
        return err("unauth", "Kirmagansiz", 401)
    db = get_db()
    row = db.execute("SELECT owner_id FROM jobs WHERE id=?", (jid,)).fetchone()
    if not row:
        return err("not_found", "Topilmadi", 404)
    if row["owner_id"] != user["id"] and user["phone"] not in admin_phones():
        return err("forbidden", "Ruxsat yo'q", 403)
    db.execute("DELETE FROM job_reports WHERE job_id=?", (jid,))
    db.execute("DELETE FROM jobs WHERE id=?", (jid,))
    db.commit()
    return jsonify(ok=True)


@app.post("/api/jobs/<int:jid>/report")
def job_report(jid):
    now = int(time.time())
    ip = request.remote_addr or "?"
    db = get_db()
    job = db.execute("SELECT status FROM jobs WHERE id=? AND status IN ('approved','hidden')", (jid,)).fetchone()
    if not job:
        return err("not_found", "Topilmadi", 404)
    if db.execute("SELECT COUNT(*) FROM job_reports WHERE ip=? AND created_at>?", (ip, now - 3600)).fetchone()[0] >= 20:
        return err("rate_limited", "Juda ko'p so'rov", 429)
    user = current_user()
    reporter = f"u{user['id']}" if user else f"ip:{ip}"
    reason = clean((request.get_json(silent=True) or {}).get("reason"), 200)
    db.execute("INSERT OR IGNORE INTO job_reports(job_id, reporter, reason, ip, created_at) VALUES(?,?,?,?,?)",
               (jid, reporter, reason, ip, now))
    if db.execute("SELECT COUNT(*) FROM job_reports WHERE job_id=?", (jid,)).fetchone()[0] >= REPORT_HIDE:
        db.execute("UPDATE jobs SET status='hidden' WHERE id=? AND status='approved'", (jid,))
    db.commit()
    return jsonify(ok=True)


# ---------- Admin (moderatsiya) ----------
def admin_user():
    user = current_user()
    if not user:
        return None, err("unauth", "Kirmagansiz", 401)
    if user["phone"] not in admin_phones():
        return None, err("forbidden", "Ruxsat yo'q", 403)
    return user, None


@app.get("/api/admin/jobs")
def admin_jobs():
    _, e = admin_user()
    if e:
        return e
    status = "hidden" if request.args.get("status") == "hidden" else "pending"
    db = get_db()
    rows = db.execute(f"{JOB_SELECT} WHERE j.status=? ORDER BY j.created_at DESC LIMIT 100", (status,)).fetchall()
    out = []
    for r in rows:
        j = job_json(r, True)
        rep = db.execute("SELECT reason FROM job_reports WHERE job_id=? ORDER BY id DESC LIMIT 5", (r["id"],)).fetchall()
        j["reports"] = [x["reason"] for x in rep]
        out.append(j)
    counts = {s: db.execute("SELECT COUNT(*) FROM jobs WHERE status=?", (s,)).fetchone()[0] for s in ("pending", "hidden")}
    return jsonify(ok=True, jobs=out, counts=counts)


@app.post("/api/admin/jobs/<int:jid>/<action>")
def admin_job_action(jid, action):
    admin, e = admin_user()
    if e:
        return e
    if action not in ("approve", "reject", "delete"):
        return err("bad_action", "Noto'g'ri amal", 400)
    db = get_db()
    if not db.execute("SELECT 1 FROM jobs WHERE id=?", (jid,)).fetchone():
        return err("not_found", "Topilmadi", 404)
    now = int(time.time())
    if action == "approve":
        db.execute("UPDATE jobs SET status='approved', approved_at=?, expires_at=? WHERE id=?", (now, now + JOB_TTL, jid))
        db.execute("DELETE FROM job_reports WHERE job_id=?", (jid,))
    elif action == "reject":
        db.execute("UPDATE jobs SET status='rejected' WHERE id=?", (jid,))
    else:
        db.execute("DELETE FROM job_reports WHERE job_id=?", (jid,))
        db.execute("DELETE FROM jobs WHERE id=?", (jid,))
    db.commit()
    app.logger.info("ADMIN %s: %s job=%s", admin["phone"], action, jid)
    return jsonify(ok=True)


# ---------- Hisobni o'chirish ----------
@app.delete("/api/account")
def account_delete():
    user = current_user()
    if not user:
        return err("unauth", "Kirmagansiz", 401)
    ip = request.remote_addr or "?"
    now = int(time.time())
    db = get_db()
    fails = db.execute("SELECT COUNT(*) FROM login_fails WHERE phone=? AND ts>?", (user["phone"], now - LOGIN_WINDOW)).fetchone()[0]
    if fails >= LOGIN_FAILS:
        return err("locked", "Juda ko'p urinish. Keyinroq urinib ko'ring", 429, retry_after=60)
    password = str((request.get_json(silent=True) or {}).get("password") or "")[:MAX_PW]
    if not check_password_hash(user["pw_hash"], password):
        db.execute("INSERT INTO login_fails(phone, ip, ts) VALUES(?,?,?)", (user["phone"], ip, now))
        db.commit()
        return err("bad_credentials", "Parol noto'g'ri", 401)
    db.execute("DELETE FROM job_reports WHERE job_id IN (SELECT id FROM jobs WHERE owner_id=?)", (user["id"],))
    db.execute("DELETE FROM jobs WHERE owner_id=?", (user["id"],))
    db.execute("DELETE FROM tg_links WHERE phone=?", (user["phone"],))
    db.execute("DELETE FROM users WHERE id=?", (user["id"],))
    db.commit()
    session.clear()
    return jsonify(ok=True)


# ---------- Huquqiy sahifalar ----------
@app.get("/privacy")
def privacy():
    return send_from_directory(app.static_folder, "privacy.html")


@app.get("/terms")
def terms():
    return send_from_directory(app.static_folder, "terms.html")


@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=os.environ.get("PRODUCTION") != "1")
