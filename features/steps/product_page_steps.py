from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product page \'{url}\'')
def open_target(context, url):
    print(f"➡ Navigating to URL: {url!r}")
    context.driver.get(url)
    sleep(8)



@then('Verify user can click through colors "{expected_colors}"')
def step_verify_colors(context, expected_colors):
    expected_colors = [c.strip() for c in expected_colors.split(",")]
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for c in colors:
        c.click()
        #sleep(2)
        selected_element = context.driver.wait.until(
            EC.visibility_of_element_located(SELECTED_COLOR)
        )

        selected_color_text = selected_element.text
        print('Current color:', selected_color_text)

        if '\n' in selected_color_text:
            selected_color = selected_color_text.split('\n')[1].strip()
        else:
            selected_color = selected_color_text.strip().replace("Color", "").strip()

        actual_colors.append(selected_color)
        print("Actual colors so far:", actual_colors)
        #sleep(1)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'



@then('Verify user can click through colors')
def step_verify_colors(context):
    expected_colors = ['Navy Denim', 'Dark Wash', 'Light Wash']

    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        c.click()
        sleep(2)
        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
