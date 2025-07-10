from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.base_page import Page

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
HEADER_LINKS =  (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
ACCOUNT_ICON = (By.XPATH, "//span[text()='Account']")

@when('Click on Cart')
def click_cart(context):
    context.app.header.click_cart()


@when('Click Account')
def click_account(context):
    context.driver.find_element(*ACCOUNT_ICON).click()

# @when('When Search for tea')
# def when_search_tea(context):
#     context.driver.find_element(By.ID, 'search').send_keys('tea')
#     context.driver.find_element(*SEARCH_BTN).click()
#     sleep(5)

@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search_product()

@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)

    # 6 == 6
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'