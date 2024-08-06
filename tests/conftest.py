import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions 
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from TestData.HomePageData import HomePageData

driver = None
Url = "https://www.demoblaze.com/index.html"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
        #driver = webdriver.Chrome()
    elif browser_name == "firefox": 
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_service = FirefoxService("/snap/bin/firefox.geckodriver")
        driver = webdriver.Firefox(service=firefox_service,options=firefox_options)

    elif browser_name == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        driver = webdriver.Edge(options=edge_options)
    else:
        driver = webdriver.Chrome(options=chrome_options)
        #driver = webdriver.Chrome()
    driver.get(Url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(params=HomePageData.positive_login_data)
def getLoginData(request):
    return request.param
