# task_conftest/ui_tests/test_ui_functionality.py
def test_ui_login(browser, user_credentials, ui_timeout, project_config):
    """UI тест логина"""
    print(f"\n--- UI Test: test_ui_login ---")
    print(f"Browser: {browser}")
    print(f"Credentials: {user_credentials}")
    print(f"UI Timeout: {ui_timeout}")
    print(f"Project Config: {project_config}")

    assert browser.startswith("browser_")
    assert user_credentials["username"] == "test_user"
    assert project_config["environment"] == "test"


def test_ui_dashboard(browser, global_setup, generate_id):
    """UI тест дашборда"""
    print(f"\n--- UI Test: test_ui_dashboard ---")
    print(f"Browser: {browser}")
    print(f"Global Setup: {global_setup}")
    print(f"Generated ID: {generate_id}")

    assert global_setup["data"] == "global_data"