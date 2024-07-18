import time

from selenium.webdriver.common.by import By

from utilities.Common import BaseClass


class CartPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    tableElements = (By.CSS_SELECTOR, ".table-responsive table tbody tr ")
    titleElement = (By.CSS_SELECTOR, "td:nth-child(2)")
    priceElement = (By.CSS_SELECTOR, "td:nth-child(3)")

    placeOrderButton = (By.CSS_SELECTOR, ".btn.btn-success")
    totalAmount = (By.XPATH, "//label[@id='totalm']")
    expectedTotalOrderAmount = "1100"
    expectedCartItems = [['MacBook Pro', '1100']]

    name = (By.CSS_SELECTOR, "#name")
    country = (By.CSS_SELECTOR, "#country")
    city = (By.CSS_SELECTOR, "#city")
    card = (By.CSS_SELECTOR, "#card")
    month = (By.CSS_SELECTOR, "#month")
    year = (By.CSS_SELECTOR, "#year")
    purchaseButton = (By.CSS_SELECTOR, "button[onclick='purchaseOrder()']")

    purchaseConfirmation = (By.CSS_SELECTOR, "h2:nth-child(6)")
    purchaseConfirmationButton = (By.CSS_SELECTOR, ".confirm.btn.btn-lg.btn-primary")

    cartPageLink = (By.LINK_TEXT, "Cart")

    def getCartItems(self, log):
        allTableElements = self.driver.find_elements(*CartPage.tableElements)
        itemsList = []
        for element in allTableElements:
            title = element.find_element(*CartPage.titleElement).text
            price = element.find_element(*CartPage.priceElement).text
            itemsList.append([title, price])

        actualCartItems = itemsList
        if actualCartItems == self.expectedCartItems:
            log.info("assertion actualCartItems == expectedCartItems passed")
            return True
        else:
            log.info("assertion actualCartItems == expectedCartItems failed")
            return False

    def placeOrder(self, log,orderData):
        self.driver.find_element(*CartPage.placeOrderButton).click()
        time.sleep(2)
        self.driver.find_element(*CartPage.name).send_keys(orderData["name"])
        self.driver.find_element(*CartPage.country).send_keys(orderData["country"])
        self.driver.find_element(*CartPage.city).send_keys(orderData["city"])
        self.driver.find_element(*CartPage.card).send_keys(orderData["card"])
        self.driver.find_element(*CartPage.month).send_keys(orderData["month"])
        self.driver.find_element(*CartPage.year).send_keys(orderData["year"])
        self.driver.find_element(*CartPage.purchaseButton).click()
        time.sleep(1)
        purchaseConfirmation = self.driver.find_element(*CartPage.purchaseConfirmation).text
        self.driver.find_element(*CartPage.purchaseConfirmationButton).click()
        return purchaseConfirmation



