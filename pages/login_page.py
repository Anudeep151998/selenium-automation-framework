from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object for https://www.saucedemo.com login page.
    All locators and actions for login are kept here.
    """

    URL = "https://www.saucedemo.com"

    # --- Locators ---
    USERNAME_INPUT    = (By.ID, "user-name")
    PASSWORD_INPUT    = (By.ID, "password")
    LOGIN_BUTTON      = (By.ID, "login-button")
    ERROR_MESSAGE     = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_CLOSE_BTN   = (By.CSS_SELECTOR, ".error-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)

    def open(self):
        """Navigate to the login page."""
        self.driver.get(self.URL)

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        """Full login action: fill username, password, and click login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Returns the visible error message text, or empty string if none."""
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return el.text
        except Exception:
            return ""

    def is_error_displayed(self):
        return self.get_error_message() != ""

    def close_error(self):
        self.driver.find_element(*self.ERROR_CLOSE_BTN).click()


# Page Object Model - Login Page
# Contains all locators and actions for saucedemo.com login page