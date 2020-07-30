from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def log_in(login, password, driver):
    driver.get("https://web.simple-mmo.com/")
    element = driver.find_element_by_name('email')
    element.send_keys(login)
    element = driver.find_element_by_name('password')
    element.send_keys(password)
    element.submit()