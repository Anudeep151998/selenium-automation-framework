import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

VALID_USER     = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture(autouse=True)
def login_first(driver, request):
    """
    Runs before every test in this file.
    Logs in so each test starts on the products page.
    """
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USER, VALID_PASSWORD)
    request.node.driver = driver  # pass driver to tests via request


class TestProducts:
    """
    7 test cases covering the products/inventory page.
    """

    def test_products_page_title_is_correct(self, driver):
        """TC07: Page title should display 'Products'."""
        products = ProductsPage(driver)
        assert products.get_page_title() == "Products", \
            "Page title should be 'Products'"

    def test_six_products_are_displayed(self, driver):
        """TC08: Saucedemo always shows exactly 6 products."""
        products = ProductsPage(driver)
        assert products.get_product_count() == 6, \
            f"Expected 6 products, got {products.get_product_count()}"

    def test_add_single_item_updates_cart_badge(self, driver):
        """TC09: Adding one item should show badge count of 1 on cart icon."""
        products = ProductsPage(driver)
        products.add_first_item_to_cart()

        assert products.get_cart_badge_count() == 1, \
            "Cart badge should show 1 after adding one item"

    def test_add_all_items_updates_cart_badge(self, driver):
        """TC10: Adding all 6 items should show badge count of 6."""
        products = ProductsPage(driver)
        products.add_all_items_to_cart()

        assert products.get_cart_badge_count() == 6, \
            "Cart badge should show 6 after adding all items"

    def test_sort_products_by_name_a_to_z(self, driver):
        """TC11: Sorting A-Z should return products in alphabetical order."""
        products = ProductsPage(driver)
        products.sort_products("az")

        names = products.get_all_product_names()
        assert names == sorted(names), \
            "Products should be in A-Z alphabetical order"

    def test_sort_products_by_name_z_to_a(self, driver):
        """TC12: Sorting Z-A should return products in reverse alphabetical order."""
        products = ProductsPage(driver)
        products.sort_products("za")

        names = products.get_all_product_names()
        assert names == sorted(names, reverse=True), \
            "Products should be in Z-A reverse alphabetical order"

    def test_sort_products_by_price_low_to_high(self, driver):
        """TC13: Sorting by price low-to-high should return ascending prices."""
        products = ProductsPage(driver)
        products.sort_products("lohi")

        prices = products.get_all_product_prices()
        assert prices == sorted(prices), \
            "Product prices should be in ascending order"