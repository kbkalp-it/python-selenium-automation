from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

@then("Verify 'Your cart is empty' is shown")
def verify_your_cart_is_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]').text
    expected_text = 'Your cart is empty'
    assert actual_text == expected_text, f"Error: expected \"{expected_text}\" not in \"{actual_text}\""

@then('Verify Cart item is present')
def verify_cart_item_is_present(context):
    sleep(3)
    cart_item = context.driver.find_element(By.XPATH, "//div[@data-test='cartItem-title']").text
    print(f"Product {cart_item} found in cart.")