import json
import re
import time
import random


class Site:
    def __init__(self):
        self.dongu = True
        self.veriler = self.veriAl()

    def program(self):
        secim = self.menu()
        if secim=="1":
            self.giris()
        if secim=="2":
            self.kayıtOl()
        if secim=="3":
            self.cikis()
    
    def menu(self):
        def kontrol(secim):
            if re.search("[^1-3]",secim):
                raise Exception("Lütfen 1 ile 3 Arasında Geçerli Bir Sayı Giriniz...")
            elif len(secim)!=1:
                raise Exception("Lütfen 1 ile 3 Arasında Geçerli Bir Sayı Giriniz...")
        while True:
            try:
                secim=input("Merhabalar, alibahsi.com'a Hoşgeldiniz.\n\nLütfen Yapmak İstediğiniz İşlemi Seçiniz...\n\n[1]-Giriş\n[2]-Kayıt Ol\n[3]-Çıkış\n\n")
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim
            
    def giris(self):
        print("Giriş Menüsüne Yönlendiriliyorsunuz...")
        time.sleep(2)
        KullaniciAdi=input("Lütfen Kullanıcı Adınızı Giriniz:")
        Sifre = input("Lütfen Şifrenizi Giriniz:")
        sonuc = self.girisKontrol(KullaniciAdi, Sifre)
        if sonuc == True:
            self.girisBasarili()
        else:
            self.girisBasarisiz()



    def girisKontrol(self,KullaniciAdi,Sifre):
        self.veriler=self.veriAl()

        for kullanıcı in self.veriler["Kullanıcılar"]:
            if kullanıcı["Kullanıcıadı"]==KullaniciAdi and kullanıcı["Sifre"]==Sifre:
                return True
        return False

    def girisBasarili(self):
        print("Kontrol Ediliyor...")
        time.sleep(2)
        print("Giriş Başarılı alibahsi.com'a Hoşgeldiniz :)")
        self.sonuc = False
        self.dongu = False

    def girisBasarisiz(self):
        print("Kullanıcı Adi veya Sifre Hatalı!!!")
        time.sleep(2)
        self.menudon()

    def kayıtOl(self):
        def kontrolka(KullaniciAdi):
            if len(KullaniciAdi)<8:
                raise Exception("Kullanıcı Adı Minimum 8 Karakterden Oluşmalıdır!!!!")
            while True:
                try:
                    KullaniciAdi=input("Lütfen Kullanıcı Adınızı Giriniz : ")
                    kontrolka(KullaniciAdi)
                except Exception as hataad:
                    print(hataad)
                    time.sleep(2)
                else:
                    break

        def kontrolsifre(Sifre):
            if len(Sifre)<8:
                raise Exception("Şifreniz Minimum 8 Karakterden Oluşmalıdır!!!!")
            elif not re.search("[0-9]",Sifre):
                raise Exception("Şifreniz Minimum Bir Rakam İçermelidir!!!")
            elif not re.search("[A-Z]",Sifre):
                raise Exception("Şifreniz Minimum Bir Büyük Harf İçermelidir!!!")    
            elif not re.search("[a-z]",Sifre):
                raise Exception("Şifreniz Minimum Bir Küçük Harf İçermelidir!!!")
            while True:
                try:
                    Sifre=input("Lütfen Sifrenizi Giriniz : ")
                    kontrolsifre(Sifre)
                except Exception as hatasifre:
                    print(hatasifre)
                    time.sleep(2)
                else:
                    break

        def kontrolmail(Mail):
            if not re.search("@" and ".com",Mail):
                raise Exception("Geçerli Bir Mail Adresi Giriniz!!!!")
            while True:
                try:
                    Mail=input("Lütfen Mailinizi Giriniz : ")
                    kontrolmail(Mail)
                except Exception as hatamail:
                    print(hatamail)
                    time.sleep(2)
                else:
                    break

        sonuc=self.kayıtVarmı(KullaniciAdi,Mail)
        if sonuc == True:
            print("Kullanıcı Adı ve Mail Sistemde Kayıtlı..")
        else:
            aktivasyonkodu=self.aktivasyonGonder()
            durum=self.aktivasyonKontrol(aktivasyonkodu)
        while True:
            if durum == True:
                self.veriKaydet(KullaniciAdi,Sifre,Mail)
                break
            else:
                input("Geçersiz Aktivasyon Kodu Lütfen Tekrar Giriniz...\n...")

        
    
    def kayıtVarmı(self,KullaniciAdi,Sifre):
        try:
            for kullanıcı in self.veriler["Kullanıcılar"]:
                if kullanıcı["Kullanıcıadı"]==KullaniciAdi and kullanıcı["Mail"]==Mail:
                    return True
        except KeyError:
            return False
        return False

    def aktivasyonGonder(self):
        with open("C:*Users/Ali/Desktop/Aktivasyon.txt","w") as Dosya:
            aktivasyon=str(random.randint(100000,999999))
            Dosya.write("Aktivasyon kodunuz : ",aktivasyon)
        return aktivasyon
    
    def aktivasyonKontrol(self,aktivasyon):
        
        aktivasyonkodual = input("Lütfen Telefonunuza Gelen Aktivasyon Kodunu Giriniz : ")
        if aktivasyon == aktivasyonkodual:
            return True
        else:
            return False

    def veriAl(self):
        pass

    def veriKaydet(self,KullaniciAdi,Sifre,Mail):
        pass
    
    def cikis(self):
        print("Sistemden Çıkılıyor...")
        time.sleep(2)
        self.dongu=False
        exit()
    
    def menudon(self):
        while True:
            x=input("Ana menüye dönmek için '5' e çıkış yapmak için 'Q' ya basınız")
            if x=="5":
                print("Ana menüye dönülüyor..")
                time.sleep(2)
                self.program()
                break
            elif x == "Q" or "q":
                self.cikis()
                break
            else:
                print("Lütfen Geçerli Bir Değer Giriniz..:")
    

Sistem = Site()
while Sistem.dongu:
    Sistem.program()