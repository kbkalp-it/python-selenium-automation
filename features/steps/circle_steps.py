from behave import given, when, then

@then('I should see at least 10 benefit cells')
def step_impl(context):
    context.app.circle_page.open_circle_page()