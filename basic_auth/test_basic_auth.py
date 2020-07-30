from default_page import BasePage
from logger import appLogger
import requests
from assistance import get_config_data, get_test_data

config_data = get_config_data()
test_data = get_test_data()


def test_basic_auth_page(browser):
    appLogger.debug('Opening browser')
    basic_auth_page = BasePage(browser)
    appLogger.debug('Open https://httpbin.org/basic-auth/user/passwd')
    basic_auth_page.go_to_site(
        config_data['basic_auth_page'].replace(
            'https://', f'https://{test_data["login"]}:{test_data["password"]}@'))
    response = requests.get(browser.current_url).json()

    appLogger.debug('Assert successful authentication')
    assert response['authenticated']
    appLogger.debug('Assert correct user login')
    assert test_data['login'] in response['user']
