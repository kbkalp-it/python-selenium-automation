from time import sleep
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@given('I open the Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')