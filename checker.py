import os
import time

from db import init_db, save_check
from main import check_site, load_sites

INTERVAL = int(os.environ.get("CHECK_INTERVAL", "60"))


def run_once():
    for site in load_sites():
        url, status = check_site(site)
        ok = isinstance(status, int) and 200 <= status < 400
        save_check(url, status, ok)
        print(f"{url} -> {status}", flush=True)


def main():
    init_db()
    while True:
        run_once()
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
