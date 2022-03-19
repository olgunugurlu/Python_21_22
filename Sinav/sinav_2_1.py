######################111111111111111111111111111########################### 6 - 24
bilet_fiyat = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71,
    "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, 
    "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, 
    "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, 
    "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, 
    "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, 
    "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, 
    "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, 
    "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8
}

#yukarıda bir bilet firmasına ait bilet_fiyat adında sözlük olarak tanımlanmış bir veri bulunmaktadır.
#Bu veri setinde key(anahtar) yapılar string tipinde bilet kodunu gösterirken, value(değer) tipindekiler
#biletin fiyatını göstermektedir.
#Buna göre ;
#Anahtarı "87-430" ve değeri 40 olan yeni bir bilet anahtar-değer yapısını bilet_fiyat'a ekleyiniz
bilet_fiyat["87-430"] = 40
#Biletlerin toplam fiyatını hesaplayınız
toplam = sum(list(bilet_fiyat.values()))
#bilet_fiyat sözlük yapısında kaç tane bilet tanımlanmıştır?
uzunluk = len(list(bilet_fiyat.values()))
#Biletlerin ortalama fiyatını bulunuz
ortalama = toplam / uzunluk
print(f"Adet: {uzunluk } Toplam: { toplam} Ortalama: {ortalama} ")
#bilet_fiyat sözlük yapısında farklı olan kaç tane fiyat değeri vardır
farkli = len(set(bilet_fiyat.values()))
print(f"Farkli: {farkli}")
#"13-111" bilet numaralı yolcunun bilet fiyatı 21 lira olarak yanlış girilmiştir. Değeri 15 lira olarak güncelleyiniz.
bilet_fiyat["13-111"] = 15
######################222222222222222222222222########################### 12 - 36
sehirler = ["Ankara","İstanbul","İzmir","Eskişehir","Antalya"]
print(sehirler)
#Yukarıda şehirler adında bir liste tanımlanmıştır
#Kullancının girdiği bir şehri eğer listede yoksa listeye ekleyiniz. (Örn: Adana ya da İzmir)
sehir = input("Bir Şehir Giriniz: ")
if sehir not in sehirler:
    sehirler.append(sehir)
#Listeyi yazdırınız
print(sehirler)
#Listeyi isim listesine göre tersten sıralayınız
sehirler.sort()
sehirler.reverse()
#Listeyi yazdırınız
print(sehirler)
#Listeden i ve e ile başlayan şehirleri siliniz
sehirler.remove("İzmir")
sehirler.remove("İstanbul")
sehirler.remove("Eskişehir")
#Listeyi yazdırınız
print(sehirler)
#Listeye Ankaradan sonra Afyokkarahisar'ı ekleyiniz
sehirler.insert(2, "Afyokkarahisar")
#Listeyi yazdırınız
print(sehirler)
#Ankara şehrinin indeks numarasını bulunuz
indeks = sehirler.index("Ankara")
print(f"Ankara'nın indeksi:{indeks}")
#Bulunan indeks numarsına göre Ankara şehrini listeden siliniz
del sehirler[indeks]
#Listeyi yazdırınız
print(sehirler)
sehirler2= ["Balıkesir","Bursa","Bilecik"]
#sehirler iki listesi ile sehirler listesini sehirler listesinde birleştiriniz
sehirler.extend(sehirler2)
#Listeyi yazdırınız
print(sehirler)
#sehirler_son adli bir listeye sehirler'in kopyasını alarak sehirler listesinin içindekileri siliniz
sehirler_son = sehirler.copy()
#sehirler_son listesini yazdırınız
print(sehirler_son)
sehirler.clear()
#sehirler listsini yazdırınız
print(sehirler)
######################3333333333333333333333333333333########################### 4 - 20
#İnsanlar için en uygun günlük nem oranı %40 - %60 arasında değişmektedir. Aralıklar dahil.
#Bir nem ölçer tarafınfan alınan değere göre girilen değer
#Uygun aralıkta ise normal, düşükse düşük nem, yüksekse yüksek nem yazdıran programı yazınız

nem = int(input("Nem Oranı (%): "))
if nem >= 40 and nem <= 60:
    print("Normal Nem")
elif nem < 40:
    print("Düşük Nem ")
else:
    print("Yüksek Nem")

######################44444444444444444444444444444########################### 3 - 20
#Bir okuldaki sınavlarla ilgili aşağıdaki kümeler verilmiştir
#Matematik dersini alan öğrenclier
matematik = {"Ahmet","Ayşe","Filiz","Kemal","Zeynep","Arat"}
#Fen Bilgisi dersini alanlar
fen_bilgisi = {"Ayşe","Hürriyet","Arat","Sevim","Fazilet"}
#İngilizce dersini alanlar
ingilizce = {"Hürriyet","Kemal"}
#Buna göre;
#İsme göre toplam öğrenci sayısı kaçtır
toplam_ogrenci = len(matematik.union(fen_bilgisi).union(ingilizce))
print(toplam_ogrenci)
#Sadece fen bilgisi dersini alanlar kimlerdir
sadece_fen = fen_bilgisi.difference(matematik).difference(ingilizce)
print(sadece_fen)
#sadece ingilizce ve fen bilgisi derslerini alanlar kimlerdir
ing_fen = fen_bilgisi.intersection(ingilizce)
print(ing_fen)


