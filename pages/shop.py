from selenium.webdriver.common.by import By
from .confirm import ConfirmPage
class ShopPage:

    def __init__(self,driver):
        self.driver = driver


    # defining locator
    items = (By.XPATH,"//app-card-list[@class='row']/app-card/div//div[@class='card-body']//a")
    buttons = (By.XPATH,"//app-card-list[@class='row']/app-card/div//div[@class='card-body']//a/ancestor::div[@class='card h-100']//div/button")
    button_select = (By.XPATH,"//a[@class='nav-link btn btn-primary']")
    button_cart = (By.XPATH,"//button[@class='btn btn-success']")


    # exposing webelement from locators
    def get_items(self):
        return self.driver.find_elements(*self.items)

    def get_button(self):
        return self.driver.find_element(*self.buttons)


    def get_button_select(self):
        return self.driver.find_element(*self.button_select)

    def get_button_cart(self):
        self.driver.find_element(*self.button_cart).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

