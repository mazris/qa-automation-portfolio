class CheckoutPage:

    def __init__(self,page):
        self.page = page

    def fill_customer_details(self, first_name,last_name,postal_code):
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", postal_code)

    def click_continue(self):
        self.page.click("#continue")

    def get_summary_title(self):
        return self.page.inner_text(".title")

    def get_total(self):
        return self.page.inner_text(".summary_total_label")

    def finish_order(self):
        self.page.click("#finish")

    def get_confirmation_header(self):
        return self.page.inner_text(".complete-header")