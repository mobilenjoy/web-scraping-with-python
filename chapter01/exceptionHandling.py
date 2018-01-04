from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	html = urlopen(url)
	bsObj = BeautifulSoup(html.read(), "html.parser")
	return bsObj.h1


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
    
#html = urlopen("http://www.pythonscraping.com/pages/page1.html")    
