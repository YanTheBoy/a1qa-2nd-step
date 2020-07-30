from pages import JsAlertsMainPage
from logger import appLogger
from assistance import get_config_data, get_asserts_data

config_data = get_config_data()
asserts_data = get_asserts_data()


def test_basic_auth_page(browser):
    appLogger.debug('Opening browser')
    alerts_page = JsAlertsMainPage(browser)
    appLogger.debug('Open http://the-internet.herokuapp.com/javascript_alerts')
    alerts_page.go_to_site(config_data['url'])

    appLogger.debug('Click on alert button')
    alerts_page.click_alert_button()
    appLogger.debug('Assert text in alert')
    assert alerts_page.get_alert_text() in asserts_data['alert']
    appLogger.debug('Accept alert window')
    alerts_page.accept_alert_window()
    appLogger.debug('Assert result after alert closed')
    assert alerts_page.get_results() in asserts_data['alert_result']

    appLogger.debug('Click on confirm button')
    alerts_page.click_confirm_button()
    appLogger.debug('Assert text in confirm')
    assert alerts_page.get_alert_text() in asserts_data['confirm']
    appLogger.debug('Accept confirm window')
    alerts_page.accept_alert_window()
    appLogger.debug('Assert result after alert closed')
    assert alerts_page.get_results() in asserts_data['confirm_result']

    appLogger.debug('Click on prompt button')
    alerts_page.click_prompt_button()
    appLogger.debug('Assert text in prompt')
    assert alerts_page.get_alert_text() in asserts_data['prompt']
    appLogger.debug('Put random string in prompt`s field')
    random_string = alerts_page.fill_string_field()
    appLogger.debug('Accept prompt window')
    alerts_page.accept_alert_window()
    appLogger.debug('Assert result after alert closed')
    assert alerts_page.get_results() in asserts_data['prompt_result']+random_string






