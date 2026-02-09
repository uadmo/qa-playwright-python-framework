from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_container = page.locator(".inventory_list")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.sort_dropdown = page.get_by_test_id("product-sort-container")
        self.first_product_price = page.locator(".inventory_item_price").first 
        self.cart_link = page.locator(".shopping_cart_link")

    def add_product_to_cart(self, product_name: str):
        product_item = self.page.locator(".inventory_item").filter(has_text=product_name)
        product_item.get_by_role("button", name="Add to cart").click()

    def go_to_cart(self):
        self.cart_link.click()