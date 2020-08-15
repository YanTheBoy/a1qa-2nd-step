import pytest
from .steps import search_flight_tickets
from framework.pageobject.pages import AllAvailableFlights
from framework.logger import appLogger
from framework.utils.assistance import get_config_data, get_test_data


config_data = get_config_data()
test_data = get_test_data()


@pytest.mark.parametrize("flight_from,flight_to",
                         [(test_data['test_case_1']['minsk'], test_data['test_case_1']['istanbul']),
                          (test_data['test_case_1']['istanbul'], test_data['test_case_1']['minsk'])
                          ])
def test_from_minsk_to_istanbul(browser, flight_from, flight_to):
    search_flight_tickets(browser, flight_from, flight_to)
    all_flights = AllAvailableFlights(browser)

    appLogger.debug('Assert the lowest price on first place in tickets list')
    assert all_flights.find_lowest_price() == all_flights.get_first_price(),\
        'Price is not on first place in list'
