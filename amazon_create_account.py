from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&showRememberMe=true&openid.pape.max_auth_age=0&pageId=usflex&prepopulatedLoginId=&openid.assoc_handle=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&policy_handle=Retail-Checkout')

driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

driver.find_element(By.CSS_SELECTOR, '#ap_email')

driver.find_element(By.CSS_SELECTOR, '[placeholder="First and last name"][name="customerName"]')

driver.find_element(By.CSS_SELECTOR, 'input#ap_password.a-input-text.a-span12.auth-required-field')

driver.find_element(By.CSS_SELECTOR, "[aria-describedby*='ap_password_check_context']")

driver.find_element(By.CSS_SELECTOR, '[class*="a-button-input"][aria-labelledby="auth-continue-announce"]')

driver.find_element(By.CSS_SELECTOR, "div.a-section a[href*='sign_in']")

driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_condition_of_use']")

driver.find_element(By.CSS_SELECTOR, "div.a-row.a-spacing-top-medium a[href*='privacy']")