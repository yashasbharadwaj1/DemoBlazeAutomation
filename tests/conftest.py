import pytest
from selenium import webdriver

driver = None
Url = "https://www.demoblaze.com/index.html"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.get(Url)
    driver.maximize_window()
    driver.implicitly_wait(6)
    request.cls.driver = driver
    yield
    driver.close()
