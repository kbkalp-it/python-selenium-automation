from behave import given, when, then
from selenium.webdriver.common.by import By

@when('Click navigation menu, click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()



