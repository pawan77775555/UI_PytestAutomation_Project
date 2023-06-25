from selenium.webdriver.common.by import By
from Base.BaseClass import BaseClass
from PageObjects.oyo_Search_Result_Page import AvailableHotelsPage
from Utilities.utils import Utilities
import inspect


class HomePage(BaseClass):
    """ Define all the locators """

    SELECT_CITY_TEXT = (By.ID, "autoComplete__home")
    SELECT_CITY_DRP_DOWN = (By.XPATH, '//div[@class="geoSuggestionsList__locationText u-textEllipsis"]/span')
    SELECT_AREA = (By.XPATH, "//span[text()='Hinjewadi']")
    SELECT_DATE_PICKER = (By.XPATH, "//span[@class='datePickerDesktop__checkInOutText'][1]")
    SELECT_FROM_DATE = (By.XPATH, "//div[@class='DateRangePicker__Month'][1]//child::td[contains(@class,'--is-selected') or @class='DateRangePicker__Date']")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")

    """ Driver initialize"""

    def __init__(self, driver):
        super().__init__(driver)

    log = Utilities.custom_logger(None)

    def validate_title(self, title):
        self.take_screenshot()
        return self.title_of_page(title)

    def select_hotel_city(self, hotel_city, area):
        self.do_click(self.SELECT_CITY_TEXT)
        self.text_value(self.SELECT_CITY_TEXT, hotel_city)
        areas_list = self.find_all_elements(self.SELECT_CITY_DRP_DOWN)
        self.take_screenshot()
        return self.utility.select_drp_down_contain(areas_list, area)

    def select_date_from_and_to(self, from_date, to_date):
        self.do_click(self.SELECT_DATE_PICKER)
        all_dates = self.find_all_elements(self.SELECT_FROM_DATE)
        self.take_screenshot()
        return self.utility.select_date_from_to(all_dates, from_date, to_date)

    def search_hotel(self):
        self.do_click(self.SEARCH_BUTTON)
        search_result = AvailableHotelsPage(self.driver)
        self.take_screenshot()
        return search_result

    def AllHomePageMethods(self,title, hotel_city, area, from_date, to_date):
        self.log.info(self.validate_title(title))
        self.select_hotel_city(hotel_city, area)
        self.select_date_from_and_to(from_date, to_date)
        return self.search_hotel()

