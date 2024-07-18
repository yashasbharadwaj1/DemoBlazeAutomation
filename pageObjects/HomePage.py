import time
from selenium.webdriver.common.by import By
from utilities.Common import BaseClass


class HomePage(BaseClass):
    signupLink = (By.LINK_TEXT, "Sign up")
    signupUserName = (By.XPATH, "//input[@id='sign-username']")
    signupPassword = (By.CSS_SELECTOR, "#sign-password")
    signupButton = (By.CSS_SELECTOR, "button[onclick='register()']")

    def __init__(self, driver):
        self.driver = driver

    def submitSignupForm(self, SignupData):
        self.driver.find_element(*HomePage.signupLink).click()
        self.driver.find_element(*HomePage.signupUserName).send_keys(SignupData["userName"])
        self.driver.find_element(*HomePage.signupPassword).send_keys(SignupData["password"])
        self.driver.find_element(*HomePage.signupButton).click()

