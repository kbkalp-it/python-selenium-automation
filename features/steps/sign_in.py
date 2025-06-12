from behave import given, when, then
from selenium.webdriver.common.by import By

@then('Sign in form is opened')
def open_sign_in(context):
    expected_text = "Sign in or create account"
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in or create account')]").text
    assert expected_text in actual_text, f'Error: expected "{expected_text}" not in "{actual_text}"'