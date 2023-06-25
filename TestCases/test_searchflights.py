import unittest

import allure
import pytest
from allure_commons.types import AttachmentType

from PageObjects.oyo_HomePage import HomePage
from Base.BaseTestClass import BaseTestClass
from ddt import ddt, data, file_data, unpack
from Utilities.utils import Utilities


@ddt
@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFlights(BaseTestClass, unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.Home_Page = HomePage(self.driver)

    """ Run using data from csv """

    @data(*Utilities.CSVTestData(
        r"C:\Users\PAWAN\Selenium_Pytest_HybridFramework(POM)_Project\TestData\OyoRoomBookAutomation.csv"))
    @unpack
    def test_search_hotel(self, title, city, area, from_date, to_date, sort):
        search_result_page = self.Home_Page.AllHomePageMethods(title, city, area, from_date, to_date)
        HotelBooking = search_result_page.All_Search_Result_Page('Hotels in  Starting', 70, sort)
        HotelBooking.All_methods_of_Hotel_Booking()