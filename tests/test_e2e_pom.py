def test_full_checkout_path(login_page, products_page, cart_page):
    # Setup
    login_page.navigate("/")
    login_page.login("standard_user", "secret_sauce")
    
    # Action
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.page.locator(".shopping_cart_link").click()
    
    # Using CartPage
    cart_page.assert_cart_item("Sauce Labs Backpack")
    cart_page.proceed_to_checkout()