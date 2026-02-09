from playwright.sync_api import expect

def test_login_and_add_item(login_page, products_page):
    # 1. Login using Page Object
    login_page.navigate("/")
    login_page.login("standard_user", "secret_sauce")

    # 2. Interact using Products Page Object
    products_page.add_product_to_cart("Sauce Labs Backpack")
    
    # 3. Assertions
    expect(products_page.cart_badge).to_have_text("1")