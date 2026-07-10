from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Replace this with the path to your html file
FULL_PATH_TO_HTML_FILE = 'https://aternos.org/go/l'

def visit_website(browser):
    browser.get(FULL_PATH_TO_HTML_FILE)
    time.sleep(3)

    links = browser.find_elements_by_xpath("//a[@href]")
    links[0].click()
    time.sleep(10)

    # Switch webdriver focus to new tab so that we can extract html
    tab_names = browser.window_handles
    if len(tab_names) > 1:
        browser.switch_to.window(tab_names[1])

    time.sleep(1)
    html = browser.page_source
    print(html)
    print()
    print()

    if 'Charts' in html:
        print('Success')
    else:
        print('Fail')

    time.sleep(10)


options = webdriver.ChromeOptions()
# If options.headless = True, the website will not load
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')
options = webdriver.ChromeOptions()
if headless:
    options.add_argument('--headless')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/87.0.4280.88 Safari/537.36")
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options = chrome_options)
 
visit_website(browser)

browser.quit()