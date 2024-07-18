import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.Common import BaseClass


class TestSignup(BaseClass):

    def test_signup(self, getSignupData):
        homePage = HomePage(self.driver)
        homePage.submitSignupForm(getSignupData)

    @pytest.fixture(params=HomePageData.signup_data)
    def getSignupData(self, request):
        return request.param
