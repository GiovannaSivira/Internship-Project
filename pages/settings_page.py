from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


# CLK_SETTINGS = (By.XPATH, "//a[@href='/settings']//div[@class='menu-button-text']")
#     CLK_COMMUNITY = (By.XPATH, "//a[@href='/community']//div[@class='setting-text']")
# CONTCT_SUPPRT_BUTN = (By.ID, "w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf-7f66deba")

class SettingsPage(Page):
    # CLK_SETTINGS = (By.XPATH, '//div[@class="div-block-55"]//a[@href="/settings"]')
    CLK_SETTINGS = (By.XPATH, '//a[@href="/settings"]//div[@class="menu-button-text"]')
    # CLK_SETTINGS = (By.XPATH, "//a[@href='/settings']")
    # '//div[@class="circle-gradient"]'
    # CLK_COMMUNITY = (By.XPATH, '//a[@href="/community"]//div[@class="setting-text"]')
    CLK_COMMUNITY = (By.XPATH, '//a[@href="/community"]//div[@class="main-menu-text"]')
    # CLK_COMMUNITY = (By.XPATH, "//a[@href='/community']//div[@class='setting-text']")
    CONTACT_SUPPORT_BUTTON = (By.XPATH, '//a[contains(@href,"reelly_dubai_bot")]')
    # CONTACT_SUPPORT_BUTTON = (By.ID, "w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf-7f66deba")
    TWELVE_SETTNGS_OPTION = (By.XPATH, '//a[contains(@class,"page-setting-block")]')
    CONNECT_THE_COMPANY_BTN = (By.XPATH, '//div[@class="account-trial-block"]//a[@href="/book-presentation"]')
    #'//div[@class="settings-block-menu"]//a[@href="/book-presentation"]'
    #'//div[text()="Connect the company"]'
    #


    def click_on_settings(self):
        sleep(4)
        self.wait_and_click(*self.CLK_SETTINGS)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_on_community(self):
        sleep(6)
        self.wait_and_click(*self.CLK_COMMUNITY)

    def verify_community_page_opens(self):
        sleep(5)
        self.verify_partial_url('/community')

    def verify_setting_page_opens(self):
        sleep(5)
        self.verify_partial_url('/settings')

    def verify_12_setting_options(self):
        sleep(5)
        self.driver.find_elements(*self.TWELVE_SETTNGS_OPTION)

    def verify_contact_support_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        elements = self.find_elements(*self.CONTACT_SUPPORT_BUTTON)
        actual_text = elements[1].text
        assert actual_text == "Contact support", f"Contact support button was not set to {actual_text}"
        elements[1].click()
        sleep(5)

    def verify_connect_the_company_button(self):
        sleep(10)
        actual_text = self.find_element(*self.CONNECT_THE_COMPANY_BTN).text
        assert actual_text == "Connect the company", f"Connect the company {actual_text} did not appear."
