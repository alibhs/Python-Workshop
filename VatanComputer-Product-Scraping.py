import requests
from bs4 import BeautifulSoup

for sayfa in range(1,11):

    url="https://www.vatanbilgisayar.com/cep-telefonu-modelleri/?page={}".format(sayfa)

    parser=BeautifulSoup(requests.get(url).content,"html.parser")

    veri = parser.find("div",{"class":"wrapper-product wrapper-product--list-page clearfix"})\
        .find_all("div",{"class":"product-list product-list--list-page"})

    for i in veri:
        ad=i.find("div",{"class":"product-list__content"}).find("a",{"class":"product-list__link"})\
            .find("div",{"class":"product-list__product-name"}).string

        fiyat=i.find("div",{"class":"product-list__content"}).find("div",{"class":"product-list__cost"})\
            .find("span",{"class":"product-list__price"}).string

        print(f"Telefon Modeli: {ad.lstrip()}Telefon Fiyatı: {fiyat} TL'dir.\n")