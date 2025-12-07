# task_conftest/api_tests/load_tests/conftest.py
import pytest


@pytest.fixture
def api_client(api_client):
    """ПЕРЕОПРЕДЕЛЕНИЕ: API клиент для нагрузочного тестирования"""
    print("=== LOAD conftest: api_client (НАГРУЗОЧНЫЙ) создается ===")
    # Модифицируем стандартный API клиент
    api_client["type"] = "load_testing"
    api_client["virtual_users"] = 100
    api_client["client"] = f"LOAD_{api_client['client']}"
    return api_client


@pytest.fixture
def auth_token(auth_token):
    """ПЕРЕОПРЕДЕЛЕНИЕ: auth_token для нагрузочного тестирования"""
    print("=== LOAD conftest: auth_token (НАГРУЗОЧНЫЙ) создается ===")
    # Используем исходный auth_token и модифицируем его
    return f"LOAD_{auth_token}_VIRTUAL_USER"


@pytest.fixture
def load_config():
    """Конфигурация специфичная для нагрузочного тестирования"""
    return {
        "test_type": "load",
        "duration": "5m",
        "users_count": 1000,
        "ramp_up": "1m"
    }
