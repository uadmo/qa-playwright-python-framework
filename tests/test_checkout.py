from playwright.sync_api import expect

def test_complete_checkout_flow(login_page, products_page, cart_page, form_page):

    # Login
    login_page.navigate("/")
    login_page.login("standard_user", "secret_sauce")

    # Add product to cart
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.go_to_cart()

    # Assert cart item
    cart_page.assert_cart_item("Sauce Labs Backpack")
    cart_page.proceed_to_checkout()

    # Fill form
    form_page.fill_form("John", "Doe", "12345")

    # Final Overview Assertion
    form_page.assert_total("$32.39")

    # Finish the purchase
    form_page.finish_purchase()

    # Assert we see the success message
    form_page.assert_success_message("Thank you for your order!")

    expect(products_page.cart_badge).not_to_be_visible()