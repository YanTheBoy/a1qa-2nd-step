import pytest
from .steps import search_flight_tickets
from framework.pageobject.pages import AllAvailableFlights
from framework.logger import appLogger
from framework.utils.assistance import get_config_data, get_test_data

config_data = get_config_data()
test_data = get_test_data()


@pytest.mark.parametrize("flight_from,flight_to",
                         [(test_data['test_case_2']['minsk'], test_data['test_case_2']['istanbul']),
                          (test_data['test_case_2']['istanbul'], test_data['test_case_2']['tunis'])
                          ])
def test_from_minsk_to_istanbul(browser, flight_from, flight_to):
    search_flight_tickets(browser, flight_from, flight_to)
    all_flights = AllAvailableFlights(browser)
    appLogger.debug('Click for straight flights')
    all_flights.find_straight_flights()
    appLogger.debug('Finding lowest price for straight flight')
    lowest_price = all_flights.get_lowest_price_for_straight_flight()
    appLogger.debug('Assert cheapest ticket is in the end of list')
    assert all_flights.get_last_price() == lowest_price, 'Prices are not equal'
