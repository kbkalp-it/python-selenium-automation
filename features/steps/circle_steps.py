from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By


@then('I should see at least 10 benefit cells')
def step_impl(context):
    sleep(5)
    benefit_cell = context.driver.find_elements(By.XPATH, "//a[contains(@data-test, '@web/slingshot-components/CellsComponent/Link')]")
    print(len(benefit_cell))
    assert len(benefit_cell) > 10, f"Expected at least 10 benefit cells, {len(benefit_cell)} cells found"