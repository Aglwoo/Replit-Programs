import urllib
from urllib import request
#import re
#from html.parser import HTMLParser

response = urllib.request.urlopen("http://amazon.com")
html = response.read()

#Some how extract that wanted data

f = open('page.html', 'w')
f.write(data)
f.close()