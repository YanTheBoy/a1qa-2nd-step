from default_page import BasePage
from selenium.webdriver.common.by import By


class ExamplePageLocators:
    H1_HEADER = (By.XPATH, '/html/body/div/h1')


class ExamplePage(BasePage):
    def get_h1_text(self):
        return self.find_element(ExamplePageLocators.H1_HEADER).text
