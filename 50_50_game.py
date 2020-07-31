from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from random import random

driver = webdriver.Chrome()
driver.get("https://web.simple-mmo.com/")
element = driver.find_element_by_name('email')
element.send_keys(os.environ['EMAIL'])
element = driver.find_element_by_name('password')
element.send_keys(os.environ['PASSWORD'])
element.submit()

driver.get('https://web.simple-mmo.com/gamecentre/5050')

wager = ['125', '250', '500', '1000', '2000', '4000', '8000', '16000', '32000', '64000', '128000']
wager_it = 0

element = driver.find_element_by_name('GoldAmount')
element.send_keys(wager[wager_it])
element.submit()

while True:
    sleep(1)
    element = driver.find_element_by_name('GoldAmount')
    try:
        notify = driver.find_element_by_xpath('//div[@class="notice notice-success"]')
        wager_it = 0
    except Exception:
        wager_it = 0 if wager_it == len(wager) - 1 else wager_it + 1 
    finally:
        sleep(2 * random())
        print(wager[wager_it])
        element.send_keys(wager[wager_it])
        element.submit()
        
