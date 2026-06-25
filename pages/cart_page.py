class CartPage:

    def __init__(self, page):
        self.page = page

    def get_cart_items_count(self):
        return self.page.locator(".cart_item").count()

    def get_item_names(self):
        items = self.page.locator(".inventory_item_name").all()
        return [item.inner_text() for item in items]

    def remove_item_by_name(self,item_name):
        item = self.page.locator(".cart_item").filter(has_text=item_name)
        item.locator("button").click()

    def proceed_to_checkout(self):
        self.page.click("#checkout")

    def continue_shopping(self):
        self.page.click("#continue-shopping")

    def get_title(self):
        return self.page.inner_text(".title")