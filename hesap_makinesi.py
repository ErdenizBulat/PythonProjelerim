import math


def gelismis_hesap_makinesi():
    print("Gelişmiş Hesap Makinesi")
    print("Seçmek istediğiniz işlemi girin:")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Üs Alma")
    print("6 - Kare Kök Alma")
    print("7 - Faktöriyel")
    print("8 - Sinüs")
    print("9 - Cosinüs")


    islem = input("Seçiminizi yapın (1/2/3/4/5/6/7/8/9/): ")

    if islem in ['1', '2', '3', '4', '5']:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))

        if islem == '1':
            print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
        elif islem == '2':
            print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
        elif islem == '3':
            print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
        elif islem == '4':
            if sayi2 != 0:
                print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
            else:
                print("Bir sayıyı sıfıra bölemezsiniz!")
        elif islem == '5':
            print(f"{sayi1} ^ {sayi2} = {sayi1 ** sayi2}")

    elif islem == '6':
        sayi = float(input("Bir sayı girin: "))
        if sayi >= 0:
            print(f"Kare kök({sayi}) = {math.sqrt(sayi)}")
        else:
            print("Negatif sayının karekökünü alamazsınız!")

    elif islem == '7':
        sayi = int(input("Bir tam sayı girin: "))
        if sayi < 0:
            print("Faktöriyel negatif sayılar için tanımlı değildir!")
        else:
            print(f"{sayi}! = {math.factorial(sayi)}")

    elif islem == '8':
        derece = float(input("Bir açı değeri (derece) girin: "))
        radian = math.radians(derece)
        print(f"Sinüs({derece}°) = {math.sin(radian)}")

    elif islem == '9':
        derece = float(input("Bir açı değeri (derece) girin: "))
        radian = math.radians(derece)
        print(f"Cosinüs({derece}°) = {math.cos(radian)}")


    else:
        print("Geçersiz işlem seçimi!")


# Hesap makinesi fonksiyonunu çalıştırmak için:
gelismis_hesap_makinesi()
