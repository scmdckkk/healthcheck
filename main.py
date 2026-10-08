import requests

SITES = ["https://google.com", "https://gitbob.com"]

for site in SITES:
    try:
        r = requests.get(site, timeout=5)
        print(f"{site} -> {r.status_code}")
    except requests.RequestException as e:
        print(f"{site} -> ОШИБКА: {e}")