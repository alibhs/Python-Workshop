import re
import time

class Kayıt:
    def __init__(self,programad):
        self.programad = programad
        self.dongu = True

    def program(self):
        secim = self.menu()

        if secim == "1":
            print("Kayıt Ekleme Menusune Yönlendiriliyorsunuz...")
            time.sleep(3)
            self.kayıtEkle()
        
        if secim == "2":
            print("Kayıt Silme Menusune Yönlendiriliyorsunuz...")
            time.sleep(3)
            self.kayıtCıkar()
        
        if secim == "3":
            print("Verilere Erişiliyor...")
            time.sleep(3)
            self.kayıtOku()
        
        if secim == "4":
            self.cıkıs()

    def menu(self):
        def kontrol(secim):
            if re.search("[^1-4]",secim):
                raise Exception("Lütfen 1 ve 4 arasında geçerli bir seçim yapınız !!")
            elif len(secim)!=1:
                raise Exception("Lütfen 1 ve 4 arasında geçerli bir seçim yapınız !!")

        while True:
            try:
                secim=input("""Merhabalar , {} Otomasyon Sistemine Hoşgeldiniz.\n\nLütfen Yapmak İstediğiniz İşlemi Seçiniz...\n\n
                [1]-Kayıt Ekle
                [2]-Kayıt Sil
                [3]-Kayıt Oku
                [4]-Çıkış\n""".format(self.programad))
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim

    def kayıtEkle(self):
        def kontrolad(ad):
            if ad.isalpha() == False:
                raise Exception("Adınız Sadece Alfabetik Karakterlerden Oluşmalıdır!!")
        while True:
            try:
                ad = input("Lütfen Adınızı Giriniz : ")
                kontrolad(ad)
            except Exception as hataad:
                print(hataad)
                time.sleep(3)
            else:
                break
       
        def kontrolsoyad(soyad):
            if soyad.isalpha() == False:
                raise Exception("Soyadınız Sadece Alfabetik Karakterlerden Oluşmalıdır!!")
        while True:
            try:
                soyad = input("Lütfen Soyadınızı Giriniz : ")
                kontrolsoyad(soyad)
            except Exception as hatasoyad:
                print(hatasoyad)
                time.sleep(3)
            else:
                break
       
        def kontrolyas(yas):
            if yas.isdigit() == False:
                raise Exception("Yaşınız Sadece Rakamlardan Oluşmalıdır!!")
        while True:
            try:
                yas = input("Lütfen Yaşınızı Giriniz : ")
                kontrolyas(yas)
            except Exception as hatayas:
                print(hatayas)
                time.sleep(3)
            else:
                break

        def kontroltc(tc):
            if tc.isdigit() == False:
                raise Exception("Kimlik Numaranız Sadece Rakamlardan Oluşmalıdır!!")
            elif len(tc)!=11 :
                raise Exception("Kimlik Numaranız 11 Rakamlardan Oluşmalıdır!!")
        while True:
            try:
                tc = input("Kimlik Numaranız : ")
                kontroltc(tc)
            except Exception as hatatc:
                print(hatatc)
                time.sleep(3)
            else:
                break
        
        def kontrolmail(mail):
            if not re.search("@" and ".com",mail):
                raise Exception("Geçerli Bir Mail Adresi Giriniz...")
        while True:
            try:
                mail = input("Mail Adresinizi Giriniz : ")
                kontrolmail(mail)
            except Exception as hatamail:
                print(hatamail)
                time.sleep(3)
            else:
                break
        
        with open("C:/Users/Ali/Desktop/Bilgiler.txt","r",encoding="utf-8") as Dosya:
            satırsayısı = Dosya.readlines()
        if len(satırsayısı)==0:
            Id=1
        else:
            with open("C:/Users/Ali/Desktop/Bilgiler.txt","r",encoding="utf-8") as Dosya:
                Id=int(Dosya.readlines()[-1].split("-")[0])+1
        
        with open("C:/Users/Ali/Desktop/Bilgiler.txt","a+",encoding="utf-8") as Dosya:
            Dosya.write("{}-{} {} {} {} {}\n".format(Id,ad,soyad,yas,tc,mail))
            print("Veriler işlenmiştir...")
        self.menuDon()
                
            

    def kayıtCıkar(self):
        y = input("Lütfen Silmek İstediğiniz Id Numarasını Giriniz :")
        with open("C:/Users/Ali/Desktop/Bilgiler.txt","r",encoding="utf-8") as Dosya:
            liste=[]
            liste2 = Dosya.readlines()
            for i in range(0,len(liste2)):
                liste.append(liste2[i].split("-")[0])
            
        del liste2[liste.index(y)]

        with open("C:/Users/Ali/Desktop/Bilgiler.txt","w+",encoding="utf-8") as YeniDosya:
            for i in liste2:
                YeniDosya.write(i)
            print("Kayıt siliniyor...")
            time.sleep(3)
            print("Kayıt Başarıyla Silinmiştir...")
        self.menuDon()


    def kayıtOku(self):
        with open("C:/Users/Ali/Desktop/Bilgiler.txt","r",encoding="utf-8") as Dosya:
            for i in Dosya:
                print(i)
        self.menuDon()

    def cıkıs(self):
        print("Otomasyondan Çıkılıyor... Teşekkürler")
        self.dongu=False
        exit()

    def menuDon(self):
        while True:
            x = input("Ana menüye dönmek için 6 ya çıkmak için lütfen 5 e basınız... : ")
            if x == 6 :
                print("Ana menüye dönülüyor...")
                time.sleep(3)
                self.program()
                break
            elif x == 5 :
                self.cıkıs()
                break
            else:
                print("Lütfen geçerli bir giriş yapınız...")




Sistem=Kayıt("Anlaşılır Ekonomi")
while Sistem.dongu:
    Sistem.program()