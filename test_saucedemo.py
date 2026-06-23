from idlelib import browser, config

from playwright.sync_api import sync_playwright

def test_valid_cred():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")
        page.fill("#user-name","standard_user")
        page.fill("#password","secret_sauce")
        page.click("#login-button")

        page.wait_for_url("**/inventory.html")
        title = page.inner_text(".title")

        if title == "Products":
            print("PASS — valid login navigates to products page")

        else:
            print(f"FAIL — expected 'Products' but got '{title}'")

        browser.close()

def test_invalid_cred():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name","standard_user")
        page.fill("#password","wrong_password")
        page.click("#login-button")

        error = page.locator(".error-message-container")
        is_visible = error.is_visible()
        if is_visible:
            print("PASS — invalid login shows error message")

        else:
            print("FAIL — error message did not appear")

        browser.close()

def test_addtocart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_url("**/inventory.html")

        page.locator(".btn_inventory").first.click()
        cart_count = page.inner_text(".shopping_cart_badge")
        if cart_count == "1":
            print("PASS — item added to cart correctly")
        else:
            print(f"FAIL — expected cart count 1 but got '{cart_count}'")

        browser.close()

def test_checkout_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_url("**/inventory.html")

        # Add item to cart
        page.locator(".btn_inventory").first.click()

        # Go to cart
        page.click(".shopping_cart_link")
        page.wait_for_url("**/cart.html")

        # Verify item is in cart
        cart_items = page.locator(".cart_item").count()
        if cart_items == 1:
            print("PASS — item appears in cart")
        else:
            print(f"FAIL — expected 1 cart item but got {cart_items}")

        # Proceed to checkout
        page.click("#checkout")
        page.wait_for_url("**/checkout-step-one.html")

        # Fill in customer details
        page.fill("#first-name", "Sarah")
        page.fill("#last-name", "Johnson")
        page.fill("#postal-code", "10001")
        page.click("#continue")

        # Verify order summary page
        page.wait_for_url("**/checkout-step-two.html")
        summary_title = page.inner_text(".title")

        if summary_title == "Checkout: Overview":
            print("PASS — order summary page loaded correctly")
        else:
            print(f"FAIL — expected checkout overview but got '{summary_title}'")

        # Complete order
        page.click("#finish")
        page.wait_for_url("**/checkout-complete.html")

        # Verify confirmation
        confirmation = page.inner_text(".complete-header")

        if confirmation == "Thank you for your order!":
            print("PASS — order completed successfully")
        else:
            print(f"FAIL — expected confirmation message but got '{confirmation}'")

        # Screenshot as evidence
        page.screenshot(path="checkout_complete.png")

        browser.close()

test_valid_cred()
test_invalid_cred()
test_addtocart()
test_checkout_flow()