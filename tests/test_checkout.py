from playwright.sync_api import expect

def test_complete_checkout_flow(logged_in_page):
    #1. Add item and go to cart
    logged_in_page.get_by_text('Sauce Labs Backpack').click()
    logged_in_page.get_by_role('button', name='Add to cart').click()
    logged_in_page.locator('a.shopping_cart_link').click()

    #2. Assert we are in the cart
    expect(logged_in_page).to_have_url('/cart.html')
    expect(logged_in_page.locator('.inventory_item_name')).to_have_text('Sauce Labs Backpack')

    #3. Proceed to checkout
    logged_in_page.get_by_test_id('checkout').click()

    # Fill form
    logged_in_page.get_by_test_id('firstName').fill('John')
    logged_in_page.get_by_test_id('lastName').fill('Doe')
    logged_in_page.get_by_test_id('postalCode').fill('12345')
    logged_in_page.get_by_test_id('continue').click()

    #4. Final Overview Assertion
    expect(logged_in_page.locator('.summary_total_label')).to_contain_text('$32.39')

    # Finish the purchase
    logged_in_page.get_by_test_id('finish').click()

    #5. Assert we see the success message
    expect(logged_in_page.get_by_role('heading')).to_have_text('Thank you for your order!')

    expect(logged_in_page.locator('.shopping_cart_badge')).not_to_be_visible()