from playwright.sync_api import Page, expect

def test_login_page_load(page: Page):
    # 1. Navigate (Uses base-url from pytest.ini)
    page.goto("/")
    
    # 2. Assert the title
    expect(page).to_have_title("Swag Labs")

    # 3. Locate elements
    username_field = page.get_by_placeholder("Username")
    password_field = page.get_by_placeholder("Password")
    login_button = page.get_by_role("button", name="Login")

    # 4. Interactions
    username_field.fill("standard_user")
    password_field.fill("secret_sauce")
    login_button.click()

    # 5. Verify successful login
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    inventory_list = page.locator(".inventory_list")
    expect(inventory_list).to_be_visible()