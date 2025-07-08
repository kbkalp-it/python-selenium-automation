from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

BENEFIT_CELL_COUNT = (By.XPATH, "//a[contains(@data-test, '@web/slingshot-components/CellsComponent/Link')]")

@then('I should see at least 10 benefit cells')
def step_impl(context):
    context.driver.implicitly_wait(4)
    benefit_cell = context.driver.find_elements(*BENEFIT_CELL_COUNT)
    print(len(benefit_cell))
    assert len(benefit_cell) > 10, f"Expected at least 10 benefit cells, {len(benefit_cell)} cells found"