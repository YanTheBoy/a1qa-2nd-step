from default_page import BasePage
from selenium.webdriver.common.by import By
from element import Button
from assistance import get_test_data, get_current_date, get_random_number
from selenium.webdriver.common.keys import Keys
from string import Template


test_data = get_test_data()

buy_btn = test_data['but_btn']
more_prices = test_data['more_prices']
departure = test_data['departure_btn']
today = get_current_date()
return_ticket = test_data['return_ticket']
lowest_price = test_data['lowest_price']
straight_flight = test_data['straight_flight']
luggage = test_data['luggage']
with_luggage = test_data['with_luggage']
tickets_loading = 40


class AviasalesMainPageLocators:
    FLIGHT_FROM = (By.XPATH, '//*[@id="origin"]')
    FLIGHT_TO = (By.XPATH, '//*[@id="destination"]')
    DEPARTURE_DATE = (By.XPATH, f'//input[@placeholder="{departure}"]/..')
    CALENDAR_DAY = (By.XPATH, '//div[@aria-disabled="false"]')
    DAY_FOR_SELECT = (Template('//div[@aria-label="$date"]'))
    RETURN_TICKET = (By.XPATH, f'//span[contains(text(), "{return_ticket}")]')
    SHOW_HOTELS = (By.XPATH, '//*[@id="clicktripz"]/..')
    FIND_FLIGHTS = (By.CLASS_NAME, 'form-submit__plane')


class AviasalesMainPage(BasePage):
    def set_flight_from(self, departure_from):
        flight_from = self.find_element(AviasalesMainPageLocators.FLIGHT_FROM)
        flight_from.send_keys(Keys.CONTROL + "a")
        flight_from.send_keys(Keys.DELETE)
        flight_from.send_keys(departure_from)

    def set_flight_destination(self, departure_to):
        flight_to = self.find_element(AviasalesMainPageLocators.FLIGHT_TO)
        flight_to.clear()
        flight_to.send_keys(departure_to)

    def get_available_days(self):
        Button(AviasalesMainPageLocators.DEPARTURE_DATE, self.driver).click()

    def choose_random_day(self):
        available_days = self.find_elements(AviasalesMainPageLocators.CALENDAR_DAY)
        random_day = available_days[get_random_number(len(available_days))]
        rnd_day_name = random_day.get_attribute('aria-label')
        Button((By.XPATH, AviasalesMainPageLocators.DAY_FOR_SELECT.substitute(date=rnd_day_name)), self.driver).click()

    def set_of_return_tickets(self):
        Button(AviasalesMainPageLocators.RETURN_TICKET, self.driver).click()

    def dismiss_hotel_show(self):
        Button(AviasalesMainPageLocators.SHOW_HOTELS, self.driver).click()

    def find_flights(self):
        Button(AviasalesMainPageLocators.FIND_FLIGHTS, self.driver).click()


class AllAvailableFlightsLocators(AviasalesMainPageLocators):
    PRICE_TABLE = (By.XPATH, f'//*[normalize-space() = "{more_prices}"]')
    LOWEST_PRICE = (By.XPATH, f'//span[contains(text(), "{lowest_price}")]/following-sibling::span')
    BUY_BUTTON = (By.XPATH, f'//*[contains(text(), "{buy_btn}")]/..//span[@data-testid="price-with-logic"]')
    STRAIGHT_FLIGHT = (By.XPATH, f'//span[contains(text(), "{straight_flight}")]')
    LOWEST_STRAIGHT_FLIGHT = (By.XPATH, f'//span[contains(text(), "{straight_flight}")]/following-sibling::span')
    LUGGAGE_FILTER = (By.XPATH, f'//button[contains(text(), "{luggage}")]')
    FLIGHTS = (By.CLASS_NAME, 'ticket-desktop')
    LUGGAGE_AVAILABLE = (By.XPATH, f'//div[contains(text(), "{with_luggage}")]')


class AllAvailableFlights(BasePage):
    def find_all_luggage_icons(self):
        return self.find_elements(AllAvailableFlightsLocators.LUGGAGE_AVAILABLE)

    def find_all_flights_on_page(self):
        return self.find_elements(AllAvailableFlightsLocators.FLIGHTS)

    def find_only_with_luggage(self):
        Button(AllAvailableFlightsLocators.LUGGAGE_FILTER, self.driver).click()

    def find_straight_flights(self):
        Button(AllAvailableFlightsLocators.STRAIGHT_FLIGHT, self.driver).click()

    def get_lowest_price_for_straight_flight(self):
        return self.find_element(AllAvailableFlightsLocators.LOWEST_STRAIGHT_FLIGHT).text

    def wait_for_price(self):
        self.find_element(AllAvailableFlightsLocators.PRICE_TABLE, time=tickets_loading)

    def find_lowest_price(self):
        return self.find_element(AllAvailableFlightsLocators.LOWEST_PRICE).text

    def get_first_price(self):
        return self.find_elements(AllAvailableFlightsLocators.BUY_BUTTON)[0].text

    def get_last_price(self):
        return self.find_elements(AllAvailableFlightsLocators.BUY_BUTTON)[-1].text

    def get_destination_name(self):
        return self.find_element(AviasalesMainPageLocators.FLIGHT_TO).get_attribute('value')

    def get_departure_name(self):
        return self.find_element(AviasalesMainPageLocators.FLIGHT_FROM).get_attribute('value')

