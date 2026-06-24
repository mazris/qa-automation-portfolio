class LoginPage:

    URL = "https://www.saucedemo.com"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)

    def enter_username(self, username):
        self.page.fill("#user-name", username)

    def enter_password(self, password):
        self.page.fill("#password", password)

    def click_login(self):
        self.page.click("#login-button")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.page.inner_text(".error-message-container h3")

    def is_error_visible(self):
        return self.page.locator(".error-message-container").is_visible()