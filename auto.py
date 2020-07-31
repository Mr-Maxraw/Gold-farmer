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
import sys

load_dotenv()

driver = webdriver.Chrome()

log_in(os.environ['EMAIL'], os.environ['PASSWORD'], driver)
loop_cnt = 1

while True:
    sys.stdout = open('bot.log', 'a')
    print('start loop 1')
    do_quests(driver)
    do_steps(driver)
    do_quests(driver)
    do_steps(driver)
    job_cnt = do_job(driver)
    for i in range(job_cnt * 10 + 1):
        sleep(60)
        print(i+1, end='', flush=True)
    print('finish loop 1')
    sys.stdout.close()