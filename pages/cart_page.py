from pages.base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = page.get_by_test_id("checkout")
        self.cart_item = page.locator(".inventory_item_name")

    def proceed_to_checkout(self):
        self.checkout_button.click()

    def assert_cart_item(self, item_name):
        expect(self.cart_item).to_have_text(item_name)
