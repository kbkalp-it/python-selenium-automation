from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
HEADER_LINKS =  (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
ACCOUNT_ICON = (By.XPATH, "//span[text()='Account']")

@when('Click on Cart')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


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
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    # context.driver.implicitly_wait(2)
    sleep(5)


@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)

    # 6 == 6
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'