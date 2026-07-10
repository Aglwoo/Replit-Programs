from selenium import webdriver

url = "https://www.google.com/finance/quote/BTC-GBP"
browser =webdriver.Chrome()
browser.get(url)