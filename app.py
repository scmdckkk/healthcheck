from flask import Flask, jsonify, render_template_string

from main import check_site, load_sites

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>Статус сайтов</title>
  <style>
    body { font-family: sans-serif; max-width: 640px; margin: 40px auto; }
    li { margin: 8px 0; }
    .ok { color: green; }
    .bad { color: crimson; }
  </style>
</head>
<body>
  <h1>Статус сайтов</h1>
  <ul>
  {% for row in rows %}
    <li class="{{ 'ok' if row.ok else 'bad' }}">
      {{ '✅' if row.ok else '❌' }} {{ row.url }} — {{ row.status }}
    </li>
  {% endfor %}
  </ul>
  <p><a href="/api/status">JSON</a></p>
</body>
</html>
"""


def collect():
    rows = []
    for site in load_sites():
        url, status = check_site(site)
        ok = isinstance(status, int) and 200 <= status < 400
        rows.append({"url": url, "status": status, "ok": ok})
    return rows


@app.route("/")
def index():
    return render_template_string(PAGE, rows=collect())


@app.route("/api/status")
def api_status():
    return jsonify(collect())
