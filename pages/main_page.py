from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    EMAIL_TEXT_FIELD = (By.ID, 'email-2')
    PASSWORD_TEXT_FIELD = (By.ID, 'field')
    CONTINUE_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")

    def open(self):
        self.open_url('https://soft.reelly.io')

    def signin_to_the_page(self, email, password):
        self.input_text(email, *self.EMAIL_TEXT_FIELD)
        self.input_text(password, *self.PASSWORD_TEXT_FIELD)
        self.click(*self.CONTINUE_BTN)
