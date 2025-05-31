# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# driver.get('https://www.target.com/')
# sleep(10)
#
# driver.find_element(By.XPATH, "//span[text() = 'Account']").click()
#
# sleep(5)
#
#
# driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
#
# # driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]").click()
#
# sleep(5)
#
# # expected_text = "Sign in or create account"
# # actual_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in or create account')]").text
# # assert expected_text in actual_text, f'Error, expected "{expected_text}" not in "{actual_text}"'
# # print("passed")

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome driver
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')
sleep(10)

driver.find_element(By.XPATH, "//span[text()='Account']").click()
sleep(5)

driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(5)

# Verify heading text
expected_text = "Sign in or create account"
actual_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in or create account')]").text

assert expected_text in actual_text, f'Error: expected "{expected_text}" not in "{actual_text}"'
print("Page heading is correct.")

# Sign in button is present
driver.find_element(By.XPATH, "//button[@data-test='login']")
print("Sign in button is present.")

driver.quit()