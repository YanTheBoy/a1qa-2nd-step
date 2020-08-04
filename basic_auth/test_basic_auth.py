from default_page import BasePage
from logger import appLogger
import requests
from assistance import get_config_data, get_test_data

config_data = get_config_data()
test_data = get_test_data()


def test_basic_auth_page(browser):
    appLogger.debug('Opening browser')
    basic_auth_page = BasePage(browser)
    appLogger.debug('Open ', config_data['basic_auth_page'])
    basic_auth_page.complete_basic_auth(
        config_data['basic_auth_page'],
        test_data['login'],
        test_data['password'])

    response = requests.get(browser.current_url).json()

    appLogger.debug('Assert successful authentication')
    assert response['authenticated'], 'Authentication failed'
    appLogger.debug('Assert correct user login')
    assert test_data['login'] in response['user'], 'Wrong user logged in'
