from selenium import webdriver

url = "https://www.google.com/finance/quote/BTC-usd"
browser = webdriver.Chrome()
browser.get(url)

now= browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[4]/div/main/div[2]/div[1]/div[1]/c-wiz/div/div[1]/div/div[1]/div/div[1]/div/span/div/div')
print(now)