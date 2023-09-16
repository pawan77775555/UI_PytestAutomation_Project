from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest

driver = None

""" Launching the Browser and Navigating to URL """


@pytest.fixture(autouse=True)
def setup(request):
    global driver
    browser = request.config.getoption('browser')
    headless = request.config.getoption('headless')
    if browser == 'chrome':
        driver = chrome_driver_setup(headless)
    elif browser == 'edge':
        driver = edge_driver_setup(headless)
    driver.get('https://www.oyorooms.com/')
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()


""" Setting up chrome browser """


def chrome_driver_setup(Headless):
    BrowserSetting = webdriver.ChromeOptions()
    BrowserSetting.add_argument('--start-maximized')
    BrowserSetting.add_argument('--disable-notifications')
    BrowserSetting.add_argument('--ignore-certificate-errors')
    if Headless == 'true':
        BrowserSetting.add_argument('--headless')
        #Webdriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=BrowserSetting)
        Webdriver = webdriver.Chrome(executable_path="UI_PytestAutomation_Project/Drivers/chromedriver.exe")
    else:
        #Webdriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=BrowserSetting)
        Webdriver = webdriver.Chrome(executable_path="UI_PytestAutomation_Project/Drivers/chromedriver.exe")
    return Webdriver


""" Setting up edge browser """


def edge_driver_setup(Headless):
    BrowserSetting = webdriver.EdgeOptions()
    BrowserSetting.add_argument('--start-maximized')
    BrowserSetting.add_argument('--disable-notifications')
    BrowserSetting.add_argument('--ignore-certificate-errors')
    BrowserSetting.add_argument('--remote-allow-origins=*')
    if Headless == 'true':
        BrowserSetting.add_argument('--headless')
        Webdriver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=BrowserSetting)
    else:
        Webdriver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=BrowserSetting)
    return Webdriver


""" Adding pytest command line arguments """


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--headless', action='store', default='false')
<<<<<<< HEAD

=======
>>>>>>> 56cbcdf465131b744be1dc28ed483f21e26a7884
