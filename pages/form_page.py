from pages.base_page import BasePage
from playwright.sync_api import expect

class FormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = page.get_by_test_id("firstName")
        self.last_name_input = page.get_by_test_id("lastName")
        self.postal_code_input = page.get_by_test_id("postalCode")
        self.continue_button = page.get_by_test_id("continue")
        self.summary_total = page.locator(".summary_total_label")
        self.finish_button = page.get_by_test_id("finish")
        self.success_message = page.get_by_role("heading")

    def fill_form(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def assert_total(self, expected_total):
        expect(self.summary_total).to_contain_text(expected_total)

    def finish_purchase(self):
        self.finish_button.click()

    def assert_success_message(self, expected_message):
        expect(self.success_message).to_have_text(expected_message)