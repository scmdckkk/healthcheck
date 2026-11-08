# healthcheck

Сервис мониторинга сайтов: проверяет доступность адресов из `sites.txt`,
хранит результаты в PostgreSQL и показывает статус на веб-странице.

## Архитектура

- `checker` проверяет сайты раз в минуту и записывает результат в базу
- `db` база данных PostgreSQL
- `web` страница со статусом (Flask) и JSON по адресу `/api/status`

## Запуск

    docker compose up --build

Страница откроется на http://localhost:5000 (первые данные появятся через несколько секунд).
Остановить: `docker compose down`.

## Добавить сайт

Допиши адрес в `sites.txt` (по одному на строку) и перезапусти:

    docker compose up --build

## Тесты

    pip install -r requirements-dev.txt
    pytest

## CI

При каждом push и pull request GitHub Actions запускает тесты, затем поднимает
все сервисы через Docker Compose и проверяет, что API отдаёт данные из базы.
