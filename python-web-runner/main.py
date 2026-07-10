from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random
from ka import keep_alive
from ua import ua


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

sleep(3)
keep_alive()

s = 0
while True:
    ua1 = random.choice(ua)
    chrome_options.add_argument(f'user-agent={ua1}')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://web.253611.repl.co")
    sleep(1000000)