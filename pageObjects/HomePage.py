import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from utilities.Common import BaseClass


class HomePage(BaseClass):
    signupLink = (By.LINK_TEXT, "Sign up")
    signupUserName = (By.XPATH, "//input[@id='sign-username']")
    signupPassword = (By.CSS_SELECTOR, "#sign-password")
    signupButton = (By.CSS_SELECTOR, "button[onclick='register()']")

    loginLink = (By.LINK_TEXT, "Log in")
    loginUserName = (By.CSS_SELECTOR, "#loginusername")
    loginPassword = (By.CSS_SELECTOR, "#loginpassword")
    loginButton = (By.CSS_SELECTOR, "button[onclick='logIn()']")

    logoutLink = (By.CSS_SELECTOR, "#logout2")

    phonesCategoryLink = (By.LINK_TEXT, "Phones")
    laptopsCategoryLink = (By.LINK_TEXT, "Laptops")
    monitorsCategoryLink = (By.LINK_TEXT, "Monitors")

    nextButton = (By.CSS_SELECTOR, "#next2")
    lastproductLink = (By.LINK_TEXT, "MacBook Pro")
    lastproductName = (By.CSS_SELECTOR, ".name")
    lastproductPrice = (By.CSS_SELECTOR, ".price-container")
    addToCartButton = (By.LINK_TEXT, "Add to cart")

    def __init__(self, driver):
        self.driver = driver

    def submitSignupForm(self, SignupData):
        self.driver.find_element(*HomePage.signupLink).click()
        self.driver.find_element(*HomePage.signupUserName).send_keys(SignupData["userName"])
        self.driver.find_element(*HomePage.signupPassword).send_keys(SignupData["password"])
        self.driver.find_element(*HomePage.signupButton).click()
        actualSignupFailureAlertText = self.returnAlertText()
        return actualSignupFailureAlertText

    def performLogin(self, LoginData):
        self.driver.find_element(*HomePage.loginLink).click()
        self.driver.find_element(*HomePage.loginUserName).send_keys(LoginData["userName"])
        time.sleep(1)
        self.driver.find_element(*HomePage.loginPassword).send_keys(LoginData["password"])
        self.driver.find_element(*HomePage.loginButton).click()

    def submitLoginFormPositiveCase(self, LoginData):
        self.performLogin(LoginData)
        userName = LoginData["userName"]
        welcomeTextAfterLogin = f"Welcome {userName}"
        self.verifyLinkPresence(welcomeTextAfterLogin)
        actualWelcomeTextAfterLogin = self.driver.find_element(By.LINK_TEXT, welcomeTextAfterLogin).text
        return actualWelcomeTextAfterLogin

    def submitLoginFormNegativeCase(self, LoginData):
        self.verifyLinkPresence("Log in")
        self.performLogin(LoginData)
        actualLoginAlertText = self.returnAlertText()
        return actualLoginAlertText

    def performLogout(self):
        self.driver.find_element(*HomePage.logoutLink).click()

    def confirmLogoutHappened(self, LoginData):
        self.submitLoginFormPositiveCase(LoginData)
        self.performLogout()
        loginText = self.driver.find_element(*HomePage.loginLink).text
        return loginText

    def performProductBrowsingCategoryWise(self, productsData, log):
        category = productsData["category"]
        products = productsData["products"]
        actualProducts = {}
        if category == "phones":
            self.driver.find_element(*HomePage.phonesCategoryLink).click()
            _list = self.verifyActualProductsPresenceAndPopulate(products, log)
            actualProducts["category"] = "phones"
            actualProducts["products"] = _list
        elif category == "laptops":
            self.driver.find_element(*HomePage.laptopsCategoryLink).click()
            _list = self.verifyActualProductsPresenceAndPopulate(products, log)
            actualProducts["category"] = "laptops"
            actualProducts["products"] = _list
        elif category == "monitors":
            self.driver.find_element(*HomePage.monitorsCategoryLink).click()
            _list = self.verifyActualProductsPresenceAndPopulate(products, log)
            actualProducts["category"] = "monitors"
            actualProducts["products"] = _list
        return actualProducts

    def verifyActualProductsPresenceAndPopulate(self, products, log):
        li = []
        for product in products:
            try:
                actualProduct = self.driver.find_element(By.LINK_TEXT, product)
                li.append(actualProduct.text)
            except NoSuchElementException:
                log.error(f"Product link text '{product}' not found.")
                li.append(None)
        return li

    def performAddToCart(self):
        self.driver.find_element(*HomePage.nextButton).click()
        self.verifyLinkPresence("MacBook Pro")
        self.driver.find_element(*HomePage.lastproductLink).click()
        productName = self.driver.find_element(*HomePage.lastproductPrice).text
        productPrice = self.driver.find_element(*HomePage.lastproductPrice).text
        self.driver.find_element(*HomePage.addToCartButton).click()
        return productName, productPrice

    def confirmAddToCart(self):
        self.performAddToCart()
        actualAlertText = self.returnAlertText()
        return actualAlertText
