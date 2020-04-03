import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("C:/Personal/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//a[text()='Shop']").click()
driver.find_element_by_xpath("//div[@class='col-lg-9']/app-card-list/app-card[4]"
                             "/div[1]/div[2]/button").click()
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver,7)
wait.until(EC.presence_of_element_located,((By.LINK_TEXT,"India")))
time.sleep(7)
driver.find_element_by_xpath("//a[text()='India']").click()
#driver.find_element_by_id("checkbox2").click()
driver.find_element_by_xpath("//input[@value='Purchase']").click()
print(driver.find_element_by_class_name("alert-success").text)