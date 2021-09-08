sayi = float(input("Sayı : "))
sorgu = sayi == round(sayi, 0)  # x'in tam sayı veya ondalıklı olmasını denetliyor .

if sorgu:
    sayi = int(sayi)
    print(f"{sayi}, tam sayıdır")

else:
    print(f"{sayi}, ondalıklı sayıdır")


# örnek program

#1- Girilen bir sayının 0 ile 100 arasında olup olmadığını kontrol edin .

x = float(input("Sayı : "))
sorgu = x == round(x,0)

if sorgu :
    x = int(x)
    
if 0 < x < 100:
    print(f"{x}, 0 ile 100 arasındadır")
    
elif x < 0:
    print(f"{x}, 0'dan küçüktür")
    
elif x > 100:
    print(f"{x}, 100'den büyüktür")
