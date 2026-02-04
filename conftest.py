import pytest
from playwright.sync_api import Page

# This piece of code tells Playwright to look for 'data-test' instead of 'data-testid'
@pytest.fixture(scope="session", autouse=True)
def configure_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")
    
@pytest.fixture
def logged_in_page(page: Page):

    page.goto("/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # Return the page object to the test
    yield page 
    
