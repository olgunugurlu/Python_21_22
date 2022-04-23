#Bir liste sayı içindeki çift sayıların toplamını bulunuz



#Girişi yapılan string bir ifadenin listeye dönüştürülerek şifrelenemesi istenmektedir.
#Buna göre;
#şifre normal harf düzeninin tersine göre yapılmalıdır.
#örnek
#giris = ["A","L","İ"] -> A alfabede 1. harf ise, alfabedeki Z olarak temsil edilir.

import string

harfler = string.ascii_lowercase;
# print(harfler)
giris = list(input("Şifrelenecek Kelime Giriniz: ").lower())
print(giris)
harfler_uzunluk = len(harfler)
giris_index = []
giris_ters_index = []
for i in giris:
    giris_index.append(harfler.index(i))
    giris_ters_index.append(harfler_uzunluk - harfler.index(i) - 1)
print(giris_index, giris_ters_index)
sifreli = ""
for k in giris_ters_index:
    sifreli += harfler[k]
print(harfler)
print(sifreli)
