import requests
from bs4 import BeautifulSoup

link="https://www.imdb.com/chart/top"
kod = requests.get(link).content
parser=BeautifulSoup(kod,"html.parser")

tr=parser.find("tbody",{"class":"lister-list"}).find_all("tr")

for i in tr:
    baslik= i.find("td",{"class":"titleColumn"}).find("a").string
    print(baslik)
