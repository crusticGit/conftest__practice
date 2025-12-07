# task_conftest/conftest.py
import random

import pytest


@pytest.fixture
def global_setup():
    """Фикстура доступная ВСЕМ тестам в проекте"""
    print("=== ROOT conftest: global_setup выполняется ===")
    return {"data": "global_data", "version": "1.0"}


@pytest.fixture
def project_config():
    """Общая конфигурация проекта"""
    print("=== ROOT conftest: project_config выполняется ===")
    return {
        "base_url": "https://example.com",
        "environment": "test",
        "timeout": 30
    }


@pytest.fixture
def generate_id():
    """Генератор ID для всех тестов"""
    return f"id_{random.randint(1000, 9999)}"
