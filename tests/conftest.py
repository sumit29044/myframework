import pytest
from selenium import webdriver
driver = None


#
def pytest_addoption(parser): # hook
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )


# command line options for selecting browser at runtime
@pytest.fixture(scope="class")
def setUp(request):
    global driver
    browser_name = request.config.getoption("--browser_name") #retriving browser name
    if browser_name == "chrome":
        driver = webdriver.Chrome("C:/Personal/chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox("C:/Personal/geckodriver.exe")
    elif browser_name == "IE":
        print("IE invoking")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver # making local variable (driver) class variable
    yield  # teardown
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

'''  
# setup with out command line options  
@pytest.fixture(scope="class")
def setUp(request):
    driver = webdriver.Chrome("C:/Personal/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver # making local variable (driver) class variable
    yield  # teardown
    driver.close()
'''

