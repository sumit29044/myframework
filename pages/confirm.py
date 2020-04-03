from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    # defining locators
    country_name = (By.ID,"country")
    country_click = (By.XPATH,"//a[text()='India']")
    purchase_button = (By.XPATH,"//input[@value='Purchase']")
    text_value = (By.CLASS_NAME,"alert-success")

    # exposing webelement with the help of locator
    def get_country_name(self):
        return self.driver.find_element(*self.country_name)

    def get_country_click(self):
        return self.driver.find_element(*self.country_click)

    def get_purchase_button(self):
        return self.driver.find_element(*self.purchase_button)

    def get_text_value(self):
        return self.driver.find_element(*self.text_value)



