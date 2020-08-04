from default_page import BasePage
from selenium.webdriver.common.by import By
from element import Button, IFrame
from assistance import generate_string
from selenium.webdriver.common.keys import Keys


class IframePageLocators:
    IFRAME_HIGHLIGHT = (By.XPATH, '//*[@id="content"]/div/h3')
    IFRAME = (By.XPATH, '//*[@id="mce_0_ifr"]')
    IFRAME_FIELD = (By.XPATH, '//*[@id="tinymce"]')
    STRONG_TEXT = (By.XPATH, '//*[@id="tinymce"]/p/strong')
    BOLD_BTN = (By.XPATH, '//div[@aria-label="Bold"]')


class IframePage(BasePage):
    def get_highlight_text(self):
        return self.find_element(IframePageLocators.IFRAME_HIGHLIGHT).text

    def get_iframe_text(self):
        return self.find_element(IframePageLocators.IFRAME_FIELD).text

    def switch_to_iframe(self):
        IFrame(IframePageLocators.IFRAME, self.driver).switch_to_iframe()

    def switch_to_default_page(self):
        self.switch_to_mainpage()

    def rewrite_iframe_field(self):
        field = self.find_element(IframePageLocators.IFRAME_FIELD)
        field.clear()
        random_string = generate_string()
        field.send_keys(random_string)
        return random_string

    def select_all_text(self):
        field = self.find_element(IframePageLocators.IFRAME_FIELD)
        field.send_keys(Keys.CONTROL + 'a')

    def make_text_bold(self):
        Button(IframePageLocators.BOLD_BTN, self.driver).click()

    def find_strong_element(self):
        return self.find_element(IframePageLocators.STRONG_TEXT).text
