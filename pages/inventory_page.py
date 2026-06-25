class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.inner_text(".title")

    def add_first_item_to_cart(self):
        self.page.locator(".btn_inventory").first.click()

    def add_item_to_cart_by_name(self, item_name):
        item = self.page.locator(".inventory_item").filter(
            has=self.page.locator(".inventory_item_name", has_text=item_name)
        )
        item.locator("button").click()

    def remove_first_item_from_cart(self):
        self.page.locator(".btn_inventory").first.click()

    def get_cart_count(self):
        badge = self.page.locator(".shopping_cart_badge")
        if badge.is_visible():
            return int(badge.inner_text())
        return 0

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()
        self.page.wait_for_load_state("networkidle")

    def open_product_details(self,item_name):
        self.page.locator(".inventory_item").filter(has_text=item_name).locator(".inventory_item_name").click()

    def get_all_item_names(self):
        items = self.page.locator(".inventory_item_name").all()
        return [item.inner_text() for item in items]
