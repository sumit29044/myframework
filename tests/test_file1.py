import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.basefile import BaseClass
from pages.home import HomePage
class TestPurchaseItems(BaseClass): # inheriting Base class for availing conftest.py file feature

    def test_purchaseItems(self):
        log = self.getLogger()

        # Ist Page
        homepage = HomePage(self.driver)
        log.info("Clicking shop link")
        print("Hello")
        shoppage = homepage.get_shop_link()

        # 2nd Page
        products_name = shoppage.get_items()
        for product in products_name:
            product_text = product.text
            log.info("Products are",product_text)
            if product_text == "Blackberry":
                shoppage.get_button().click()
        shoppage.get_button_select().click()
        confirmpage = shoppage.get_button_cart()

        # 3rd Page
        confirmpage.get_country_name().send_keys("ind")
        log.info("Waiting for india to be present")
        self.verifyLinkPresence("India")
        time.sleep(7)
        confirmpage.get_country_click().click()
        confirmpage.get_purchase_button().click()
        text_value = (confirmpage.get_text_value().text)
        log.info(text_value)
        assert ("sumit" in text_value)


