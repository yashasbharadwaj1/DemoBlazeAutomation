from pageObjects.HomePage import HomePage
from utilities.Common import BaseClass


class TestAddToCart(BaseClass):
    def test_addToCart(self):
        expectedAddedToCartConfirmationAlertText = "Product added"
        homePage = HomePage(self.driver)
        actualAddedToCartConfirmationAlertText = homePage.confirmAddToCart()
        assert actualAddedToCartConfirmationAlertText == expectedAddedToCartConfirmationAlertText
