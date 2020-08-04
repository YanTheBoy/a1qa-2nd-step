from default_page import BasePage
from selenium.webdriver.common.by import By
from element import Button
from assistance import generate_string

from string import Template


class JsAlertsLocators:
    JS_BTN_ONCLICK = Template('//*[@id="content"]//button[@onclick="$name"]')
    JS_ALERT_BTN = (By.XPATH, JS_BTN_ONCLICK.substitute(name='jsAlert()'))
    JS_CONFIRM_BTN = (By.XPATH, JS_BTN_ONCLICK.substitute(name='jsConfirm()'))
    JS_PROMPT_BTN = (By.XPATH, JS_BTN_ONCLICK.substitute(name='jsPrompt()'))
    JS_RESULT = (By.XPATH, '//*[@id="result"]')


class JsAlertsMainPage(BasePage):
    def click_alert_button(self):
        Button(JsAlertsLocators.JS_ALERT_BTN, self.driver).click()

    def click_confirm_button(self):
        Button(JsAlertsLocators.JS_CONFIRM_BTN, self.driver).click()

    def click_prompt_button(self):
        Button(JsAlertsLocators.JS_PROMPT_BTN, self.driver).click()

    def get_alert_text(self):
        return self.get_alert_msg()



    def accept_alert_window(self):
        self.accept_alert()

    def fill_string_field(self):
        alert = self.switch_to_alert()
        random_str = generate_string()
        alert.send_keys(random_str)
        return random_str

    def get_results(self):
        return self.find_element(JsAlertsLocators.JS_RESULT).text

