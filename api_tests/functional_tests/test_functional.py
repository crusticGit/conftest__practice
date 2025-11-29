# task_conftest/api_tests/functional_tests/test_users.py
def test_get_users(api_client, auth_token, api_headers, functional_config, global_setup):
    """Функциональный тест получения пользователей"""
    print(f"\n--- Functional Test: test_get_users ---")
    print(f"API Client: {api_client}")
    print(f"Auth Token: {auth_token}")
    print(f"Functional Config: {functional_config}")
    print(f"Global Setup: {global_setup}")

    # Проверяем что используем СТАНДАРТНЫЕ фикстуры
    assert "token_" in auth_token
    assert api_client["type"] == "rest_api"
    assert functional_config["test_type"] == "functional"


def test_create_user(api_client, test_data, generate_id):
    """Функциональный тест создания пользователя"""
    print(f"\n--- Functional Test: test_create_user ---")
    print(f"Test Data: {test_data}")
    print(f"Generated ID: {generate_id}")
    assert test_data["users"]
