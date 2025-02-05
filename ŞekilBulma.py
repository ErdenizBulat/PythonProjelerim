sekil = input("hangi şeklin tipini öğrenmek istiyorsunuz?")

if (sekil =="dörtgen"):
    print("lütfen kenarları giriniz.")
    a = int(input("kenar1:"))
    b = int(input("kenar2:"))
    c = int(input("kenar3:"))
    d = int(input("kenar4:"))

    if (a == b and a == c and a == d):
        print("kare")
    elif (a == c and b == d):
        print("dikdörtgen")
    else:
        print("dörtgen")


elif (sekil == "üçgen"):
    print("lütfen kenarları giriniz.")
    a = int(input("kenar1:"))
    b = int(input("kenar2:"))
    c = int(input("kenar3:"))
    if (abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c ):
            print("eşkenar üçgen")
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            print("ikizkenar üçgen")
        else:
            print("çeşitkenar üçgen")
    else:
        print("üçgen belirtmiyor")
else:
    print("geçersiz şekil")