from selenium.webdriver.common.by import By
from Base.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class HotelBooking(BaseClass):
    """ Define all the locators """

    PHOTOS_BUTTON = (By.XPATH, '//button[@class="slick-arrow slick-next"]')
    BOOK_BUTTON = (By.XPATH, "//span[text()='Continue to Book']")

    """ Driver initialize"""

    def __init__(self, driver):
        super().__init__(driver)

    def check_photos(self):
        self.take_screenshot()
        try:
            while True:
                web_element = self.short_explicit_wait().until(EC.element_to_be_clickable(self.PHOTOS_BUTTON))
                web_element.click()

        except:
            pass

    def scroll_down(self):
        self.take_screenshot()
        self.scroll_down_page_for_booking()

    def book_hotel(self):
        self.take_screenshot()
        self.do_click(self.BOOK_BUTTON)

    def All_methods_of_Hotel_Booking(self):
        self.check_photos()
        self.scroll_down()
        self.book_hotel()
