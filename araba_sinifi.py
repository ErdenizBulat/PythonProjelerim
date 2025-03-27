class Araba():
    def __init__(self, marka, model, yil, max_hiz, yakit_tipi, depo_kapasitesi, yakit_seviyesi = 0, anlik_hiz = 0):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.max_hiz = max_hiz
        self.yakit_tipi = yakit_tipi
        self.depo_kapasitesi = depo_kapasitesi
        self.anlik_hiz = anlik_hiz
        self.yakit_seviyesi = yakit_seviyesi

    def __len__(self):
        return self.depo_kapasitesi

    def __str__(self):
        return "Araba: {}\nModel: {}\nYil: {}\nMax Hiz: {}\nYakit Tipi: {}\nDepo Kapasitesi: {}\nYakit Seviyesi: {}\nAnlik Hiz: {}".format(self.marka, self.model, self.yil, self.max_hiz, self.yakit_tipi, self.depo_kapasitesi, self.yakit_seviyesi, self.anlik_hiz)

    def hizlan(self, hizlanma_miktari):

        if self.anlik_hiz + hizlanma_miktari <= self.max_hiz:
            self.anlik_hiz += hizlanma_miktari
            print(f"Arabanin hizi {self.anlik_hiz}km/s hizla gidiyor")

        else:
            print(f"Arabanin maksimum hizi {self.max_hiz}km/s'tir. Araba daha fazla hizlanamaz.")

    def yavasla(self, yavaslanma_miktari):

        if self.anlik_hiz > 0:
            self.anlik_hiz -= yavaslanma_miktari
            print(f"Arabanin hizi {self.anlik_hiz}km/s hizla gidiyor.")

        elif self.anlik_hiz < 0:
            print("Gecersiz deger girdiniz arabain hizi negatif olamaz.")

        else:
            print("Araba zaten duruyor.")

    def dur(self):

        if self.anlik_hiz > 0:
            self.anlik_hiz = 0
            print("Araba durduruldu.")

        else:
            print("Araba zaten duruyor.")

    def kalk(self):

        if self.anlik_hiz == 0:
            print("Araba hareket etmeye basliyor.")

        else:
            print("Araba zaten hareket ediyor.")

    def yakit_ekle(self, eklenecek_yakit):

        if self.yakit_seviyesi < depo_kapasitesi:
            self.yakit_seviyesi += eklenecek_yakit
            print(f"{eklenecek_yakit}L Yakit eklendi.\nYakit seviyesi: {self.yakit_seviyesi}")

        else:
            print("Arabanin yakiti zaten dolu!")

    def yakit_durumu(self):
        print(f"Arabada {self.yakit_seviyesi}L yakiti var.")


marka = input("Marka giriniz: ")
model = input("Model giriniz: ")
yil = int(input("Yil giriniz: "))
max_hiz = int(input("Max hiz giriniz: "))
yakit_tipi = input("Yakit tipi giriniz: ")
depo_kapasitesi = int(input("Depo kapasitesi giriniz: "))

araba1 = Araba(marka, model, yil, max_hiz, yakit_tipi, depo_kapasitesi)

print("""
Araba Uygulamasi

1. Depo kapasitesini goster
2. Arabanin bilgilerini goster
3. Arabanin hizini arttir
4. Arabanin hizini azalt
5. Arabani durdur
6. Arabani hareket ettir
7. Arabana yakit ekle
8. Arabanin yakit durumu
Cikis icin 'q' basiniz

""")

while True:

    islem = input("Islem seciniz: ")

    if islem == "q":
        print("Program sonlandiriliyor...")
        break

    elif islem == "1":
        print("Depo kapasitesi: ", len(araba1))

    elif islem == "2":
        print(araba1)

    elif islem == "3":
        hizlanma_miktari = int(input("Hizlanma miktari giriniz: "))
        araba1.hizlan(hizlanma_miktari)

    elif islem == "4":
        yavaslama_miktari = int(input("Yavaslama miktarini giriniz: "))
        araba1.yavasla(yavaslama_miktari)

    elif islem == "5":
        araba1.dur()

    elif islem == "6":
        araba1.kalk()

    elif islem == "7":
        eklenecek_yakit = int(input("Kac litre yakit koymak istiyorsunuz: "))
        araba1.yakit_ekle(eklenecek_yakit)

    elif islem == "8":
        araba1.yakit_durumu()

    else:
        print("Gecersiz islem girdiniz.")