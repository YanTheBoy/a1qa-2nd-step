import pytest
from browser_factory import Browser
from logger import appLogger
from assistance import get_config_data, get_testrail_data
import os.path
from testrail import *
config_data = get_config_data()
testrail = get_testrail_data()

USER_ID = testrail['user_id']
TEST_ID = testrail['test_id']
TR_URL = testrail['url']
TR_LOGIN = testrail['login']
TR_PASS = testrail['pass']
SCREENSHOT = testrail['pic']

@pytest.fixture(params=[config_data["browser"]], scope="session")
def browser(request):
    appLogger.debug('Set-up')
    driver = Browser.factory(request.param)

    appLogger.debug('Maximize browser window')
    driver.maximize_window()

    yield driver
    take_screenshot(driver)

    appLogger.debug('Tear-down')
    driver.quit()


def take_screenshot(browser):
    browser.save_screenshot(SCREENSHOT)

def pytest_sessionstart(session):
    session.results = dict()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call':
        item.session.results[item] = result


def pytest_sessionfinish(session):
    for result in session.results.values():
        if result.passed:
            status_id = 1
            comment = "Test succesfully passed!"
        elif result.failed:
            status_id = 5
            comment = "Attention! Test failed!"
    send_results_to_testrail(status_id, comment)


def send_results_to_testrail(status, comment):
    client = APIClient(TR_URL)
    client.user = TR_LOGIN
    client.password = TR_PASS
    add_res = client.send_post(f'add_result/{TEST_ID}', data={
        "status_id": status,
        "comment": comment,
        "assignedto_id": USER_ID
    })
    TEST_RUN = add_res['id']
    add_att = client.send_post(f'add_attachment_to_result/{TEST_RUN}', SCREENSHOT)