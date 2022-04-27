import requests
from bs4 import BeautifulSoup

url= "https://havadurumu15gunluk.xyz/havadurumu/630/istanbul-hava-durumu-15-gunluk.html"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("div",{"class":"table"})

for div in list:
    date2=div.div.findNextSibling().findNextSibling().text
    date3=div.div.findNextSibling().findNextSibling().findNextSibling().text
    date4=div.div.findNextSibling().findNextSibling().findNextSibling().findNextSibling().text
    date5=div.div.findNextSibling().findNextSibling().findNextSibling().findNextSibling().findNextSibling().text
    date6=div.div.findNextSibling().findNextSibling().findNextSibling().findNextSibling().findNextSibling().findNextSibling().text
    date7=div.div.findNextSibling().findNextSibling().findNextSibling().findNextSibling().findNextSibling().findNextSibling().findNextSibling().text
    date8=div.div.findNextSibling().findNextSibling().findNextSibling().findNextSibling().findNextSibling().findNextSibling().findNextSibling().findNextSibling().text
    
   
    print(date2)
    print(date3)
    print(date4)
    print(date5)
    print(date6)
    print(date7)
    print(date8)
    #Last temperature is temperature at night,I couldn't display it properly.Will try to do so in next version.



