"""SMS yuborish moduli.

Ikki rejim bor (SMS_PROVIDER muhit o'zgaruvchisi bilan tanlanadi):
  console - SMS yuborilmaydi, kod server terminalida chiqadi (sinash uchun, bepul)
  eskiz   - haqiqiy SMS (Eskiz.uz uslubidagi HTTP API)

MUHIM: provayder kalitlari faqat serverda, muhit o'zgaruvchilarida turadi.
Ularni hech qachon saytning (brauzer) kodiga yozmang.
"""
import os
import time


class SmsError(Exception):
    pass


def send_sms(phone: str, text: str) -> None:
    provider = os.environ.get("SMS_PROVIDER", "console")
    if provider == "console":
        print(f"\n[DEV SMS] +{phone}: {text}\n", flush=True)
        return
    if provider == "eskiz":
        _send_eskiz(phone, text)
        return
    raise SmsError(f"Noma'lum SMS provayder: {provider}")


# ---- Eskiz.uz uslubidagi provayder ----
# DIQQAT: manzillar va maydon nomlarini provayderning rasmiy hujjati
# bilan solishtiring, ular o'zgargan bo'lishi mumkin.
_BASE = os.environ.get("ESKIZ_BASE_URL", "https://notify.eskiz.uz/api")
_token = {"value": None, "exp": 0.0}


def _eskiz_token() -> str:
    import requests

    if _token["value"] and time.time() < _token["exp"]:
        return _token["value"]
    try:
        r = requests.post(
            f"{_BASE}/auth/login",
            data={
                "email": os.environ["ESKIZ_EMAIL"],
                "password": os.environ["ESKIZ_PASSWORD"],
            },
            timeout=10,
        )
        r.raise_for_status()
        _token["value"] = r.json()["data"]["token"]
        _token["exp"] = time.time() + 25 * 24 * 3600  # token ~30 kun yashaydi
    except (KeyError, ValueError, requests.RequestException) as e:
        raise SmsError("Provayderga kirib bo'lmadi") from e
    return _token["value"]


def _send_eskiz(phone: str, text: str) -> None:
    import requests

    try:
        r = requests.post(
            f"{_BASE}/message/sms/send",
            headers={"Authorization": f"Bearer {_eskiz_token()}"},
            data={
                "mobile_phone": phone,  # 998901234567 ko'rinishida
                "message": text,  # tasdiqlangan shablon bilan bir xil bo'lishi kerak
                "from": os.environ.get("ESKIZ_FROM", "4546"),  # sender name
            },
            timeout=10,
        )
        r.raise_for_status()
    except requests.RequestException as e:
        raise SmsError("SMS yuborilmadi") from e
