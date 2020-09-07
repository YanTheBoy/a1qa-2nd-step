import pytest
from framework.browser.browser_factory import Browser
from framework.logger import appLogger
from framework.utils.assistance import get_config_data


config_data = get_config_data()


@pytest.fixture(params=[config_data["browser"]])
def browser(request):
    appLogger.debug('Set-up')
    driver = Browser.factory(request.param)

    appLogger.debug('Maximize browser window')
    driver.maximize_window()

    yield driver

    appLogger.debug('Tear-down')
    driver.quit()

