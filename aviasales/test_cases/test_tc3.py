import pytest
from .steps import search_flight_tickets
from framework.pageobject.pages import AllAvailableFlights
from framework.logger import appLogger
from framework.utils.assistance import get_config_data, get_test_data


config_data = get_config_data()
test_data = get_test_data()


@pytest.mark.parametrize("flight_from,flight_to",
                         [(test_data['test_case_3']['minsk'], test_data['test_case_3']['istanbul'])])
def test_from_minsk_to_istanbul(browser, flight_from, flight_to):
    search_flight_tickets(browser, flight_from, flight_to)
    all_flights = AllAvailableFlights(browser)

    appLogger.debug('Mark luggage for filter')
    all_flights.find_only_with_luggage()
    appLogger.debug('Assert all flights with luggage')
    assert len(all_flights.find_all_flights_on_page()) == len(all_flights.find_all_luggage_icons()),\
        'Not all flight with luggage and hand luggage'
