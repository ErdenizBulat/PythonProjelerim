class Hayvan:
    def __init__(self, adi, yas):  # __init__ metodu doğru yazıldı
        self.adi = adi
        self.yas = yas

    def ses_cikar(self):
        pass

    def bilgileri_goster(self):
        print(f"Ad: {self.adi}\nYaş: {self.yas}")

class Inek(Hayvan):
    def __init__(self, adi, yas, inek_turu):
        super().__init__(adi, yas)
        self.inek_turu = inek_turu

    def ses_cikar(self):
        return "Möö!"

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"İnek Türü: {self.inek_turu}")

class Civciv(Hayvan):
    def __init__(self, adi, yas, renk):
        super().__init__(adi, yas)
        self.renk = renk

    def ses_cikar(self):
        return "Cik cik!"

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Renk: {self.renk}")

class Koyun(Hayvan):
    def __init__(self, adi, yas, yapagi_miktari):
        super().__init__(adi, yas)
        self.yapagi_miktari = yapagi_miktari

    def ses_cikar(self):
        return "Mee!"

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Yapağı Miktarı: {self.yapagi_miktari} kg")


inek_adi = input("İneğin adını girin: ")
inek_yas = int(input("İneğin yaşını girin: "))
inek_turu = input("İneğin türünü girin: ")

civciv_adi = input("Civcivin adını girin: ")
civciv_yas = int(input("Civcivin yaşını girin: "))
civciv_renk = input("Civcivin rengini girin: ")

koyun_adi = input("Koyunun adını girin: ")
koyun_yas = int(input("Koyunun yaşını girin: "))
koyun_yapagi = float(input("Koyunun yapağı miktarını girin (kg): "))


inek = Inek(inek_adi, inek_yas, inek_turu)
civciv = Civciv(civciv_adi, civciv_yas, civciv_renk)
koyun = Koyun(koyun_adi, koyun_yas, koyun_yapagi)

inek.bilgileri_goster()
print(inek.ses_cikar())
civciv.bilgileri_goster()
print(civciv.ses_cikar())
koyun.bilgileri_goster()
print(koyun.ses_cikar())





