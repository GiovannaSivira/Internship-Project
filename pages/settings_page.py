from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


# CLK_SETTINGS = (By.XPATH, "//a[@href='/settings']//div[@class='menu-button-text']")
#     CLK_COMMUNITY = (By.XPATH, "//a[@href='/community']//div[@class='setting-text']")
# CONTCT_SUPPRT_BUTN = (By.ID, "w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf-7f66deba")

class SettingsPage(Page):
    CLK_SETTINGS = (By.XPATH, "//a[@href='/settings']")
    CLK_COMMUNITY = (By.XPATH, "//a[@href='/community']//div[@class='setting-text']")
    CONTACT_SUPPORT_BUTTON = (By.ID, "w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf-7f66deba")

    def click_on_settings(self):
        sleep(4)
        self.wait_and_click(*self.CLK_SETTINGS)

    def click_on_community(self):
        sleep(4)
        self.wait_and_click(*self.CLK_COMMUNITY)

    def verify_community_page_opens(self):
        sleep(5)
        self.verify_partial_url('/community')

    def verify_contact_support_button(self):
        sleep(5)
        actual_text = self.find_element(*self.CONTACT_SUPPORT_BUTTON).text
        assert actual_text == "Contact support", f"Contact support button was not set to {actual_text}"
        self.wait_and_click(*self.CONTACT_SUPPORT_BUTTON)
