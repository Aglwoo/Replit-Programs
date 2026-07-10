import pandas as pd
import lxml
import bs4
print("hi")
word = pd.read_html("https://www.nasdaq.com/market-activity/stocks")
print("hi")
len(word)
print("hi")
bob = open("bob.txt","w")
word =  str(word)
bob.writelines(word)



