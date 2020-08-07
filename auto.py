from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from log_in import log_in
from time import sleep, strftime, localtime
import os
from dotenv import load_dotenv
from job import do_job
from quest import do_quests
from travel import do_steps
import sys

load_dotenv()

chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument("--mute-audio")
#chrome_optionsheadless = True

driver = webdriver.Chrome(options=chrome_options)

driver.set_window_size(800, 800)
driver.set_window_position(0, 650)

log_in(os.environ['EMAIL'], os.environ['PASSWORD'], driver)
loop_cnt = 1
print("input 1 for single loop or other int for continuous run")
issingle = int(input()) == 1 

while True:
    sys.stdout = open('bot.log', 'a')
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    print('start loop ' + str(loop_cnt), flush=True)
    do_quests(driver)
    do_steps(driver)
    do_quests(driver)
    do_steps(driver)
    job_cnt = do_job(driver)
    if issingle:
        print('finish single loop (jobs may still be running)')
        sys.stdout.close()
        driver.close()
        break
    else:
        for i in range(job_cnt * 10 + 1):
            sleep(60)
            print(i+1, end=' ', flush=True)
        print('\nfinish loop ' + str(loop_cnt))
    loop_cnt = loop_cnt + 1
    sys.stdout.close()