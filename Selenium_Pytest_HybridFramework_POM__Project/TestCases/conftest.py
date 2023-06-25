from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
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
    serv_obj = ChromeService(executable_path="Selenium_Pytest_HybridFramework_POM__Project/Drivers/chromedriver.exe")
    if Headless == 'true':
        BrowserSetting.add_argument('--headless')
        Webdriver = webdriver.Chrome(service=serv_obj, options=BrowserSetting)
    else:
        Webdriver = webdriver.Chrome(service=serv_obj, options=BrowserSetting)
    return Webdriver


""" Setting up edge browser """


def edge_driver_setup(Headless):
    BrowserSetting = webdriver.EdgeOptions()
    BrowserSetting.add_argument('--start-maximized')
    BrowserSetting.add_argument('--disable-notifications')
    BrowserSetting.add_argument('--ignore-certificate-errors')
    BrowserSetting.add_argument('--remote-allow-origins=*')
    serv_obj = EdgeService(executable_path="Selenium_Pytest_HybridFramework_POM__Project/Drivers/msedgedriver.exe")
    if Headless == 'true':
        BrowserSetting.add_argument('--headless')
        Webdriver = webdriver.Edge(service=serv_obj, options=BrowserSetting)
    else:
        Webdriver = webdriver.Edge(service=serv_obj, options=BrowserSetting)
    return Webdriver


""" Adding pytest command line arguments """


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--headless', action='store', default='false')


""" Attach Screenshot in Reports """


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def pytest_html_report_title(report):
    report.title = "Automation Report"
