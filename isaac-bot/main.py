from typing_extensions import runtime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

ONE_DAY = 24 * 60 * 60  # seconds

x = 0
i = 0
global ans
ans = 0.01
def ansspam(ans):
  while True:
  
  # I don't actually know what this stuff does.
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # This is Google Chrome. Shoved into a variable called 'driver'
    driver = webdriver.Chrome(options=chrome_options)
    # Change the link to your server's vote site.
    print("Loading site...")
    driver.get("https://isaacphysics.org/questions/jury_duty?board=5d2f7a20-5ffd-4af2-80de-ca25c47d3a44&stage=a_level")
    print("Finding text box...")
    #time.sleep(3)
    name_txt_box = driver.find_element("xpath", '//*[@id="main"]/div/div[3]/div/div[1]/form/div/div[1]/div[2]/div/div[1]/label/div/input')
    for i in range(1,6):
      # Change the string to your Minecraft username.
      print("Typing userame...")
      name_txt_box.send_keys(round(ans,2))

      # This submits the form, sending your vote.
      print("Submitting...")
      name_txt_box.submit()
      #time.sleep(2)
      name_txt_box.clear()
      ans += 0.01


def antilock():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://aternos.org/go/")
  while True:
    i =  0
def run():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  print("Loading site...")
  driver.get("https://aternos.org/go/")
  print("Finding login")
  #time.sleep(3)
  un = driver.find_element("xpath",'/html/body/div[3]/div/div/div[3]/div[4]/div[1]/div[2]/input')
  un.send_keys("aglw00")
  print("Finding password")
  pw = driver.find_element("xpath",'/html/body/div[3]/div/div/div[3]/div[4]/div[2]/div[2]/input')
  pw.send_keys("bobross")
  submit_button = driver.find_element('xpath','/html/body/div[3]/div/div/div[3]/div[4]/button')
  submit_button.click()
  while True:
    i=0
run()
#antilock()
#ansspam(ans)