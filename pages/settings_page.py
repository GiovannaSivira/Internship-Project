from selenium.webdriver.common.by import By
from pages.base_page import Page


class SettingsPage(Page):
   CLK_SETTINGS = (By.XPATH, "//a[@href='/settings']//div[@class='menu-button-text']")
   CLK_COMMUNITY = (By.XPATH, "//a[@href='/community']//div[@class='setting-text']")
   CONTCT_SUPPRT_BUTN =(By. ID, "w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf-7f66deba")
   def click_on_settings(self):
      self.wait_and_click(*self.CLK_SETTINGS)

   def click_on_community(self):
      self.wait_and_click(*self.CLK_COMMUNITY)

   def verify_community_page_opens(self):
      self.verify_partial_url('/community')

   def verify_contact_support_button(self):
      self.wait_and_click(*self.CONTCT_SUPPRT_BUTN)