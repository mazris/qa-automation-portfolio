import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import allure
from api.api_client import POSAPIClient
from db.db_helper import DBHelper

@pytest.fixture
def pos_client():
    return POSAPIClient()

@pytest.fixture
def db():
    helper = DBHelper()
    yield helper
    helper.reset_all_test_data()
    helper.disconnect()

@pytest.mark.smoke
@allure.suite("Smoke Suite")
@allure.description("Verify customer data from API matches the database directly")
def test_get_customer_matches_db(pos_client, db):
    # Get directly from DB first
    db_customer = db.get_customer_by_id(1)

    # Get same customer through the API
    response = pos_client.get_customer(1)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    api_customer = response.json()

    # Verify API response matches DB exactly
    assert api_customer["name"] == db_customer["name"], \
        "API response does not match DB data"
    assert api_customer["loyalty_points"] == db_customer["loyalty_points"], \
        "Loyalty points mismatch between API and DB"

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description(
    "Verify promo code exists in DB, apply it via real API call, "
    "confirm calculated discount is correct"
)
def test_apply_active_promo_code(pos_client, db):
    # Step 1 — DB setup: insert a fresh promo code
    db.insert_promo_code("TESTPROMO", 10, "2026-12-31")

    # Step 2 — DB verify setup
    promo = db.get_promo_code("TESTPROMO")
    assert promo is not None, "Promo code not found in DB before API call"
    assert promo["is_active"] == 1

    # Step 3 — real API call that reads from the DB and calculates discount
    response = pos_client.apply_promo("TESTPROMO", cart_total=50.00)
    assert response.status_code == 200, \
        f"Expected 200 but got {response.status_code}"

    data = response.json()
    expected_discount = 50.00 * 0.10
    expected_total = 50.00 - expected_discount

    assert data["discount_amount"] == round(expected_discount, 2), \
        f"Expected discount {expected_discount} but got {data['discount_amount']}"
    assert data["final_total"] == round(expected_total, 2), \
        f"Expected total {expected_total} but got {data['final_total']}"

    # Step 4 — cleanup
    db.delete_promo_code("TESTPROMO")

@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify applying an inactive promo code returns an error")
def test_apply_inactive_promo_code(pos_client, db):
    # Setup — insert an inactive promo code
    db.insert_promo_code("EXPIRED1", 15, "2025-01-01")
    db.deactivate_promo_code("EXPIRED1")

    # API call
    response = pos_client.apply_promo("EXPIRED1", cart_total=50.00)

    assert response.status_code == 400, \
        f"Expected 400 but got {response.status_code}"

    # Cleanup
    db.delete_promo_code("EXPIRED1")


@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description(
    "Update loyalty points via real API call, "
    "verify the change persisted directly in the database"
)
def test_update_loyalty_points_persists_to_db(pos_client, db):
    # Step 1 — confirm starting state in DB
    customer = db.get_customer_by_id(1)
    assert customer["loyalty_points"] == 500

    # Step 2 — real API call to update points
    response = pos_client.update_loyalty_points(1, 250)
    assert response.status_code == 200, \
        f"Expected 200 but got {response.status_code}"

    # Step 3 — verify the API response itself
    data = response.json()
    assert data["loyalty_points"] == 250, \
        f"Expected 250 in API response but got {data['loyalty_points']}"

    # Step 4 — verify directly in the DB, independent of the API
    db_customer = db.get_customer_by_id(1)
    assert db_customer["loyalty_points"] == 250, \
        f"Expected 250 in DB but got {db_customer['loyalty_points']}"