###veri türleri
###tam sayı bir değişken
##sayi = 5
###ondalıklı bir değişken
##derece = 3.14
###karakter dizisi (string): birden çok karakterden oluşur
##kullanici_adi = "ou@g.c"
###karakter tipinde char: tek karakterden oluşur
##karakter = 'a'
###boolean veri tipi true - false
##dogruMu = False
##print(sayi)
##print(derece)
##print(kullanici_adi)
##print(karakter)
##print(dogruMu)
###type komutu ile değişkenin tipini öğrenebiliriz
##print(type(sayi))
##print(type(derece))
##print(type(kullanici_adi))
##print(type(karakter))
##print(type(dogruMu))
###dir
###dir komutu herhangi bir sınıfla ilgili metotları listeleriz
##import random
##print(dir(random))
##print("******************")
###help, modullere ait fonksiyonların nasıl çalıştığını gösterir
##print(help(random.randint))
##
###char to int
##print(ord(karakter))
##print("Veri Türleri - 2")
##
###sayısal işlemler
##not1 = 100
##not2 = 90
##not3 = 25
##toplam = not1 + not2 + not3
##ortalama = toplam / 3
##print(not1, not2, not3, toplam)
##print(type(not1), type(not2), type(not3), type(toplam))
##print("Ortalama:", ortalama)
##print("Ortalama Tip:", type(ortalama))

#string işlemleri
isim = "ahmet"
soyisim = "veli"
#artı operatörü ile iki veya daha fazla string ifadesi birleştirilebilir
#concatenate: birleştirme
print(isim + soyisim)
ad_soyad = isim + " " + soyisim
print(ad_soyad)
print(type(ad_soyad))
#karakterleri çoğaltmak için çarpma kullanılır
karakter = 'ahmet '
print(karakter  * 5)


#string kütüphanesi ile alfabedeki harfleri string olarak alabiliriz
import string
print(dir(string))
buyuk_harfler = string.ascii_uppercase
print(buyuk_harfler)
sayilar = string.digits
print(sayilar)
kucuk_harfler = string.ascii_lowercase
print(kucuk_harfler)
############################
sesli_harfler = "aeıioöuü"
cumle = "bugün günlerden çarşamba"
############################














