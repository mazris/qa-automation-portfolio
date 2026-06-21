from playwright.sync_api import sync_playwright

def test_add_todo_item():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")

        # Add three items
        items = [
            "Restock coffee mugs",
            "Check inventory levels",
            "Process loyalty customer returns"
        ]

        for item in items:
            page.fill(".new-todo", item)
            page.press(".new-todo", "Enter")

        # Verify all 3 items were added
        todo_count = page.locator(".todo-list li").count()
        print(f"Items in list: {todo_count}")

        if todo_count == 3:
            print("PASS — all 3 items added correctly")
        else:
            print(f"FAIL — expected 3 items but got {todo_count}")

        # Complete the first item
        page.locator(".todo-list li").first.locator(".toggle").click()

        # Verify 2 items remaining
        page.click(".filters a[href='#/active']")
        active_count = page.locator(".todo-list li").count()

        if active_count == 2:
            print("PASS — completing item works correctly")
        else:
            print(f"FAIL — expected 2 active items but got {active_count}")

        # Delete the second item
        second_item = page.locator(".todo-list li").first
        second_item.hover()
        second_item.locator(".destroy").click()

        # Verify 1 item remaining
        remaining = page.locator(".todo-list li").count()

        if remaining == 1:
            print("PASS — delete item works correctly")
        else:
            print(f"FAIL — expected 1 item but got {remaining}")

        page.screenshot(path="todo_test_result.png")
        print("Screenshot saved")
        browser.close()


test_add_todo_item()
