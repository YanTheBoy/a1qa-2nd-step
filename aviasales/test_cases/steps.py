import pytest
from framework.pageobject.pages import AviasalesMainPage, AllAvailableFlights
from framework.logger import appLogger
from framework.utils.assistance import get_config_data, get_test_data, get_random_number

config_data = get_config_data()
test_data = get_test_data()


@pytest.mark.parametrize("flight_from,flight_to",
                         [(test_data['test_case_2']['minsk'], test_data['test_case_2']['istanbul']),
                          (test_data['test_case_2']['istanbul'], test_data['test_case_2']['tunis'])
                          ])
def search_flight_tickets(browser, flight_from, flight_to):
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
    available_days = aviasales_page.find_available_flight_days()
    day_to_flight = available_days[get_random_number(len(available_days))]
    appLogger.debug('Choose random day to flight')
    aviasales_page.choose_random_day(aviasales_page.get_day_date(day_to_flight))
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
    assert all_flights.get_destination_name() in flight_to, 'Wrong destination selected'


if __name__ == '__main__':
    pass
