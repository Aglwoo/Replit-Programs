from requests_html import HTML, HTMLSession

#SPAN
session = HTMLSession()
r = session.get('https://www.nasdaq.com/market-activity/stocks/amzn')

article = r.html.find('/html/body/div[3]/div/main/div[2]/div[3]/section/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span/span[2]')
print(article)