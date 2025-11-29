# task_conftest/api_tests/load_tests/test_load_performance.py
def test_load_users(api_client, auth_token, load_config, global_setup):
    """Нагрузочный тест пользователей с ПЕРЕОПРЕДЕЛЕННЫМИ фикстурами"""
    print(f"\n--- Load Test: test_load_users ---")
    print(f"API Client: {api_client}")
    print(f"Auth Token: {auth_token}")
    print(f"Load Config: {load_config}")

    # Проверяем что фикстуры ПЕРЕОПРЕДЕЛЕНЫ
    assert auth_token.startswith("LOAD_token_")
    assert "VIRTUAL_USER" in auth_token
    assert api_client["type"] == "load_testing"
    assert "LOAD_api_client" in api_client["client"]
    assert load_config["test_type"] == "load"


def test_load_products(auth_token, api_headers, generate_id):
    """Еще один нагрузочный тест"""
    print(f"\n--- Load Test: test_load_products ---")
    print(f"Auth Token: {auth_token}")
    print(f"Generated ID: {generate_id}")

    # auth_token должен быть переопределенным
    assert "LOAD_" in auth_token