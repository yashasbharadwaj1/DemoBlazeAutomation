import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.Common import BaseClass


class TestProductBrowsing(BaseClass):

    def test_ProductBrowsingCategoryWise(self, getExpectedProductsData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        actualProducts = homePage.performProductBrowsingCategoryWise(getExpectedProductsData,log)
        assert actualProducts == getExpectedProductsData

    @pytest.fixture(params=HomePageData.expected_products_data)
    def getExpectedProductsData(self, request):
        return request.param
