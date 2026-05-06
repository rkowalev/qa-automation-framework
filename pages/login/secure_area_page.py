from playwright.sync_api import Page

class SecureAreaPage():
    URL_PART = "/secure"

    def __init__(self, page: Page):
        self.page = page

        self.flash_message = page.locator("#flash")
        self.logout_button = page.get_by_role("link", name="Logout")

    def logout(self):
        self.logout_button.click()

    def flash_text(self):
        return self.flash_message.text_content()