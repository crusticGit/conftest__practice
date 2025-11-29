# task_conftest/api_tests/functional_tests/conftest.py
import pytest


@pytest.fixture
def functional_config():
    """Конфигурация для функциональных тестов"""
    print("=== FUNCTIONAL conftest: functional_config ===")
    return {
        "test_type": "functional",
        "validate_schema": True,
        "check_performance": False
    }


@pytest.fixture
def test_data():
    """Тестовые данные для функционального тестирования"""
    return {
        "users": ["test_user_1", "test_user_2"],
        "products": ["product_a", "product_b"]
    }
