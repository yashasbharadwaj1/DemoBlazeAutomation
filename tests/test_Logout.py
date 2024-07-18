import pytest

from pageObjects.HomePage import HomePage
from utilities.Common import BaseClass


@pytest.mark.usefixtures("getLoginData")
class TestLogot(BaseClass):

    def test_logout(self,getLoginData):
        log = self.getLogger()
        # Login in re-appearing after logout confirms logout happened
        expectedLoginText = "Log in"
        homePage = HomePage(self.driver)
        actualLoginText = homePage.confirmLogoutHappened(getLoginData)
        assert actualLoginText == expectedLoginText
