# Selenium Automation Framework — Saucedemo E-Commerce

A Python-based test automation framework built with **Selenium WebDriver** and **pytest**, demonstrating end-to-end UI testing for an e-commerce web application.

---

## Project Overview

This framework automates **20 test cases** across three core user flows — Login, Products, and Checkout — on the publicly available demo site [saucedemo.com](https://www.saucedemo.com).

Built using the **Page Object Model (POM)** design pattern for maintainability and scalability.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Selenium WebDriver | Browser automation |
| pytest | Test execution and assertions |
| pytest-html | HTML test reports |
| webdriver-manager | Auto ChromeDriver management |
| Page Object Model | Framework design pattern |

---

## Project Structure

```
selenium-framework/
│
├── pages/                        # Page Object classes
│   ├── __init__.py
│   ├── login_page.py             # Login page locators and actions
│   ├── products_page.py          # Products/inventory page
│   ├── cart_page.py              # Shopping cart page
│   └── checkout_page.py          # Checkout step 1 and 2 pages
│
├── tests/                        # Test files
│   ├── __init__.py
│   ├── test_login.py             # 6 login test cases
│   ├── test_products.py          # 7 product test cases
│   └── test_checkout.py          # 7 checkout test cases
│
├── reports/                      # Auto-generated HTML test reports
├── conftest.py                   # pytest fixtures — browser setup/teardown
├── requirements.txt              # Project dependencies
└── README.md
```

---

## Test Cases Covered

### Login (6 tests)
- Valid login redirects to products page
- Invalid password shows error message
- Invalid username shows error message
- Empty username shows validation error
- Empty password shows validation error
- Locked out user sees specific error

### Products (7 tests)
- Products page title is correct
- Exactly 6 products are displayed
- Adding one item updates cart badge to 1
- Adding all items updates cart badge to 6
- Sort by name A to Z works correctly
- Sort by name Z to A works correctly
- Sort by price low to high works correctly

### Checkout (7 tests)
- Cart shows correct item after adding
- Removing item from cart empties the cart
- Missing first name shows validation error
- Missing last name shows validation error
- Missing postal code shows validation error
- Valid checkout info navigates to order summary
- Completing checkout shows order confirmation

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/selenium-automation-framework.git
cd selenium-automation-framework
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run all tests**
```bash
pytest tests/
```

**4. Run with HTML report**
```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

**5. Run a specific test file**
```bash
pytest tests/test_login.py -v
```

---

## Sample Test Report

After running, open `reports/report.html` in your browser to see a full test report with pass/fail status for each test case.

---

## Key Concepts Demonstrated

- **Page Object Model (POM)** — each page has its own class with locators and actions separated from test logic
- **pytest fixtures** — `conftest.py` handles browser setup and teardown automatically
- **Explicit waits** — `WebDriverWait` used throughout to handle dynamic elements reliably
- **Meaningful assertions** — every test has a clear assertion message explaining what failed
- **Real-world test scenarios** — covers positive flows, negative flows, and boundary/validation cases

---

## Author

**Anudeep Burra**  
MSc Computing — Sheffield Hallam University  
[LinkedIn](https://www.linkedin.com/in/anudeepburra/) | [GitHub] (https://github.com/Anudeep151998)