import requests

SITES = ["https://google.com", "https://github.com"]


def check_site(url, timeout=5):
    """Проверяет сайт и возвращает (адрес, статус или текст ошибки)."""
    try:
        r = requests.get(url, timeout=timeout)
        return url, r.status_code
    except requests.RequestException as e:
        return url, f"ОШИБКА: {e}"


def main():
    for site in SITES:
        url, result = check_site(site)
        print(f"{url} -> {result}")


if __name__ == "__main__":
    main()
