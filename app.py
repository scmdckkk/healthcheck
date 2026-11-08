from flask import Flask, jsonify, render_template_string

from db import latest_checks

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
    small { color: gray; }
  </style>
</head>
<body>
  <h1>Статус сайтов</h1>
  {% if not rows %}<p>Данных пока нет, подожди минуту и обнови страницу.</p>{% endif %}
  <ul>
  {% for row in rows %}
    <li class="{{ 'ok' if row.ok else 'bad' }}">
      {{ '✅' if row.ok else '❌' }} {{ row.url }} — {{ row.status }}
      <small>({{ row.checked_at }})</small>
    </li>
  {% endfor %}
  </ul>
  <p><a href="/api/status">JSON</a></p>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(PAGE, rows=latest_checks())


@app.route("/api/status")
def api_status():
    return jsonify(latest_checks())
