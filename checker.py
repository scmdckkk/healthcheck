import os
import time

from db import init_db, last_ok, save_check
from main import check_site, load_sites
from notify import send_telegram

INTERVAL = int(os.environ.get("CHECK_INTERVAL", "60"))


def run_once():
    for site in load_sites():
        url, status = check_site(site)
        ok = isinstance(status, int) and 200 <= status < 400
        previous = last_ok(url)
        save_check(url, status, ok)
        print(f"{url} -> {status}", flush=True)
        # Сообщаем только о смене состояния, а не каждую минуту.
        if previous is not None and previous != ok:
            if ok:
                send_telegram(f"✅ {url} снова доступен ({status})")
            else:
                send_telegram(f"❌ {url} недоступен: {status}")


def main():
    init_db()
    while True:
        run_once()
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
