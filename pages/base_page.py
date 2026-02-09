from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = ""):
        # This uses the base_url from pytest.ini automatically
        self.page.goto(path)

    def get_title(self):
        return self.page.title()