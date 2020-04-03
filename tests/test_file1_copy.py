import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.basefile import BaseClass


class TestPurchaseItems(BaseClass): # inheriting Base class for availing conftest.py file feature

    def test_purchaseItems(self):


        self.driver.find_element_by_xpath("//a[text()='Shop']").click()
        products_name = self.driver.find_elements_by_xpath("//app-card-list[@class='row']/app-card/div//div[@class='card-body']//a")
        button_xpath = "//app-card-list[@class='row']/app-card/div//div[@class='card-body']//a/ancestor::div[@class='card h-100']//div/button"
        for product in products_name:
            product_text = product.text
            if product_text == "Blackberry":
                self.driver.find_element_by_xpath(button_xpath).click()
        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        wait = WebDriverWait(self.driver,7)
        wait.until(EC.presence_of_element_located,((By.LINK_TEXT,"India")))
        time.sleep(7)
        self.driver.find_element_by_xpath("//a[text()='India']").click()
        #driver.find_element_by_id("checkbox2").click()
        self.driver.find_element_by_xpath("//input[@value='Purchase']").click()
        print(self.driver.find_element_by_class_name("alert-success").text)
        self.driver.close()

