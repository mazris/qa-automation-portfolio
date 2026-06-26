# QA Automation Portfolio

A test automation framework built with python and playwright, 
following the Page Object Model (POM) design pattern.

Built as part of my return to QA automation engineering in 2026
after a year building my app, an IOS meal planning app


# Framework structure 

qa-automation-portfolio/

├── pages/          # Page object classes — one per page

├── tests/          # Test suites — one file per feature

├── data/           # Centralized test data

└── conftest.py     # Shared browser setup and teardown

## Tech stack
- Python 3
- Playwright
- pytest
- Git / GitHub

## Test coverage

### Login tests (tests/login_test.py)
- valid login navigates to product page
- invalid credentials show correct error message
- Locked user sees correct error message 

### Checkout tests (tests/test_checkout.py)

- Full E2E checkout flow - login -> add item to cart -> checkout -> confirmation
- Add item to cart and remove it - cart count verified at each step

## How to run
- Install dependencies:

pip3 install pytest-playwright

playwright install

- Run all tests:
pytest tests/ -v
- Run a specific file:
pytest tests/test_login.py -v

## Key design decisions

**Page Object Model** - each page has its own class with methods 
for every interaction. Tests never touch selectors directly.
If a selector changes it's fixed in one place, not accross every test file.

**Centralized test data** - all usernames, passwords, expected messages, and customer details live in one TestData class.
Tests stay clean and data is easy to maintain.

**wait_for_load_state over wait_for_url** - learned through debugging that networkidle is more reliable than URL pattern matching for single-page app navigation.


## Reporting

Tests generate an Allure report automatically after each run.
The report includes test status, suite grouping, descriptions, 
and screenshots on failure.

Run with automatic report:
```
./run_tests.sh          # all tests
./run_tests.sh smoke    # smoke suite only
./run_tests.sh regression  # regression suite only
```
