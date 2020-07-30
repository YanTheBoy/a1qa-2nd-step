from default_page import BasePage
from selenium.webdriver.common.by import By
from element import Button
from random import choice
from string import ascii_uppercase, ascii_lowercase, digits


class JsAlertsLocators:
    JS_ALERT_BTN = (By.XPATH, '//*[@id="content"]//button[@onclick="jsAlert()"]')
    JS_CONFIRM_BTN = (By.XPATH, '//*[@id="content"]//button[@onclick="jsConfirm()"]')
    JS_PROMPT_BTN = (By.XPATH, '//*[@id="content"]//button[@onclick="jsPrompt()"]')
    JS_RESULT = (By.XPATH, '//*[@id="result"]')


class JsAlertsMainPage(BasePage):
    def click_alert_button(self):
        Button(JsAlertsLocators.JS_ALERT_BTN, self.driver).click()

    def click_confirm_button(self):
        Button(JsAlertsLocators.JS_CONFIRM_BTN, self.driver).click()

    def click_prompt_button(self):
        Button(JsAlertsLocators.JS_PROMPT_BTN, self.driver).click()

    def get_alert_text(self):
        return self.switch_to_alert().text

    def accept_alert_window(self):
        self.switch_to_alert().accept()

    def fill_string_field(self):
        alert = self.switch_to_alert()
        random_str = generate_string()
        alert.send_keys(random_str)
        return random_str

    def get_results(self):
        return self.find_element(JsAlertsLocators.JS_RESULT).text


def generate_string():
    return ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for i in range(16))
