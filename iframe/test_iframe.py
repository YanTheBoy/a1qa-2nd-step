from pages import IframePage
from logger import appLogger
from assistance import get_config_data, get_asserts_data


config_data = get_config_data()
asserts_data = get_asserts_data()


def test_basic_auth_page(browser):
    appLogger.debug('Opening browser')
    iframe_page = IframePage(browser)
    appLogger.debug('Open', config_data['url'])
    iframe_page.go_to_site(config_data['url'])
    appLogger.debug('Assert text in page highlight')
    assert iframe_page.get_highlight_text() in asserts_data['iframe_highlight'], 'Site highlight is not correct'

    appLogger.debug('Switch window to Iframe')
    iframe_page.switch_to_iframe()
    appLogger.debug('Put random text in Iframe field')
    random_string = iframe_page.rewrite_iframe_field()
    appLogger.debug('Assert iframe field is not empty')
    assert iframe_page.get_iframe_text() in random_string, 'Entered string is not equal to iframe field text'

    appLogger.debug('Select all text in field')
    iframe_page.select_all_text()
    appLogger.debug('Switch to default window')
    iframe_page.switch_to_default_page()
    appLogger.debug('Make text bold')
    iframe_page.make_text_bold()
    appLogger.debug('Switch window to Iframe')
    iframe_page.switch_to_iframe()
    appLogger.debug('Assert text made bold')
    assert iframe_page.find_strong_element(), 'Entered string is not bold'

