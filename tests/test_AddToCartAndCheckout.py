import pytest

from TestData.CartPageData import CartPageData
from pageObjects.HomePage import HomePage
from utilities.Common import BaseClass


class TestAddToCartAndCheckout(BaseClass):

    def test_addToCartAndCheckout(self, getOrderData):
        expectedPurchaseConformationMessage = "Thank you for your purchase!"
        log = self.getLogger()
        homePage = HomePage(self.driver)
        actualPurchaseConfirmationMessage = homePage.performCheckout(log, getOrderData)
        assert actualPurchaseConfirmationMessage == expectedPurchaseConformationMessage

    @pytest.fixture(params=CartPageData.order_data)
    def getOrderData(self, request):
        return request.param


