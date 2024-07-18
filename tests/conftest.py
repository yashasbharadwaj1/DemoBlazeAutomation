import pytest
from selenium import webdriver

from TestData.HomePageData import HomePageData

driver = None
Url = "https://www.demoblaze.com/index.html"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.get(Url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(params=HomePageData.positive_login_data)
def getLoginData(request):
    return request.param
