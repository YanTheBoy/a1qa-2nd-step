from framework.base.default_page import BasePage
from selenium.webdriver.common.by import By
from .element import Button, BaseElement, DriverElement
from framework.utils.assistance import get_test_data, get_current_date
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
    FLIGHT_FROM = (By.ID, 'origin')
    FLIGHT_TO = (By.ID, 'destination')
    DEPARTURE_DATE = (By.XPATH, f'//input[@placeholder="{departure}"]/..')
    CALENDAR_DAY = (By.XPATH, '//div[@aria-disabled="false"]')
    DAY_FOR_SELECT = (Template('//div[@aria-label="$date"]'))
    RETURN_TICKET = (By.XPATH, f'//span[contains(text(), "{return_ticket}")]')
    SHOW_HOTELS = (By.XPATH, '//*[@id="clicktripz"]/..')
    FIND_FLIGHTS = (By.CLASS_NAME, 'form-submit__plane')


class AviasalesMainPage(BasePage):
    def set_flight_from(self, departure_from):
        flight_from = BaseElement(AviasalesMainPageLocators.FLIGHT_FROM, self.driver)
        flight_from.send_keys(Keys.CONTROL + 'a')
        flight_from.send_keys(Keys.DELETE)
        flight_from.send_keys(departure_from)

    def set_flight_destination(self, departure_to):
        flight_to = BaseElement(AviasalesMainPageLocators.FLIGHT_TO, self.driver)
        flight_to.clear_field()
        flight_to.send_keys(departure_to)

    def get_available_days(self):
        Button(AviasalesMainPageLocators.DEPARTURE_DATE, self.driver).click()

    def find_available_flight_days(self):
        return BaseElement(AviasalesMainPageLocators.CALENDAR_DAY, self.driver).find_elements()

    def get_day_date(self, day):
        return DriverElement.get_element_attribute(day, 'aria-label')

    def choose_random_day(self, day):
        Button((By.XPATH, AviasalesMainPageLocators.DAY_FOR_SELECT.substitute(date=day)), self.driver).click()

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
        return BaseElement(AllAvailableFlightsLocators.LUGGAGE_AVAILABLE, self.driver).find_elements()

    def find_all_flights_on_page(self):
        return BaseElement(AllAvailableFlightsLocators.FLIGHTS, self.driver).find_elements()

    def find_only_with_luggage(self):
        Button(AllAvailableFlightsLocators.LUGGAGE_FILTER, self.driver).click()

    def find_straight_flights(self):
        Button(AllAvailableFlightsLocators.STRAIGHT_FLIGHT, self.driver).click()

    def get_lowest_price_for_straight_flight(self):
        return BaseElement(AllAvailableFlightsLocators.LOWEST_STRAIGHT_FLIGHT, self.driver).get_text()

    def wait_for_price(self):
        BaseElement(AllAvailableFlightsLocators.PRICE_TABLE, self.driver).find_element(time=tickets_loading)

    def find_lowest_price(self):
        return BaseElement(AllAvailableFlightsLocators.LOWEST_PRICE, self.driver).get_text()

    def get_first_price(self):
        first_price = BaseElement(AllAvailableFlightsLocators.BUY_BUTTON, self.driver).find_elements()[0]
        return DriverElement.get_element_text(first_price)

    def get_last_price(self):
        last_price = BaseElement(AllAvailableFlightsLocators.BUY_BUTTON, self.driver).find_elements()[-1]
        return DriverElement.get_element_text(last_price)

    def get_destination_name(self):
        return BaseElement(AllAvailableFlightsLocators.FLIGHT_TO, self.driver).get_attribute('value')

    def get_departure_name(self):
        return BaseElement(AllAvailableFlightsLocators.FLIGHT_FROM, self.driver).get_attribute('value')
