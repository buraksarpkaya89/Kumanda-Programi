import random
import time

class kumanda():


    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = [], kanal = "boş" ):
        self.tv_durum =tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal =kanal

    def tv_ac(self):

        if (self.tv_durum == "Açık"):
            print("Televizyonunuz zaten açık")
        else:
            print("Televizyon açılıyor")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if (self.tv_durum =="Kapalı"):
            print("Televizyonunuz zaten kapalı")
        else:
            print("Televizyonunuz açılıyor")
            self.tv_durum = "Kapalı"

    def ses_ayarlari(self):

         if (self.tv_durum == "Açık"):

             while True:
                 cevap = input("Sesi azalt: '<'\nSesi arttır : '>'\nÇıkış : çıkış\nBir Tuşa basınız: ")
                 if (cevap == "<"):
                     if (self.tv_ses != 0):
                         self.tv_ses -= 1
                         print("Ses : ", self.tv_ses)
                 elif(cevap == ">"):

                     if(self.tv_ses != 50):
                         self.tv_ses += 1
                         print(("Ses : ", self.tv_ses))
                 else:
                     print("Ses güncellendi ", self.tv_ses)
                     break
         else:
             print("Lütfen televizyonu açınız")

    def kanal_ekle(self,kanal_ismi):
        if (self.tv_durum == "Açık"):
            print(("Kanal ekleniyor"))
            time.sleep(1)
            self.kanal_listesi.append(kanal_ismi)
            print(("Kanal eklendi"))
        else:
            print("Lütfen televizyonu açınız")

    def rastgele_kanal(self):
        if (self.tv_durum == "Açık"):
            rastgele = random.randint(0, len(self.kanal_listesi)-1)

            self.kanal = self.kanal_listesi[rastgele]
            print("Şu anki kanal : ",self.kanal)
        else:
            print("Lütfen televizyonu açınız")

    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv durumu : {}\nKanal listesi : {}\nŞu anki kanal : {}\n".format(self.tv_durum,self.kanal_listesi,self.kanal)

Kumanda = kumanda()
print("""
Televizyon Kumandası

1.Tv aç
2.Tv kapat
3.Ses ayarları
4.Kanal ekle
5.Kanal sayısını öğrenme
6.Rastgele kanala geçme
7.Televizyon bilgileri
Çıkmak için 'q' ya basınız
""")

while True:
    islem =input("İşlemi seçiniz: ")

    if (islem == "q"):
        print("işlem sonlandırılıyor..")
        break
    elif (islem == "1"):
        Kumanda.tv_ac()
    elif (islem == "2"):
        Kumanda.tv_kapat()
    elif (islem == "3"):\
        Kumanda.ses_ayarlari()
    elif (islem == "4"):
        kanalisimleri = input("Kanal işlemlerini ',' ile ayırarak girin: ")
        kanal_listesi = kanalisimleri.split(",")

        for eklenecekler in kanal_listesi:
            Kumanda.kanal_ekle(eklenecekler)

    elif (islem == "5"):
        print("Kanal sayısı: ", len(Kumanda))

    elif (islem == "6"):
        Kumanda.rastgele_kanal()
    elif (islem == "7"):
        print(Kumanda)
    else:
        print("Geçersiz işlem")
