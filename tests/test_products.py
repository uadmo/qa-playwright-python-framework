from playwright.sync_api import Page, expect

def test_add_specific_product_to_cart(product_page_logged_in):
   
    product_page_logged_in.add_product_to_cart("Sauce Labs Bolt T-Shirt")

    expect(product_page_logged_in.cart_badge).to_have_text("1")

def test_sort_products_price(product_page_logged_in):
    # Interact with a dropdown
    product_page_logged_in.sort_dropdown.select_option("lohi")
    
    # Assert the first item is the cheapest
    expect(product_page_logged_in.first_product_price).to_contain_text("$7.99")