from selenium.webdriver.common.by import By
from .shop import ShopPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver


    # storing locator
    shop_link = (By.XPATH,"//a[text()='Shop']")
    name = (By.XPATH,"//div[@class='form-group']//input[@name='name']")
    email = (By.XPATH,"//div[@class='form-group']//input[@name='email']")
    password = (By.ID,"exampleInputPassword1")
    checkbox = (By.XPATH,"//div[@class='form-check']")
    select_item = (By.ID,"exampleFormControlSelect1")
    radio_button = (By.XPATH,"//label[text()='Student']")
    submit_button = (By.XPATH,"//input[@value='Submit']")



     # getting loactors
    def get_shop_link(self):
         #self.driver.find_element_by_xpath("//a[text()='Shop']")
         self.driver.find_element(*self.shop_link).click()
         shoppage = ShopPage(self.driver)
         return shoppage

    def get_name(self):
        return self.driver.find_element(*self.name)


    def get_email(self):
        return self.driver.find_element(*self.email)


    def get_pwd(self):
        return self.driver.find_element(*self.password)


    def get_checkbox(self):
        return self.driver.find_element(*self.checkbox)

    def get_select_items(self):
        return self.driver.find_element(*self.select_item)

    def get_radio_button(self):
        return self.driver.find_element(*self.radio_button)

    def get_submit_button(self):
        return self.driver.find_element(*self.submit_button)


