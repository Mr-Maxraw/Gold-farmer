from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from log_in import log_in
import time
import os
import random
# from dotenv import load_dotenv

# load_dotenv()

# driver = webdriver.Chrome()
# log_in(os.environ['EMAIL'], os.environ['PASSWORD'], driver)

def do_steps(driver):
    driver.get('https://web.simple-mmo.com/travel')

    steps = int(driver.find_element_by_id('current_steps').get_attribute('innerHTML'))
    print('we will go for ' + str(steps) + ' steps')
    for i in range(steps):
        container = driver.find_element_by_id("travelBarContainer")
        while container.is_displayed():
            container = driver.find_element_by_id("travelBarContainer")
            time.sleep(0.5 + random.randint(1, 3)/10)
        do_step = driver.find_element_by_id("primaryStepButton")
        ActionChains(driver).click(do_step).perform()
        time.sleep(1)
        try:
            att_btn = driver.find_element_by_xpath('//a[text()[contains(., " Attack")]]')
            time.sleep(1)
            ActionChains(driver).click(att_btn).perform()
            time.sleep(1)
            visibitity = driver.find_element_by_id('success-killed').is_displayed()
            while (not visibitity):
                ActionChains(driver).click(driver.find_element_by_id('attackButton')).perform()
                time.sleep(1)
                visibitity = driver.find_element_by_id('success-killed').is_displayed()
            time.sleep(1.5)
            ActionChains(driver).click(driver.find_element_by_xpath('//a[text()[contains(., "Close")]]')).perform()
        except:
            pass
        do_step = driver.find_element_by_id("primaryStepButton")
        btn_txt = do_step.get_attribute('innerHTML')
        while btn_txt != 'Take another step' and btn_txt != '\nTake a step\n':
            btn_txt = do_step.get_attribute('innerHTML')

# do_steps(driver)
# driver.close()