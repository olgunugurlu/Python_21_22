# #listeler

# #listeler
# #bir değişken sadece bir değer tutabilir
# #bir liste birden çok değer alabilir
# #farklı veri türünde değerleri tutabilir
# #listenin kendine metotları vardır
# #ogrenci_notlari = []
# ogrenci_notlari = list() #boş liste
# print(ogrenci_notlari)
# #print(dir(ogrenci_notlari))
# #ön tanımlı liste
# ogrenci_notlari = [50, 65, 75, 80, 90]
# print(ogrenci_notlari)
# #listeye eleman ekleme
# ogrenci_notlari.append(100)
# print(ogrenci_notlari)

# #liste oluşturma 
# #karakter dizilerinden oluşan bir liste örneği
# meyveler = ["elma","armut","vişne","muz","erik"]
# #karakter listesi örneği
# sesli_harfler = ['a','e','ı','i','o','ö', 'u', 'ü']
# #liste içinde liste
# liste = [[1,2,3],[3,4,5],[5,6,7]]
# #farklı veri türlerinden oluşturulmuş liste
# farkli_veri_turleri = ["isim", 65, 56.7]

# ####################### Metotlar #####################
# #len, append, count, extend, index, insert, pop, 
# # remove, reverse, sort, clear, in
# ######################################################
# print("###############################################")
# import random 
# sayilar = []

# # for i in range(10):
# #     sayi = random.randint(5, 10)
# #     sayilar.append(sayi)

# #listeye eleman ekleme
# sayilar.append(5) 
# sayilar.append(15)
# sayilar.append(5)
# sayilar.append(25)
# sayilar.append(35)
# #indeks numarası 0 dan başlar
# print(sayilar[0])
# print(sayilar[1])
# print(sayilar[2])
# print(sayilar[3])
# print(sayilar[4])
# print(sayilar)
# #liste elemanının değerini değiştirme
# #burada sıfır indeks numarsını gösterir
# sayilar[0] = 45
# print(sayilar)

# # liste uzunluğu
# uzunluk = len(sayilar) #length in kısaltması
# print(f'Liste Uzunluğu: ', uzunluk)
# #listenin son elemanını uzunluk değerine göre yazdırma
# print(sayilar[uzunluk-1])

# #listeki belirli bir elemanın kaç tane olduğunu verir
# print(sayilar.count(5))

# #Problem:
# 5 tane farklı ülkeden oluşan bir liste oluşturunuz
#listeyi yaparken append komutunu kullanınız
# listenin 3. elemanını ikinci elemanı ile değiştiriniz
# değiştirdiğiniz elemanın sayısınu ekranda yazdırınız.

# ulkeler = ["Türkiye"]
# ulkeler.append("Almanya")
# ulkeler.append("Fransa")
# ulkeler.append("İngiltere")
# ulkeler.append("İspanya")
# print(ulkeler)
# ulkeler[3] = ulkeler[2]
# print(ulkeler)
# fransa = ulkeler.count("Fransa")
# print(f'Fransa Sayısı: {fransa}')
# #print("Fransa Sayısı:", fransa)

# #araya eleman ekleme
# ulkeler.insert(index, object)

#araya eleman ekleme
liste = [5,10,15]
print(liste)
liste.insert(1, 25)
print(liste)
liste.insert(2, 30)
print(liste)
liste.append(10)

#listeden eleman çıkarma
liste.remove(30) #listedeki bir değer yazılır
print(liste)

#listedeki bir elemanın indeks numarasını bulme
#listede aynı değerde iki veya daha fazla eleman varsa 
#onun indeks değeri döner
index = liste.index(10)
# print(index)

#Uygulama
#python harflerinden oluşan bir liste yapınız
#listeye dili harflerini bir karakterlik boşluktan sonra ekleyiniz
#listede kaç tane i harfi olduğunu ekranda yazdırınız
#n harfinin indeks değerini ekranda yazdırınız
#listenin 3. ve 5. harfini ekranda yazdırınız
#listeden python harflerini sildiriniz
#listenin ilk indeksinde itibaren c# karakterlerini ekleyiniz(insert)
# liste2 = []
# liste2.append('p')
liste2 = ['p','y','t','h','o','n']
liste2.append(' ')
liste2.append('d')
liste2.append('i')
liste2.append('l')
liste2.append('i')
i_harf_sayisi = liste2.count('i')
print(f"i sayısı: {i_harf_sayisi}")
index_n = liste2.index('n')
print(f'n harfinin indeksi: {index_n}')
print(liste2[3], liste2[5])
liste2.remove('p')
liste2.remove('y')
liste2.remove('t')
liste2.remove('h')
liste2.remove('o')
liste2.remove('n')
print(liste2)
liste2.insert(0, '#')
liste2.insert(0, 'C')
print(liste2)

# for i, k in enumerate(liste):
#     print(i , k)

liste = []
#kullanıcıdan bir giriş alınız
giris = input("Bir Karakter Giriniz: ")
#listeye kullanıcının girdiği değeri ekleyiniz
liste.append(giris)
print(liste)
while giris != 'x': 
    #kullanıcıdan bir giriş alınız
    giris = input("Bir Karakter Giriniz: ")
    #listeye kullanıcının girdiği değeri ekleyiniz
    liste.append(giris)
    #listeyi yazdırınız
    print(liste)
print(liste)

