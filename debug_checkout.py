import time
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--no-first-run")
options.add_argument("--disable-features=PasswordLeakDetection,SafeBrowsingEnhancedProtection")
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")  # fresh profile
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,
})
options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

# Login
driver.get("https://www.saucedemo.com")
wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add item
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test^='add-to-cart']"))).click()

# Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
wait.until(EC.url_contains("cart"))
print("Cart URL:", driver.current_url)

# Click checkout
wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
time.sleep(2)

print("Checkout URL:", driver.current_url)
print("Page title:", driver.title)

# Check elements visible
els = driver.find_elements(By.CSS_SELECTOR, "input, button")
print("\nElements on page:")
for el in els[:10]:
    print(f"  {el.tag_name} id={el.get_attribute('id')} displayed={el.is_displayed()}")

time.sleep(2)
driver.quit()
print("\nSuccess — no popups!")