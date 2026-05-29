from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Page Object for checkout step one and step two pages.
    Step 1 URL: https://www.saucedemo.com/checkout-step-one.html
    Step 2 URL: https://www.saucedemo.com/checkout-step-two.html
    """

    # --- Step 1 Locators ---
    FIRST_NAME      = (By.ID, "first-name")
    LAST_NAME       = (By.ID, "last-name")
    POSTAL_CODE     = (By.ID, "postal-code")
    CONTINUE_BTN    = (By.ID, "continue")
    ERROR_MESSAGE   = (By.CSS_SELECTOR, "[data-test='error']")

    # --- Step 2 Locators ---
    FINISH_BTN      = (By.ID, "finish")
    ITEM_TOTAL      = (By.CLASS_NAME, "summary_subtotal_label")
    TAX             = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_PRICE     = (By.CLASS_NAME, "summary_total_label")
    CANCEL_BTN      = (By.ID, "cancel")

    # --- Confirmation Locators ---
    CONFIRM_HEADER  = (By.CLASS_NAME, "complete-header")
    CONFIRM_TEXT    = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BTN   = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)

    # --- Step 1 actions ---
    def enter_first_name(self, value):
        field = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        field.clear()
        field.send_keys(value)

    def enter_last_name(self, value):
        self.driver.find_element(*self.LAST_NAME).clear()
        self.driver.find_element(*self.LAST_NAME).send_keys(value)

    def enter_postal_code(self, value):
        self.driver.find_element(*self.POSTAL_CODE).clear()
        self.driver.find_element(*self.POSTAL_CODE).send_keys(value)

    def fill_checkout_info(self, first, last, postal):
        """Fill all step 1 fields at once."""
        self.enter_first_name(first)
        self.enter_last_name(last)
        self.enter_postal_code(postal)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def get_error_message(self):
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return el.text
        except Exception:
            return ""

    def is_error_displayed(self):
        return self.get_error_message() != ""

    # --- Step 2 actions ---
    def get_item_total(self):
        return self.driver.find_element(*self.ITEM_TOTAL).text

    def get_total_price(self):
        return self.driver.find_element(*self.TOTAL_PRICE).text

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def click_cancel(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_BTN)).click()

    # --- Confirmation actions ---
    def get_confirmation_header(self):
        return self.wait.until(EC.visibility_of_element_located(self.CONFIRM_HEADER)).text

    def is_order_confirmed(self):
        return "Thank you" in self.get_confirmation_header()

    def click_back_to_products(self):
        self.driver.find_element(*self.BACK_HOME_BTN).click()

# Page Object Model - Checkout Page
# Contains all locators and actions for saucedemo.com checkout pages