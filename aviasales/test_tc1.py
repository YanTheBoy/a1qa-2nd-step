from pages import AviasalesMainPage, AllAvailableFlights
from logger import appLogger
import pytest
from assistance import get_config_data, get_test_data


config_data = get_config_data()
test_data = get_test_data()


@pytest.mark.parametrize("flight_from,flight_to",
                         [(test_data['test_case_1']['minsk'], test_data['test_case_1']['istanbul']),
                          (test_data['test_case_1']['istanbul'], test_data['test_case_1']['minsk'])
                          ])
def test_from_minsk_to_istanbul(browser, flight_from, flight_to):
    appLogger.debug('Opening browser')
    aviasales_page = AviasalesMainPage(browser)
    appLogger.debug('Open', config_data['url'])
    aviasales_page.go_to_site(config_data['url'])

    appLogger.debug('Setting flight departure from')
    aviasales_page.set_flight_from(flight_from)
    appLogger.debug('Setting flight destination')
    aviasales_page.set_flight_destination(flight_to)
    appLogger.debug('Get available flight dates')
    aviasales_page.get_available_days()
    appLogger.debug('Choose random day to flight')
    aviasales_page.choose_random_day()
    appLogger.debug('Turn off return tickets')
    aviasales_page.set_of_return_tickets()
    appLogger.debug('Turn off hotel searching')
    aviasales_page.dismiss_hotel_show()
    appLogger.debug('Click to find flights')
    aviasales_page.find_flights()

    all_flights = AllAvailableFlights(browser)
    appLogger.debug('Waiting for price loading')
    all_flights.wait_for_price()

    appLogger.debug('Assert departure country')
    assert flight_from in all_flights.get_departure_name(), 'Wrong departure selected'
    appLogger.debug('Assert destination country')
    assert flight_to in all_flights.get_destination_name(), 'Wrong destination selected'
    appLogger.debug('Assert the lowest price on first place in tickets list')
    assert all_flights.find_lowest_price() == all_flights.get_first_price(),\
        'Price is not on first place in list'
