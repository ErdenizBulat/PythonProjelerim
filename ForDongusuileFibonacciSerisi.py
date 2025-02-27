"""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.

1,1,2,3,5,8,13,21,34...............
"""
ilk_sayi = 1

ikincisayi = 1

fibonacci = [ilk_sayi,ikincisayi]
for i in range(10):


    ilk_sayi,ikincisayi = ikincisayi,ilk_sayi + ikincisayi

    fibonacci.append(ikincisayi)

print(fibonacci)
