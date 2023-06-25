from selenium.webdriver.common.by import By
from Base.BaseClass import BaseClass
from PageObjects.oyo_Hotel_Booking import HotelBooking
from Utilities.utils import Utilities


class AvailableHotelsPage(BaseClass):
    """ Define all the locators """

    LEFT_SLIDER_SOURCE = (By.XPATH, "//*[@class='input-range__slider-container'][1]/div[1]")
    SORT_DRP_DOWN = (By.CLASS_NAME, "dropdown__select")
    SORT_DRP_DOWN_VALUES = (By.XPATH, '//li[@class="dropdown__item"]')
    SELECT_COLLECTION = (By.XPATH, "//div[text()='OYOs welcomes couples']")
    VIEW_DETAILS_BUTTON = (By.XPATH, "(//span[text()='View Details'])[1]")

    log = Utilities.custom_logger(None)

    """ Driver initialize"""

    def __init__(self, driver):
        super().__init__(driver)

    def validate_title_of_page(self, title):
        self.take_screenshot()
        return self.title_of_page_contain(title)

    def select_price_bandwidth(self, target):
        self.take_screenshot()
        return self.select_left_slider(self.LEFT_SLIDER_SOURCE, target)

    def select_filter(self, filter_option):
        self.take_screenshot()
        self.do_click(self.SORT_DRP_DOWN)
        filter_values = self.find_all_elements(self.SORT_DRP_DOWN_VALUES)
        return self.utility.select_drp_down_contain(filter_values, filter_option)

    def select_collections(self):
        self.take_screenshot()
        return self.do_click(self.SELECT_COLLECTION)

    def select_hotel(self):
        self.take_screenshot()
        self.do_click(self.VIEW_DETAILS_BUTTON)
        self.switch_to_new_window()
        hotel_booking = HotelBooking(self.driver)
        return hotel_booking

    def All_Search_Result_Page(self, title, target, filter_option):
        self.log.info(self.validate_title_of_page(title))
        self.select_price_bandwidth(target)
        self.select_filter(filter_option)
        self.select_collections()
        return self.select_hotel()
