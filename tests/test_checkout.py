import sys
import os

import allure
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from data.test_data import TestData

@pytest.mark.smoke
@allure.suite("Smoke Suite")
@allure.description("Verify that a full checkout workflow works correctly from login to confirmation")
def test_full_checkout_flow(page):
    # Step 1 — login
    login = LoginPage(page)
    login.navigate()
    login.login(
        TestData.STANDARD_USER["username"],
        TestData.STANDARD_USER["password"]
    )
    page.wait_for_url("**/inventory.html")

    # Step 2 — add item to cart
    inventory= InventoryPage(page)
    assert inventory.get_title() == TestData.PRODUCTS_TITLE
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    assert inventory.get_cart_count() == 1, "FAIL — cart count should be 1 after adding item"
    print("PASS — item added to cart")

    # Step 3 — go to cart and verify

    inventory.go_to_cart()
    cart = CartPage(page)
    assert cart.get_cart_items_count() == 1, "FAIL — cart should have 1 item"
    assert "Sauce Labs Backpack" in cart.get_item_names(), "FAIL — correct item not in cart"
    print("PASS — cart contains correct item")

    # Step 4 — proceed to checkout
    cart.proceed_to_checkout()
    page.wait_for_url("**/checkout-step-one.html")
    checkout = CheckoutPage(page)
    checkout.fill_customer_details(
        TestData.CUSTOMER["first_name"],
        TestData.CUSTOMER["last_name"],
        TestData.CUSTOMER["postal_code"],
    )
    checkout.click_continue()

    # Step 5 — verify order summary
    page.wait_for_url("**/checkout-step-two.html")
    assert checkout.get_summary_title() == "Checkout: Overview", "FAIL — wrong page title"
    print("PASS — order summary page loaded")

    # Step 6 — finish order
    checkout.finish_order()
    page.wait_for_url("**/checkout-complete.html")
    confirmation = checkout.get_confirmation_header()
    assert confirmation == TestData.ORDER_CONFIRMATION, f"FAIL — got '{confirmation}'"
    print("PASS — order completed successfully")

    # Screenshot as evidence
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name="checkout complete",
        attachment_type=allure.attachment_type.PNG
    )


@pytest.mark.regression
@allure.suite("Regression Suite")
@allure.description("Verify that a user can add items to cart and remove them from cart")
def test_add_and_remove_from_cart(page):
    #Login first
    login = LoginPage(page)
    login.navigate()
    login.login(
        TestData.STANDARD_USER["username"],
        TestData.STANDARD_USER["password"]
    )
    page.wait_for_url("**/inventory.html")
    inventory = InventoryPage(page)
    # Add item
    assert inventory.get_title() == TestData.PRODUCTS_TITLE
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    assert inventory.get_cart_count() == 1, "FAIL — cart count should be 1"
    print("PASS — item added to cart")

    # Remove item
    inventory.remove_first_item_from_cart()
    assert inventory.get_cart_count() == 0, "FAIL — cart count should be 0 after removal"
    print("PASS — item removed from cart")

