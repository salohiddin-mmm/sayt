"""Telegram Bot API bilan ishlash (kutubxonasiz, faqat requests).

BOT_TOKEN va BOT_USERNAME .env faylida turadi. Token haqida hech qayerga yozmang.
TELEGRAM_API_BASE faqat sinov uchun (soxta server) o'zgartiriladi.
"""
import os

from sms import SmsError


class TgError(SmsError):
    pass


def _call(method, payload, timeout=15):
    import requests

    token = os.environ.get("BOT_TOKEN", "")
    if not token:
        raise TgError("BOT_TOKEN berilmagan")
    base = os.environ.get("TELEGRAM_API_BASE", "https://api.telegram.org")
    try:
        r = requests.post(f"{base}/bot{token}/{method}", json=payload, timeout=timeout)
        data = r.json()
    except (requests.RequestException, ValueError) as e:
        raise TgError("Telegramga ulanib bo'lmadi") from None  # tokenli URL xabarga tushmasin
    if not data.get("ok"):
        raise TgError(f"Telegram xatosi: {data.get('description', '?')}")
    return data.get("result")


def send_message(chat_id, text, reply_markup=None):
    payload = {"chat_id": chat_id, "text": text}
    if reply_markup:
        payload["reply_markup"] = reply_markup
    return _call("sendMessage", payload)


def get_updates(offset, timeout=30):
    return _call("getUpdates", {"offset": offset, "timeout": timeout,
                                "allowed_updates": ["message"]}, timeout=timeout + 10)
