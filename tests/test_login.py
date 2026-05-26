import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# Valid credentials for saucedemo.com
VALID_USER     = "standard_user"
VALID_PASSWORD = "secret_sauce"


class TestLogin:
    """
    6 test cases covering login functionality on saucedemo.com.
    Each test gets a fresh browser from conftest.py driver fixture.
    """

    def test_valid_login_redirects_to_products(self, driver):
        """TC01: Valid username and password should land on products page."""
        login = LoginPage(driver)
        login.open()
        login.login(VALID_USER, VALID_PASSWORD)

        products = ProductsPage(driver)
        assert products.is_on_products_page(), \
            "Expected to land on products page after valid login"

    def test_invalid_password_shows_error(self, driver):
        """TC02: Correct username but wrong password should show error."""
        login = LoginPage(driver)
        login.open()
        login.login(VALID_USER, "wrong_password")

        assert login.is_error_displayed(), "Error message should appear for wrong password"
        assert "Username and password do not match" in login.get_error_message()

    def test_invalid_username_shows_error(self, driver):
        """TC03: Non-existent username should show error."""
        login = LoginPage(driver)
        login.open()
        login.login("unknown_user", VALID_PASSWORD)

        assert login.is_error_displayed(), "Error message should appear for invalid username"

    def test_empty_username_shows_error(self, driver):
        """TC04: Submitting with empty username should show validation error."""
        login = LoginPage(driver)
        login.open()
        login.login("", VALID_PASSWORD)

        assert login.is_error_displayed(), "Error should appear when username is empty"
        assert "Username is required" in login.get_error_message()

    def test_empty_password_shows_error(self, driver):
        """TC05: Submitting with empty password should show validation error."""
        login = LoginPage(driver)
        login.open()
        login.login(VALID_USER, "")

        assert login.is_error_displayed(), "Error should appear when password is empty"
        assert "Password is required" in login.get_error_message()

    def test_locked_user_cannot_login(self, driver):
        """TC06: Locked out user should see specific error message."""
        login = LoginPage(driver)
        login.open()
        login.login("locked_out_user", VALID_PASSWORD)

        assert login.is_error_displayed(), "Locked user should see an error"
        assert "locked out" in login.get_error_message().lower()