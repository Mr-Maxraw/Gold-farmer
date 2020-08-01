from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime, localtime
import os
from random import random
from dotenv import load_dotenv
import sys

load_dotenv()

driver = webdriver.Chrome()
driver.get("https://web.simple-mmo.com/")
element = driver.find_element_by_name('email')
element.send_keys(os.environ['EMAIL'])
element = driver.find_element_by_name('password')
element.send_keys(os.environ['PASSWORD'])
element.submit()

driver.get('https://web.simple-mmo.com/gamecentre/5050')

wager = ['225', '450', '900', '1800', '3600', '7200', '14400', '28800', '57600', '115200', '230400']

wager_it = 0

element = driver.find_element_by_name('GoldAmount')
element.send_keys(wager[wager_it])
element.submit()

sys.stdout = open('gold.log', 'a')
print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
print('start gold gen', flush=True)
count = 0

while True:
    #sleep(0.5)
    count += 1
    element = driver.find_element_by_name('GoldAmount')
    try:
        notify = driver.find_element_by_xpath('//div[@class="notice notice-success"]')
        wager_it = 0
    except Exception:
        wager_it = 0 if wager_it == len(wager) - 1 else wager_it + 1
        if wager_it == 0:
            print('loss')
    finally:
        sleep(1 * random() + 0.3)
        print(wager[wager_it], flush=True)
        if wager_it == 0 and count >= 1000:
            driver.close()
            break
        element.send_keys(wager[wager_it])
        element.submit()
        
