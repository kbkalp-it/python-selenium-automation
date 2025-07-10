from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*=addToCartButton]")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


@then('Verify search worked for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results()

@when('Click on Add to Cart')
def click_on_search_results(context):
    context.driver.wait.until(EC.presence_of_element_located(ADD_TO_CART_BTN))
    add_to_cart_btn = context.driver.find_element(*ADD_TO_CART_BTN)
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_btn)
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN))
    #context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),message = 'Product name was not visible')
    add_to_cart_btn.click()

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored: ', context.product_name)

@when("Click on 'Add to Cart' from side navigation")
def click_on_cart(context):
    context.driver.implicitly_wait(3)
    context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART)).click()

# @when('View Cart and Checkout')
# def view_checkout(context):
#     context.driver.implicitly_wait(3)
#     context.driver.find_element().click(*VIEW_CART_CHECKOUT)