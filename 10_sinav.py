#%%
# 1.Aşağıdaki değişken değerlerinin tiplerini ekrana yazdırınız
#
sayi = 5	
pi = 3.14	
karakter = 'c'
dogru = True	
ders = "Programlama"
print(type(sayi))
print(type(pi))
print(type(karakter))
print(type(dogru))
print(type(ders))
# %%
# 2.Kenar uzunlukları kullanıcı tarafından girilen
# bir dikdörtgenin alanını ve çevresini hesaplayan
# ve ekranda aşağıdaki gibi gösteren programı 
# python programlama dilinde yazınız. 
# (Değişkenlerinizin isimleri hesaplamalarınıza uygun olsun)
a = float(input("Uzun Kenar: "))
b = float(input("Kısa Kenar: "))
alan = a * b;
cevre = 2 * (a + b)
print(f'Alan: {alan} Çevre: {cevre}')
# %%
# 3. Kenar uzunlukları a ve b şeklinde 
# girilen bir dik üçgenin hipotenüs uzunluğunu 
# bulan ve ekranda aşağıdaki gibi 
# gösteren programı python programlama 
# dilinde yazınız. 
# (Değişkenlerinizin isimleri hesaplamalarınıza uygun olsun)
import math
a = float(input("Uzun Kenar: "))
b = float(input("Kısa Kenar: "))
hipotenus = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(f'Hipotenus: {hipotenus}')
# %%
# 4
import random
sayi = random.randint(10, 100)
kalan = sayi % 11
bolum = sayi // 11
print(f'Sayı: {sayi} Kalan: {kalan} Bölüm: {bolum}')
# %%
# 5
sehirler = ["Ankara", "Bursa","Çanakkale", "Denizli","Eskişehir"]
#a
sehir = input("Şehir: ")
sehirler.append(sehir)
print(sehirler)
sehirler.remove("Ankara")
print(sehirler)
print(len(sehirler))
sehirler.insert(2, "Adana")
print(sehirler)
print(sehirler.index("Denizli"))
print(sehirler[2:4])
print("Eskişehir" in sehirler)
sehirler.pop()
print(sehirler)
yeni_sehirler = []
yeni_sehirler = sehirler[0:2].copy()
print(yeni_sehirler)
sehirler.clear()
print(sehirler)


# %%
