# healthcheck

Скрипт проверяет доступность сайтов и выводит HTTP-статус каждого.

## Запуск локально

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python main.py

## Запуск в Docker

    docker build -t healthcheck .
    docker run --rm healthcheck

## Тесты

    pip install -r requirements-dev.txt
    pytest

## CI

При каждом push GitHub Actions запускает тесты, затем собирает Docker-образ и запускает контейнер.
