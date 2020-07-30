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

def do_job(driver):
    driver.get('https://web.simple-mmo.com/jobs/viewall')
    job_btn = driver.find_element_by_xpath('//a[text()[contains(., "Go to your job")]]')
    ActionChains(driver).click(job_btn).perform()
    try:
        st_job_btn =  driver.find_element_by_xpath('//a[text()[contains(., "Start working")]]')
        ActionChains(driver).click(st_job_btn).perform()
        time.sleep(1)
        st_job_btn2 =  driver.find_element_by_xpath('//button[text()[contains(., "Start the job")]]')
        slider = driver.find_element_by_xpath('//input[@type="range"]')
        job_cnt = slider.get_attribute('max')
        for i in range(int(job_cnt) - 1):
            slider.send_keys(Keys.RIGHT)
        ActionChains(driver).click(st_job_btn2).perform()
        return int(job_cnt)
    except:
        print('fail')
        return 0

# do_job(driver)
# driver.close()