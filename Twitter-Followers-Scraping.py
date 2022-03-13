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

url="https://twitter.com/alibhss"
driver.get(url)
time.sleep(3)

takipci=driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > div > div > div.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a")
takipci.click()
time.sleep(3)

divliste=[]
takipciliste1=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/section/div").find_elements_by_css_selector(".css-901oao.css-bfa6kz.r-14j79pv.r-18u37iz.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0")
time.sleep(2)

for j in takipciliste1:
    divliste.append(j.text)

sonyukseklik=driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(2)
    takipciliste2=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/section/div").find_elements_by_css_selector(".css-901oao.css-bfa6kz.r-14j79pv.r-18u37iz.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0")
    for i in takipciliste2:
        x=i.text
        if x not in divliste:
            divliste.append(x)
    yeniyukseklik=driver.execute_script("return document.documentElement.scrollHeight")
    if sonyukseklik==yeniyukseklik:
        break
    sonyukseklik=yeniyukseklik

sayac=0
for k in divliste:
    sayac+=1
    sayac=sayac
    print(f"{sayac}-{k}")

