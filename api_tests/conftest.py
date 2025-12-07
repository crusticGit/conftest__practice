# task_conftest/api_tests/conftest.py
import random

import pytest


@pytest.fixture
def api_client():
    """Фикстура для API клиента - доступна всем API тестам"""
    print("=== API conftest: api_client создается ===")
    client_id = f"api_client_{random.randint(1, 100)}"
    return {"client": client_id, "type": "rest_api"}


@pytest.fixture
def auth_token():
    """Фикстура аутентификации - будет ПЕРЕОПРЕДЕЛЕНА в нагрузочных тестах"""
    print("=== API conftest: auth_token (СТАНДАРТНЫЙ) создается ===")
    return f"token_{random.randint(1000, 9999)}"


@pytest.fixture
def api_headers():
    """Базовые заголовки для API запросов"""
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
