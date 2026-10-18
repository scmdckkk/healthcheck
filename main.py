from pathlib import Path

import requests

SITES_FILE = Path(__file__).parent / "sites.txt"


def load_sites(path=SITES_FILE):
    """Читает адреса из файла, пропуская пустые строки и комментарии."""
    sites = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            sites.append(line)
    return sites


def check_site(url, timeout=5):
    """Проверяет сайт и возвращает (адрес, статус или текст ошибки)."""
    try:
        r = requests.get(url, timeout=timeout)
        return url, r.status_code
    except requests.RequestException as e:
        return url, f"ОШИБКА: {e}"


def main():
    for site in load_sites():
        url, result = check_site(site)
        print(f"{url} -> {result}")


if __name__ == "__main__":
    main()
