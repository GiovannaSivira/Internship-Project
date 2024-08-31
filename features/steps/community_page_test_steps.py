from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC



@given('Open the main page')
def open_reely(context):
    context.app.main_page.open()

@when('Log in to the page')
def Log_in(context):
    context.app.main_page.signin_to_the_page(email='giovannaloquera@hotmail.com', password='Devinj#01')

@when('Click on settings option')
def click_on_settings_option(context):
    context.app.settings_page.click_on_settings()

@when('Click on Community option')
def click_on_community_option(context):
    context.app.settings_page.click_on_community()
#
@then('Verify the right page opens')
def verify_community_page(context):
    context.app.settings_page.verify_community_page_opens()
#
@then('Verify “Contact support” button is available and clickable')
def verify_support_button(context):
    context.app.settings_page.verify_contact_support_button()