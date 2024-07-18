import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.Common import BaseClass


class TestLogin(BaseClass):

    def test_loginPositiveCase(self, getPositiveLoginData):
        log = self.getLogger()
        userName = getPositiveLoginData["userName"]
        expectedWelcomeTextAfterLogin = f"Welcome {userName}"
        homePage = HomePage(self.driver)
        actualWelcomeTextAfterLogin = homePage.submitLoginFormPositiveCase(getPositiveLoginData)
        log.info(f"LoginFormSubmission Outcome :- {actualWelcomeTextAfterLogin}")
        assert expectedWelcomeTextAfterLogin == actualWelcomeTextAfterLogin
        homePage.performLogout()

    @pytest.fixture(params=HomePageData.positive_login_data)
    def getPositiveLoginData(self, request):
        return request.param

    def test_loginNegativeCase(self,getNegativeLoginData):
        log = self.getLogger()
        expectedLoginFailureAlertTextList = "Wrong password."
        homePage = HomePage(self.driver)
        actualLoginFailureAlertText = homePage.submitLoginFormNegativeCase(getNegativeLoginData)
        log.info(f"actualLoginAlertText :- {actualLoginFailureAlertText}")
        assert actualLoginFailureAlertText == expectedLoginFailureAlertTextList

    @pytest.fixture(params=HomePageData.negative_login_data)
    def getNegativeLoginData(self, request):
        return request.param
