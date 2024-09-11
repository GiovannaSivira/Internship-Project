from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    #
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # # options.add_argument('--window-size=1920x1080')
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(
    #     service=service,
    #     options=options
    # )

    ### BROWSERSTACK ###
    # bs_user = 'giovannasivira_bEaNqt'
    # bs_key = '7XeRVV3R286Np9HSbxVg'
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": 'Windows',
    #     "osVersion": "11",
    #     'browserName': 'Firefox',
    #     'browserVersion': 'latest - beta',
    #     'sessionName': scenario_name
    #
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

##Mobile Emulation
    ##Set-up Chrome for mobile emulator

    chrome_options = Options()
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

   #Initialize Chrome Webdriver with mobile emulation
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)


    # context.driver.maximize_window()
    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
