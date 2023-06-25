import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from Utilities.utils import Utilities

"""Base Class of all the PageObject classes"""
""" Consist of all the re-usable methods"""


class BaseClass:
    """ Driver initialize"""

    def __init__(self, driver):
        self.driver = driver

    utility = Utilities()

    """ Defined Explicit wait"""

    def explicit_wait(self):
        explicit_wait = WebDriverWait(self.driver, 10, poll_frequency=2)
        return explicit_wait

    def short_explicit_wait(self):
        explicit_wait = WebDriverWait(self.driver, 5, poll_frequency=2)
        return explicit_wait

    """ Defined Mouse Action Object"""

    def mouse_actions(self):
        mouse_action = ActionChains(self.driver)
        return mouse_action

    """ Take the title of page and compare"""

    def title_of_page(self, given_title):
        self.explicit_wait().until(EC.title_is(given_title))
        title_of_current_page = self.driver.title
        assert given_title == title_of_current_page, 'WebPage Title Mis-Match'
        return title_of_current_page

    def title_of_page_contain(self, given_title):
        title_of_current_page = self.driver.title
        assert not given_title in title_of_current_page, 'WebPage Title Mis-Match'
        return title_of_current_page

    """ click the web element """

    def do_click(self, locator):
        web_element = self.explicit_wait().until(EC.presence_of_element_located(locator))
        web_element.click()

    """ send text to web element """

    def text_value(self, locator, text):
        web_element = self.explicit_wait().until(EC.presence_of_element_located(locator))
        web_element.send_keys(text)

    """ Select drop down value """

    def select_dropdown(self, method_type, value_type, locator):
        web_element = self.explicit_wait().until(EC.presence_of_element_located(locator))
        drp_down = Select(web_element)
        if method_type == 'value':
            drp_down.select_by_value(value_type)
        if method_type == 'text':
            drp_down.select_by_visible_text(value_type)
        if method_type == 'index':
            drp_down.select_by_index(value_type)

    """ Return List of all elements """

    def find_all_elements(self, locator):
        elements_list = self.explicit_wait().until(EC.presence_of_all_elements_located(locator))
        return elements_list

    def find_element_on_page(self, locator):
        web_element = self.explicit_wait().until(EC.presence_of_element_located(locator))
        return web_element

    """ Select left slider"""

    def select_left_slider(self, locator, target):
        min_slider = self.explicit_wait().until(EC.presence_of_element_located(locator))
        self.drag_and_drop(min_slider, target)

    """ Drag and Drop the element by axis"""

    def drag_and_drop(self, current_location, target):
        self.mouse_actions().drag_and_drop_by_offset(current_location, target, 0).perform()

    """ Switch to new window"""

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    """ Scroll Down for booking"""

    def scroll_down_page_for_booking(self):
        self.driver.execute_script("window.scrollBy(0,1500);")

    """ Take Screenshot """

    def take_screenshot(self):
        self.driver.get_screenshot_as_file(
            r"C:\UI_PytestAutomation_Project\Selenium_Pytest_HybridFramework(POM)_Project\Screenshots\test.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
