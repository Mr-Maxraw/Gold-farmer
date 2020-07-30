from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from log_in import log_in
from time import sleep
import os
from dotenv import load_dotenv
from job import do_job
from quest import do_quests
from travel import do_steps

load_dotenv()

driver = webdriver.Chrome()

log_in(os.environ['EMAIL'], os.environ['PASSWORD'], driver)

while True:
    do_quests(driver)
    do_steps(driver)
    job_cnt = do_job(driver)
    sleep(job_cnt * 600 - 750)