from playwright.sync_api import Page, expect

def test_add_specific_product_to_cart(logged_in_page):
    # 1. Locator Chaining: Find the item 'Sauce Labs Bolt T-Shirt'
    # Then find the button inside that specific item.
    product_item = logged_in_page.locator(".inventory_item").filter(has_text="Sauce Labs Bolt T-Shirt")
    product_item.get_by_role("button", name="Add to cart").click()

    # 2. Verify the Badge update
    cart_badge = logged_in_page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")

def test_sort_products_price(logged_in_page):
    # Interact with a dropdown
    logged_in_page.get_by_test_id("product-sort-container").select_option("lohi")
    
    # Assert the first item is the cheapest
    first_item_price = logged_in_page.locator(".inventory_item_price").first
    expect(first_item_price).to_contain_text("$7.99")