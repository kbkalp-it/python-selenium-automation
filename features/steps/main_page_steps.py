from behave import given, when, then


@given('Open target main page')
def open_target(context):
    context.app.main_page.open_main_page()

@given('I open the Target Circle page')
def open_target_circle(context):
    context.app.main_page.open_circle_main_page()