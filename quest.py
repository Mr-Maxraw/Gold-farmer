from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from log_in import log_in
import time
import os
# from dotenv import load_dotenv

# load_dotenv()

# driver = webdriver.Chrome()
# driver.set_window_size(800, 800)
# log_in(os.environ['EMAIL'], os.environ['PASSWORD'], driver)

def do_quests(driver):
    driver.get('https://web.simple-mmo.com/quests/viewall')

    while True:
        quest_list = driver.find_elements_by_class_name("kt-widget5__item")
        quest_list.reverse()
        needed_quests = list()
        for quest in quest_list:
            try:
                complete = quest.find_element_by_xpath('.//span[text()[contains(., "Completed")]]')
                pass
            except:
                needed_quests.append(quest)
                pass
        quest = needed_quests[0]
        try:
            open_modal = quest.find_element_by_xpath('.//button[text()[contains(., "View Quest")]]')
            open_modal.send_keys(Keys.ENTER)
            ActionChains(driver).click(open_modal).perform()
            time.sleep(1)
            st_q_btn = driver.find_element_by_xpath('//button[text()[contains(., "Perform quest")]]')
            ActionChains(driver).click(st_q_btn).perform()
        except:
            driver.refresh()
        try:
            time.sleep(1.5)
            error_msg = driver.find_element_by_id('swal2-validation-message')
            if error_msg.get_attribute('innerHTML') == "Error: You don't have enough quest points.":
                break
        except:
            pass
        driver.refresh()

# do_quests(driver)
# driver.close()