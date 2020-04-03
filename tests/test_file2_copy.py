from selenium.webdriver.support.select import Select

from utilities.basefile import BaseClass
from pages.home import HomePage

class TestForm(BaseClass):

    def test_form(self):
        homepage = HomePage(self.driver)
        homepage.get_name().send_keys("Sumit")
        homepage.get_email().send_keys("sumit.shivhare@gmail.com")
        homepage.get_pwd().send_keys("12345")
        homepage.get_checkbox().click()
        self.selectItemsByText(homepage.get_select_items(),"Male")
        homepage.get_radio_button().click()
        homepage.get_submit_button().click()
