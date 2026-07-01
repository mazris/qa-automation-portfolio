# QA Automation Portfolio

A three-tier test automation framework built with Python and Playwright,
following the Page Object Model (POM) design pattern.

Built as part of my return to QA automation engineering in 2026,
after a year building MunchMind, an iOS meal planning app.

---

## Framework structure

qa-automation-portfolio/

├── pages/ # Page object classes — one per page

│   ├── login_page.py

│   ├── inventory_page.py

│   ├── cart_page.py

│   └── checkout_page.py

├── tests/ # UI test suites

│   ├── test_login.py

│   └── test_checkout.py

├── api/ # API client and API test suites

│   ├── api_client.py

│   ├── test_users_api.py

│   └── test_pos_integration.py

├── db/  # Database helper for setup and verification

│   └── db_helper.py

├── mock_backend/ # Local Flask backend connected to MySQL

│   └── app.py

├── data/  # Centralized test data

│   └── test_data.py

├── conftest.py  # Shared browser setup and teardown

├── pytest.ini   # Pytest configuration and markers

└── run_tests.sh # One-command test suite runner


---

## Tech stack

- Python 3
- Playwright
- pytest
- Flask
- MySQL / pymysql
- Allure reporting
- Git / GitHub

---

## Test coverage

### UI tests — Playwright + POM (tests/)
- Valid login navigates to products page
- Invalid credentials show correct error message
- Locked user sees correct error message
- Full E2E checkout flow — login → add to cart → checkout → confirmation
- Add item to cart and remove — cart count verified at each step

### API tests — requests (api/)
- GET valid user returns 200 with correct data
- GET non-existent user returns 404
- POST create user returns 201 with created data
- PUT update user returns 200 with updated data
- DELETE user returns 200
- GET all users returns non-empty list

### Integration tests — API + DB (api/test_pos_integration.py)
- Customer data from API matches database directly
- Active promo code applied via API — discount calculated correctly
- Inactive promo code rejected via API — returns 400
- Loyalty points updated via API — change verified directly in DB

---

## How to set up

### 1 — install dependencies
pip3 install pytest-playwright pymysql flask requests allure-pytest

playwright install

brew install allure

### 2 — set up MySQL database
mysql -u root -p

CREATE DATABASE pos_test_db;

Then run the table and data setup scripts in db/setup.sql

### 3 — start the local Flask backend
python3 mock_backend/app.py

Leave this running in a separate terminal tab before running integration tests.

---

## How to run

Run all tests with automatic Allure report:
./run_tests.sh

Run smoke suite only:
./run_tests.sh smoke

Run regression suite only:
./run_tests.sh regression

Run a specific file:
pytest tests/test_login.py -v
pytest api/test_pos_integration.py -v

---

## Key design decisions

**Page Object Model** — each page has its own class with methods
for every interaction. Tests never touch selectors directly.
If a selector changes it's fixed in one place, not across every test file.

**Centralized test data** — all usernames, passwords, expected
messages, and customer details live in one TestData class.
Tests stay clean and data is easy to maintain.

**Three-tier integration** — integration tests use a real local
Flask backend connected to MySQL. API calls genuinely read from
and write to the database. DB verification after API calls confirms
actual state change, not assumed behavior.

**DB helper as support layer** — the database helper is not a
standalone test layer. It's used to set up preconditions before
tests run and verify DB state after API calls complete.

**wait_for_load_state over wait_for_url** — learned through debugging
that networkidle is more reliable than URL pattern matching for
single-page app navigation in Playwright.

**Transaction isolation fix** — when two separate DB connections
are active simultaneously (Flask backend + test fixture), MySQL's
REPEATABLE READ isolation can cause stale reads. Fixed by calling
connection.commit() before SELECT queries in db_helper.py to force
a fresh transaction snapshot.

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
