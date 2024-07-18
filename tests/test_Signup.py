import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.Common import BaseClass


class TestSignup(BaseClass):

    def test_signup(self, getSignupData):
        expectedSignupFailureText = "This user already exist."
        homePage = HomePage(self.driver)
        actualSignupFailureAlertText = homePage.submitSignupForm(getSignupData)
        assert actualSignupFailureAlertText == expectedSignupFailureText

    @pytest.fixture(params=HomePageData.signup_data)
    def getSignupData(self, request):
        return request.param
