print("********************\nATM sistemine hoşgeldiniz\n********************")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan 'q' tuşu ile çıkabilirsiniz.

""")

bakiye  = 1000 # Bakiyemiz 1000 lira olsun.

while True:
    islem = input("İşlemi giriniz:")

    if (islem == "q"):
        print("Yine bekleriz....")
        break
    elif (islem == "1"):
        print("Bakiyeniz {} tldir".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Yatırmak istediğiniz tutar:"))

        bakiye += miktar
    elif (islem == "3"):
        miktar = int(input("Çekmek istediğiniz tutar:"))
        if (bakiye - miktar < 0 ):
            print("Bu kadar para çekemezsiniz...")
            print("Bakiyeniz {} tldir".format(bakiye))
            continue
        bakiye -= miktar

    else:
        print("Lütfen geçerli bir işlem giriniz.")