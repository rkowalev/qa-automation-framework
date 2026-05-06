from playwright.sync_api import Page

class LoginPage():
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.flash_message = page.locator("#flash")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def flash_text(self):
        return self.flash_message.text_content()