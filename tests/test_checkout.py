import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

VALID_USER     = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture(autouse=True)
def login_and_add_item(driver):
    """Login, add one item, go to cart before each test."""
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USER, VALID_PASSWORD)

    products = ProductsPage(driver)
    products.add_first_item_to_cart()
    products.go_to_cart()

    # Wait until cart page is fully loaded
    WebDriverWait(driver, 10).until(EC.url_contains("cart"))


class TestCheckout:

    def test_cart_shows_added_item(self, driver):
        """TC14: Cart should show 1 item."""
        cart = CartPage(driver)
        assert cart.get_cart_item_count() == 1

    def test_remove_item_from_cart(self, driver):
        """TC15: Removing item should empty the cart."""
        cart = CartPage(driver)
        cart.remove_first_item()

        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        assert cart.is_cart_empty()

    def test_checkout_missing_first_name_shows_error(self, driver):
        """TC16: Missing first name should show error."""
        cart = CartPage(driver)
        cart.click_checkout()

        # Wait for the first name INPUT field to appear — more reliable than URL
        wait = WebDriverWait(driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

        checkout = CheckoutPage(driver)
        # Only fill last name and postal — leave first name empty
        checkout.enter_last_name("Burra")
        checkout.enter_postal_code("S1 1AA")
        checkout.click_continue()

        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        ))
        assert checkout.is_error_displayed()

    def test_checkout_missing_last_name_shows_error(self, driver):
        """TC17: Missing last name should show error."""
        cart = CartPage(driver)
        cart.click_checkout()

        wait = WebDriverWait(driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

        checkout = CheckoutPage(driver)
        checkout.enter_first_name("Anudeep")
        # Leave last name empty — skip enter_last_name
        checkout.enter_postal_code("S1 1AA")
        checkout.click_continue()

        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        ))
        assert checkout.is_error_displayed()

    def test_checkout_missing_postal_code_shows_error(self, driver):
        """TC18: Missing postal code should show error."""
        cart = CartPage(driver)
        cart.click_checkout()

        wait = WebDriverWait(driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

        checkout = CheckoutPage(driver)
        checkout.enter_first_name("Anudeep")
        checkout.enter_last_name("Burra")
        # Leave postal code empty — skip enter_postal_code
        checkout.click_continue()

        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        ))
        assert checkout.is_error_displayed()

    def test_complete_checkout_shows_order_summary(self, driver):
        """TC19: Valid info should go to order summary page."""
        cart = CartPage(driver)
        cart.click_checkout()

        wait = WebDriverWait(driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

        checkout = CheckoutPage(driver)
        checkout.enter_first_name("Anudeep")
        checkout.enter_last_name("Burra")
        checkout.enter_postal_code("S1 1AA")
        checkout.click_continue()

        # Wait for finish button to appear on step two
        wait.until(EC.visibility_of_element_located((By.ID, "finish")))

        assert "checkout-step-two" in driver.current_url

    def test_finish_order_shows_confirmation(self, driver):
        """TC20: Finishing order should show Thank you confirmation."""
        cart = CartPage(driver)
        cart.click_checkout()

        wait = WebDriverWait(driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

        checkout = CheckoutPage(driver)
        checkout.enter_first_name("Anudeep")
        checkout.enter_last_name("Burra")
        checkout.enter_postal_code("S1 1AA")
        checkout.click_continue()

        # Wait for finish button on step two
        wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        checkout.click_finish()

        # Wait for confirmation header
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))

        assert checkout.is_order_confirmed()