from selenium.webdriver.support.select import Select
import pytest

from utilities.basefile import BaseClass
from pages.home import HomePage
from testdata.homepagedata import HomePageData

class TestForm(BaseClass):

    def test_form(self,loadData):
        homepage = HomePage(self.driver)
        homepage.get_name().send_keys(loadData["name"])
        homepage.get_email().send_keys(loadData["email"])
        homepage.get_pwd().send_keys(loadData["pwd"])
        homepage.get_checkbox().click()
        self.selectItemsByText(homepage.get_select_items(),"Male")
        homepage.get_radio_button().click()
        homepage.get_submit_button().click()
        self.driver.refresh()

    '''
     # sending data using list and tuple combination
    @pytest.fixture(params=[('sumit','sumit@gmail.com','12345'),('amit','amit@gmail.com','13579',('neha','neha@gmail.com',
                                                                                                  '98211'))])
    def loadData(self,request):
        return request.param
    '''
    # implementing data driven concept
    @pytest.fixture(params=HomePageData.testHomePageData)
    def loadData(self,request):
        return request.param
