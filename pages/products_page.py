from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductsPage:

    URL = "https://www.saucedemo.com/inventory.html"

    PAGE_TITLE     = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS  = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES  = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CART_BADGE     = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON      = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN  = (By.CLASS_NAME, "product_sort_container")
    BURGER_MENU    = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK    = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)

    def is_on_products_page(self):
        try:
            self.wait.until(EC.url_contains("inventory"))
            return True
        except Exception:
            return False

    def get_page_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE)).text

    def get_all_product_names(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_NAMES)]

    def get_all_product_prices(self):
        return [float(el.text.replace("$", "")) for el in self.driver.find_elements(*self.PRODUCT_PRICES)]

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def add_first_item_to_cart(self):
        btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
        ))
        btn.click()

    def add_all_items_to_cart(self):
        # Must re-fetch buttons each loop — DOM changes after every click
        total = self.get_product_count()
        for _ in range(total):
            btns = self.driver.find_elements(By.CSS_SELECTOR, "[data-test^='add-to-cart']")
            if not btns:
                break
            btns[0].click()
            time.sleep(0.5)  # wait for DOM to update before next click

    def get_cart_badge_count(self):
        try:
            return int(self.driver.find_element(*self.CART_BADGE).text)
        except Exception:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()

    def sort_products(self, option):
        Select(self.driver.find_element(*self.SORT_DROPDOWN)).select_by_value(option)

    def logout(self):
        self.driver.find_element(*self.BURGER_MENU).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()