import random
import time

class Kumanda():

    def __init__(self, tvDurum = "Kapali", tvSes = 0, kanalListesi = ["Now", "Halk", "Ntv"], kanal = "Now"):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal

    def tvAc(self):
        if (self.tvDurum == "Acik"):
            print("Televizyon zaten acik")
        else:
            print("Televizyon aciliyor")
            self.tvDurum = "Acik"

    def tvKapat(self):
        if(self.tvDurum == "Kapali"):
            print("Televiyon zaten kapali")
        else:
            print("Teleziyon kapaniyor")
            self.tvDurum = "Kapali"


    def sesAyarlari(self):
        while True:
            print("Sesi azalt: '<'\nSesi arttir: '>'\nCikis: q")
            cevap = input("Cevap: ")

            if cevap == "<":
                if(self.tvSes != 0):
                    self.tvSes -= 1
                    print("Ses: ", self.tvSes)
                else:
                    print("Ses 0 dan daha dusuk olamaz.")

            elif cevap == ">":
                if(self.tvSes != 35):
                    self.tvSes += 1
                    print("Ses: ", self.tvSes)
                else:
                    print("Ses 35 den daha yuksek olamaz.")

            else:
                print("Ses Guncellendi: ", self.tvSes)
                break

    def kanalEkle(self, kanalIsmi):
            print("Kanal ekleniyor...")
            time.sleep(1)
            self.kanalListesi.append(kanalIsmi)
            print("Kanal eklendi.")

    def rastgeleKanal(self):
        rastgele = random.randint(0, len(self.kanalListesi) - 1)
        self.kanal = self.kanalListesi[rastgele]
        print("Su anki kanal: ", self.kanal)

    def __str__(self):
        return f"Tv durum: {self.tvDurum}\nTv ses: {self.tvSes}\nKanal Listesi: {self.kanalListesi}\nSu anki kanal: {self.kanal}"

    def __len__(self):
        return len(self.kanalListesi)



kumanda = Kumanda()

print("""
Televizyon Uygulamasi

1.Tv Ac
2.Tv Kapat
3.Ses Ayarlari
4.Kanal Ekle
5.Rastgele kanal gecme
6.Televizyon Bilgileri
7.Kanal sayisini ogrenme
Cikmak icin 'b' basiniz

""")

while True:
    islem = input("Islem seciniz: ")

    if islem == "b":
        print("Program sonlandiirliyor...")
        break

    elif islem == "1":
        kumanda.tvAc()

    elif islem == "2":
        kumanda.tvKapat()

    elif islem == "3":
        kumanda.sesAyarlari()

    elif islem == "4":
        kanalIsmi = input("Kanal ismini giriniz: ")
        kumanda.kanalEkle(kanalIsmi)

    elif islem == "5":
        kumanda.rastgeleKanal()

    elif islem == "6":
        print(kumanda)

    elif islem == "7":
        print("Kanal sayisi: ", len(kumanda))

    else:
        print("Gecersiz islem girdiniz.")