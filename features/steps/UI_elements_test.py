from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Open the reely main page')
def open_reely(context):
    context.app.main_page.open()


@when('Log in to the reely page')
def Log_in(context):
    context.app.main_page.signin_to_the_page(email='giovannaloquera@hotmail.com', password='Devinj#01')


@when('Click on reely settings option')
def click_on_settings_option(context):
    context.app.settings_page.click_on_settings()


@then('Verify the right reely page opens')
def verify_setting_page_opens(context):
    context.app.settings_page.verify_setting_page_opens()


@then('Verify there are 12 options for the settings')
def verify_there_are_12_options(context):
    context.app.settings_page.verify_12_setting_options()


@then('Verify “connect the company” button is available')
def verify_connect_the_company_button(context):
    context.app.settings_page.verify_connect_the_company_button()
