from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

ITEM_TITLE = (By.XPATH, "//div[@data-test='cartItem-title']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@then("Verify 'Your cart is empty' is shown")
def verify_cart_empty(context):
     context.app.cart_page.verify_cart_empty()

@then('Verify Cart item is present')
def verify_cart_item_is_present(context):
    context.driver.implicitly_wait(3)
    cart_item = context.driver.find_element(*ITEM_TITLE).text
    print(f"Product {cart_item} found in cart.")

@when('Open cart page')
def open_cart_page(context):
    context.driver.get("https://www.target.com/cart")

@then('Verify cart has correct product')
def verify_product_name(context):
    # context.product_name => stored before
    product_name_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    print('Name in cart: ', product_name_in_cart)

    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'