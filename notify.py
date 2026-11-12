import os

import requests


def send_telegram(text):
    """Отправляет сообщение в Telegram. Без токена или chat id молча пропускает."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return False
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={"chat_id": chat_id, "text": text},
            timeout=10,
        )
        return r.ok
    except requests.RequestException as e:
        # Текст исключения не печатаем: в нём может быть адрес с токеном.
        print(f"Не удалось отправить в Telegram: {type(e).__name__}", flush=True)
        return False
