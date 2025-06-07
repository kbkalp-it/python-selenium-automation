from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on Cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()

@when('Click Account')
def click_account(context):
    context.driver.find_element(By.XPATH, "//span[text()='Account']").click()

@when('Click navigation menu, click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

@then("Verify 'Your cart is empty' is shown")
def verify_your_cart_is_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]').text
    expected_text = 'Your cart is empty'
    assert actual_text == expected_text, f"Error: expected \"{expected_text}\" not in \"{actual_text}\""

@then('Sign in form is opened')
def open_sign_in(context):
    expected_text = "Sign in or create account"
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in or create account')]").text
    assert expected_text in actual_text, f'Error: expected "{expected_text}" not in "{actual_text}"'
