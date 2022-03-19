import math
#Soru 1:
#Kenar uzunlukları verilen bir dik üçgenin
#Hipotenüs uzunluğunu hesaplayınız.
# #kullanıcıdan bilgi nasıl alıyorduk
a = float(input("a kenarını giriniz: ")) #tip dönüşümü
b = float(input("b kenarını giriniz: ")) #tip dönüşümü
#c = math.sqrt(a**2 + b**2)
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print("c kenarı: ", c)
################################################
#Soru 2:
#iki kenarı girilen bir dikdörgenin, alanını ve çevresini hesaplayınız.
a = float(input("Kısa kenarı giriniz: ")) #tip dönüşümü
alan = a * b
cevre = 2 * (a + b)
print("Alan: ", alan)
print("Çevre: ", cevre)
################################################
#Soru 3:
#Kullanıcıdan alının sayısal bir değerin 9 ile bölümünden
#kalanını ve bölümünü ekrana yazdırınız.
sayi = int(input(("Bir Sayi: ")))
kalan = sayi % 9
bolum = sayi // 9
print(f'Kalan: {kalan}, Bölüm: {bolum}')
################################################
#Soru 4:
#Girişi yapılan iki basamaklı bir sayının onlar basamağındaki rakamı
#ekrana yazdıran programı yazınız
sayi = int(input(("(AB) Şeklinde Bir Sayi: ")))
birler = sayi % 10
sayi =  sayi - birler
onlar = int(sayi / 10)
print(onlar)
################################################
#Soru 5:
#Girişi yapılan iki basamaklı bir sayının basamak değerleri toplamını
#ekrana yazdıran programı yazınız
sayi = int(input(("(AB) Şeklinde Bir Sayi: ")))
birler = sayi % 10
sayi =  sayi - birler
onlar = int(sayi / 10)
toplam = onlar + birler
print("Basamaklar Toplamı: ", toplam)
################################################
#Soru 6:
#Kullanıcıdan alınan bir karakterin ascii 
# tablosundaki karlığını ekrana yazdırınız
giris = input(("Bir Karakter Giriniz: "))
print(f"{giris}'nın ASCII kod karşılığı {ord(giris)}")
################################################
#Soru 7:
# x ve y koordinatları girilen 
# iki nokta arasındaki mesafeyi hesaplayan programı yazınız.
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x1: "))
y2 = float(input("y2: "))
uzaklik = math.sqrt(math.pow((y2-y1), 2) + math.pow((x2-x1), 2))
print("İki Nokta Arasındaki Mesafe: ", uzaklik)







