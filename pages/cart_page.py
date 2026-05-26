from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Page Object for the cart page.
    URL: https://www.saucedemo.com/cart.html
    """

    # --- Locators ---
    CART_ITEMS        = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES        = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES       = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BTNS       = (By.CSS_SELECTOR, "[data-test^='remove']")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON   = (By.ID, "checkout")
    CART_QUANTITY     = (By.CLASS_NAME, "cart_quantity")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)

    def is_on_cart_page(self):
        try:
            self.wait.until(EC.url_contains("cart"))
            return True
        except Exception:
            return False

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_item_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [el.text for el in elements]

    def get_item_prices(self):
        elements = self.driver.find_elements(*self.ITEM_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]

    def remove_first_item(self):
        btns = self.wait.until(EC.presence_of_all_elements_located(self.REMOVE_BTNS))
        btns[0].click()

    def remove_all_items(self):
        while True:
            btns = self.driver.find_elements(*self.REMOVE_BTNS)
            if not btns:
                break
            btns[0].click()

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    def click_continue_shopping(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_SHOPPING)).click()

    def is_cart_empty(self):
        return self.get_cart_item_count() == 0