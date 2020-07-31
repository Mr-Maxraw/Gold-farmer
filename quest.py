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

def do_quests(driver):
    driver.get('https://web.simple-mmo.com/quests/viewall')

    while True:
        try:
            open_modal = driver.find_element_by_xpath('//button[text()[contains(., "View Quest")]]')
            ActionChains(driver).click(open_modal).perform()
            time.sleep(1)
            st_q_btn = driver.find_element_by_xpath('//button[text()[contains(., "Perform quest")]]')
            ActionChains(driver).click(st_q_btn).perform()
        except:
            driver.refresh()
        try:
            time.sleep(1)
            error_msg = driver.find_element_by_id('swal2-validation-message')
            if error_msg.get_attribute('innerHTML') == "Error: You don't have enough quest points.":
                break
        except:
            pass
        driver.refresh()

# do_quests(driver)
# driver.close()