import math

# Kullanıcıdan işlem türünü seçmesini isteyin
print("Hesap Makinesi")
print("İşlem Seçin:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
print("5. Üs Alma")
print("6. Karekök Alma")

secim = input("Seçiminizi yapın (1/2/3/4/5/6): ")

# Kullanıcıdan sayıları alalım
if secim in ['5', '7']:  # Üs alma ve karekök için sadece bir sayı gerekir
    sayi1 = float(input("Bir sayı girin: "))
else:
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

# Seçime göre işlemi yapalım
if secim == '1':
    print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
elif secim == '2':
    print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
elif secim == '3':
    print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
elif secim == '4':
    if sayi2 != 0:
        print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
    else:
        print("Hata! Bir sayıyı sıfıra bölemezsiniz.")
elif secim == '5':
    # Üs alma işlemi
    us = float(input("Üs değerini girin: "))
    print(f"{sayi1} ^ {us} = {sayi1 ** us}")
elif secim == '6':
    # Karekök alma işlemi
    if sayi1 >= 0:
        print(f"Karekök({sayi1}) = {math.sqrt(sayi1)}")
    else:
        print("Hata! Negatif bir sayının karekökünü alamazsınız.")
else:
    print("Geçersiz giriş!")