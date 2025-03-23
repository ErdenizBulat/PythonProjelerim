class Calisan:
    def __init__(self, adi, soyadi, maas):
        self.adi = adi
        self.soyadi = soyadi
        self.maas = maas

    def bilgileri_goster(self):
        print(f"Ad: {self.adi}\nSoyad: {self.soyadi}\nMaaş: {self.maas} TL")

class GenelMudur(Calisan):
    def __init__(self, adi, soyadi, maas, sirket):
        super().__init__(adi, soyadi, maas)
        self.sirket = sirket

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Şirket: {self.sirket}")

class Mudur(Calisan):
    def __init__(self, adi, soyadi, maas, departman):
        super().__init__(adi, soyadi, maas)
        self.departman = departman

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Departman: {self.departman}")

class Programci(Calisan):
    def __init__(self, adi, soyadi, maas, programlama_dili):
        super().__init__(adi, soyadi, maas)
        self.programlama_dili = programlama_dili

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Programlama Dili: {self.programlama_dili}")

class Stajyer(Calisan):
    def __init__(self, adi, soyadi, maas, okul):
        super().__init__(adi, soyadi, maas)
        self.okul = okul

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Okul: {self.okul}")

# Kullanıcıdan bilgi alma
gm_adi = input("Genel Müdürün adını girin: ")
gm_soyadi = input("Genel Müdürün soyadını girin: ")
gm_maas = int(input("Genel Müdürün maaşını girin: "))
gm_sirket = input("Genel Müdürün şirketini girin: ")

gm = GenelMudur(gm_adi, gm_soyadi, gm_maas, gm_sirket)

mudur_adi = input("Müdürün adını girin: ")
mudur_soyadi = input("Müdürün soyadını girin: ")
mudur_maas = int(input("Müdürün maaşını girin: "))
mudur_departman = input("Müdürün departmanını girin: ")

mudur = Mudur(mudur_adi, mudur_soyadi, mudur_maas, mudur_departman)

programci_adi = input("Programcının adını girin: ")
programci_soyadi = input("Programcının soyadını girin: ")
programci_maas = int(input("Programcının maaşını girin: "))
programci_dili = input("Programcının bildiği dili girin: ")

prog = Programci(programci_adi, programci_soyadi, programci_maas, programci_dili)

stajer_adi = input("Stajyerin adını girin: ")
stajer_soyadi = input("Stajyerin soyadını girin: ")
stajer_maas = int(input("Stajyerin maaşını girin: "))
stajer_okul = input("Stajyerin okulunu girin: ")

stajer = Stajyer(stajer_adi, stajer_soyadi, stajer_maas, stajer_okul)

gm.bilgileri_goster()
mudur.bilgileri_goster()
prog.bilgileri_goster()
stajer.bilgileri_goster()


