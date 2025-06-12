from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

@then("Click on 'Add to Cart'")
def click_on_cart(context):
    sleep(3)
    context.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Add to cart for Tazo Organic Tea Latte Chai Black Tea')]").click()

@then('View Cart and Checkout')
def view_checkout(context):
    sleep(3)
    context.driver.find_element(By.XPATH, "//a[contains(@class, 'styles_ndsButtonSecondary')]").click()