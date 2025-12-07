# task_conftest/ui_tests/conftest.py
import random

import pytest


@pytest.fixture
def browser():
    """Фикстура браузера - доступна только UI тестам"""
    print("=== UI conftest: browser запускается ===")
    browser_id = f"browser_{random.randint(1, 100)}"
    yield browser_id
    print("=== UI conftest: browser закрывается ===")


@pytest.fixture
def user_credentials():
    """Данные пользователя для UI тестов"""
    return {
        "username": "test_user",
        "password": "test_pass_123",
        "role": "user"
    }


@pytest.fixture
def ui_timeout():
    """Таймауты для UI операций"""
    return {
        "element_visible": 10,
        "page_load": 30,
        "script_timeout": 15
    }
