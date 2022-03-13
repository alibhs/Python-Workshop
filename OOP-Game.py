import time
import random
import sys

class Oyuncu:
    def __init__(self,isim,can=5,enerji=100):
        self.isim = isim
        self.can = can
        self.enerji = enerji
        self.darbe = 0
    
    def mevcut_durum_goruntuleme(self):
        print("darbe: ", self.darbe)
        print("can: ", self.can)
        print("enerji: ", self.enerji)
    
    def saldır(self,rakip):
        print("Bir saldırı gerçekleştirdiniz...")
        print("Saldırı sürüyor bekleyiniz...")

        for i in range(10):
            time.sleep(.3)
            print(".",end=" ",flush=True)
        sonuc = self.saldırı_sonucunu_hesapla()

        if sonuc == 0:
            print("\nSonuç = Kazanan taraf yok")
        if sonuc == 1:
            print("\nSonuç = Rakibinizi darbelediniz")
            self.darbele(rakip)
        if sonuc == 2:
            print("\nSonuç = Rakibinizden darbe aldınız")
            rakip.darbele(self)
 
    def saldırı_sonucunu_hesapla(self):
        return random.randint(0,2)
        
    def kac(self):
        print("Kaçılıyor...")
        for i in range(10):
            time.sleep(.3)
            print("\n", flush=True)
        print("Rakibiniz sizi yakaladı.")
        
    def darbele(self,darbelenen):
        darbelenen.darbe +=1
        darbelenen.enerji -=1
        if(darbelenen.darbe % 5) == 0:
            darbelenen.can -=1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print("Oyunu {} Kazandı!".format(self.isim))
            self.oyundan_cık()

    def oyundan_cık(self):
        print("Çıkılıyor...")
        sys.exit()

# OYUNCULAR
siz = Oyuncu("Ali")
rakip = Oyuncu("Oğuzhan")

#OYUN BAŞLANGICI
while True:
    print("""Şuanda rakibinizle karşı karşıyasınız yapmak istediğiniz hamleyi seçiniz :
    Saldır : s
    Kaç : k
    Çık : q""")
    hamle = input()
    if hamle == "s":
        siz.saldır(rakip)
        print('Rakibinizin durumu \n')
        rakip.mevcut_durum_goruntuleme()

        print('Sizin durumunuz\n.')
        siz.mevcut_durum_goruntuleme()
    if hamle == "k":
        siz.kac()
    if hamle == "q":
        siz.oyundan_cık()
                
 
