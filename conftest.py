import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.form_page import FormPage

@pytest.fixture(scope="session", autouse=True)
def configure_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def products_page(page: Page):
    return ProductsPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture
def form_page(page: Page):
    return FormPage(page)

@pytest.fixture
def logged_in_setup(login_page):
    # This fixture logs in and returns the page object
    login_page.navigate("/")
    login_page.login("standard_user", "secret_sauce")
    return login_page

@pytest.fixture
def product_page_logged_in(login_page, products_page):
    """Fixture to navigate to login, perform login, and return the products page."""
    login_page.navigate("/")
    login_page.login("standard_user", "secret_sauce")
    return products_page