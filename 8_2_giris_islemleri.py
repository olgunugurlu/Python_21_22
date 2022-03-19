# #string'den dönüştürme
# #string: karakter dizisi türünde
# ad_soyad = input("Adınızı Giriniz: ")
# print(ad_soyad, type(ad_soyad))
# #tam sayı dönüşümü
# sayi = int(input("Bir Sayı Giriniz: "))
# print(sayi, type(sayi))
# #ondalıklı sayı dönüşümü
# derece = float(input("Bir Derece Giriniz: "))
# print(derece, type(derece))

# #float, int vs veri türünden string'e dönüştür
# pi = 3.14
# donusum = str(pi)
# print(type(donusum))
# #soldaki string verisi ile sağdaki sayılsal veri birlşetirilemez
# #bunu düzeltmek için sayısal veri str ile string veri türüne dönüştürüldü
# print("Pi Değeri: " + str(pi))
#%%
#Soru: yarıçapı girilen bir dairenin, alanı ve çevresini hesaplayınız.
# alan = pi * r^2
# cevre = 2 * pi * r
import math
yaricap = float(input("Yarıçap Giriniz: "))
pi = 3.14
alan = pi * math.pow(yaricap, 2) 
cevre = 2 * pi * yaricap
print(f"Alan: {alan} Çevre: {cevre}")
#%%
#Soru: Yüksekliği ve taban uzunluğu girilen dik üçgenin alanını hesaplayınız.
yukseklik = float(input("Yüksekliği Giriniz: "))
taban_uzunlugu = float(input("Taban Uzunluğu: "))
ucgenin_alani = (yukseklik * taban_uzunlugu) / 2
print("Alan: ", ucgenin_alani)

#Soru: Kenar uzunluğu girilen kübün hacmini hesaplayınız
kenar = float(input("Kübün Kenar Uzunluğunu Giriniz: "))
hacim = math.pow(kenar, 3) #kenar * kenar * kenar
print("Hacim {} m3".format(hacim))

#%%
#Soru 1.sınav 2.sınav ve performans notu girilen bir öğrenciye ait;
#1. sınavın %20 si
#2. sınavın %50 si
#performans notunun %30'una göre ortalaması hesaplanmak istenmektedir
#gerekli programı yazınız.
sinav1 = int(input("1.Sınav Notu: "))
sinav2 = int(input("2.Sınav Notu: "))
performans = int(input("Performans Notu: "))

sinav1 *=  0.2
sinav2 *= 0.5
performans *= 0.3
toplam = sinav1 + sinav2 + performans
print("Ortalama: ", toplam)

# %%
# x = 5
# y = x
# print(x is y)
# print(x == y)
# print(hex(id(x)))
# print(hex(id(y)))
# #x = 7
# y = 6
# print(x is y)
# print(x == y)
# print(hex(id(x)))
# print(hex(id(y)))


# %%
