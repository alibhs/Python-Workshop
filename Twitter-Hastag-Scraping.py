from Tbilgi import kullanıcıadı,sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches',['enable-logging'])

driver=webdriver.Chrome(executable_path=r"C:/Users/Ali/Desktop/chromedriver.exe",chrome_options=options)

url="https://twitter.com/i/flow/login"
driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(2)

ka=driver.find_element_by_xpath("//input[@autocomplete='username']")
ka.send_keys(kullanıcıadı)
time.sleep(2)
ka.send_keys(Keys.ENTER)
time.sleep(2)

sif=driver.find_element_by_xpath("//input[@autocomplete='current-password']")
sif.send_keys(sifre)
time.sleep(2)
sif.send_keys(Keys.ENTER)
time.sleep(3)

aranan="atatürk"
arama="https://twitter.com/search?q={}&src=typed_query&f=live".format(aranan)
driver.get(arama)
time.sleep(2)

bilgi=[]
profil = driver.find_elements_by_css_selector(".css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu")
for i in profil:
    bilgi.append(i.text)

tweetsayısı=50

while True:
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(2)
    profil2 = driver.find_elements_by_css_selector(".css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu")
    for j in profil2:
        x=j.text
        if x not in bilgi:
            bilgi.append(x)
    if len(bilgi)>=tweetsayısı:
        break

sayac=1
for k in range(0,tweetsayısı):
    kisi=(bilgi[k].split("\n")[1])
    yazılantwit=(bilgi[k].split("\n")[4])
    print(f"{sayac}-{kisi}: {yazılantwit}")
    sayac+=1
    sayac=sayac
    
print(bilgi)