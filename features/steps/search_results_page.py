from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify search worked for tea')
def verify_search_worked(context):
    actual_text_content = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert 'tea' in actual_text_content, f"Error, expected 'tea' not in {actual_text_content}"


@then('Verify search worked for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert product in actual_text, f"Error, expected {product} not in actual {actual_text}"

@when('Click on Add to Cart on search result')
def click_on_search_results(context):
    sleep(3)
    context.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Add Tazo Organic Tea Latte Chai Black Tea')]").click()