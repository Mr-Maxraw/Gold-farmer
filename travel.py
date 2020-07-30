from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from log_in import log_in
import time
import os
# from dotenv import load_dotenv

# load_dotenv()

# driver = webdriver.Chrome()
# log_in(os.environ['EMAIL'], os.environ['PASSWORD'], driver)

def do_steps(driver):
    driver.get('https://web.simple-mmo.com/travel')

    steps = int(driver.find_element_by_id('current_steps').get_attribute('innerHTML'))
    print(steps)
    for i in range(steps):
        do_step = driver.find_element_by_xpath('//button[@class=" btn  btn-primary stepbuttonnew"]')
        ActionChains(driver).click(do_step).perform()
        time.sleep(15)

# do_steps(driver)
# driver.close()