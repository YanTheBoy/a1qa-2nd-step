from pages import ExamplePage
from logger import appLogger
from assistance import get_config_data, get_asserts_data, get_test_data


config_data = get_config_data()
asserts_data = get_asserts_data()
test_data = get_test_data()


def test_sending_cookie(browser):
    appLogger.debug('Opening browser')
    example_page = ExamplePage(browser)
    appLogger.debug('Open', config_data['url'])
    example_page.go_to_site(config_data['url'])
    appLogger.debug('Assert right page was opened')
    assert example_page.get_h1_text() in asserts_data['header'], 'Incorrect site was opened.'

    appLogger.debug('Add all cookies')
    for name, value in test_data['cookies'].items():
        example_page.add_cookies({name: value})
    appLogger.debug('Assert cookies was successfully added')
    for name, _ in test_data['cookies'].items():
        assert example_page.get_cookie(name) is not None, 'Cookie was not add to site'

    appLogger.debug('Delete cookie')
    example_page.delete_cookie(test_data['del_cookie'])
    appLogger.debug('Assert cookie was deleted.')
    assert example_page.get_cookie(test_data['del_cookie']) is None, 'Cookie was not delete'

    appLogger.debug('Update cookie value')
    example_page.add_cookies(
        {test_data['update_cookie']: test_data['new_value']})
    appLogger.debug('Assert cookie was updated')
    assert (example_page.get_cookie(test_data['update_cookie']))['value'] == test_data['new_value']

    appLogger.debug('Delete all cookies')
    example_page.delete_cookies()
    appLogger.debug('Assert empty list of cookies')
    assert len(example_page.get_cookies()) == 0, 'Cookies were not deleted'
