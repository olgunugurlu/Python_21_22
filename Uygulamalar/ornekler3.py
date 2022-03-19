# sinavlar = {"A": ["s1","s3","s7"],
#             "B":["s2","s3"],
#             "C":["s1","s4","s5","s7"]    ,
#             "D":["s4","s6"],
#             "E":["s1","s2"]
# }
#5 öğnreciye ait sınavlar yukarıda verilmiştir
#haftanın her günü için bir tane sınav planlanmak istenmektedir
#buna göre pazartesi s1, salı s2, çarşamba s3, perşembe s4
#cuma s5, cumartesi s6 ve pazar s7 sınavları yapılacaktır
#günlere göre sınava girecek öğrencilerin listesini oluşturunuz.




liste = [2,1,6,8,5,4,3,2,3,9,3,4,5,2,3,5,6]
#yukarıdaki listede kaç farklı sayı vardır.
sayilar = {2,4,6,8,10}
#liste de kendini tekrar eden sayıları hariç tutarak
#sayılar set'i ile kesişimini ve birleşimini bulunuz
#kesişim kümesini elemanları değiştirilemez bir liste olarak kopyalayınız
liste_set = set(liste)
print("Listenin Eşsiz Elemanları: ", liste_set)
print("Sayılar: ", sayilar)
print("Uzunluk: ", len(liste_set))
birlesim = liste_set.union(sayilar)
kesisim = liste_set.intersection(sayilar)
print("Birleşim: ", birlesim)
print("Kesişim: ", kesisim)











#Bir telefon defteri yapılmak isteniyor
#İletişim kişileri bir sözlük tipinde saklanacaktır.
#key olarak kişi adı soyadı, değer olarak bir liste
#listede numara ve e posta adresi yer alacaktır
#Buna göre isim girişiyle kişinin e posta adresini gösteren
#eğer listede isim yoksa bulunamadı uyarısını veren programı yazınız

# telefon_defteri = {"A": ["50544125485","a@gmail.com"],
#                    "B":["5553624585","b@hotmail.com"],
#                    "C":["5324587896","c@yahoo.com"],
#                    "D":["5465236363","d@hotmail.com"],
#                    "E":["5015698545","e@hotmail.com"]
#                     }

# giris = input("Rehberde Aranacak İsmi Giriniz:")
# isimler = telefon_defteri.keys()
# print(telefon_defteri[giris][1])






#yıllara göre asgari ücret tablosnu sözlük olarak oluşturunuz
#Buna göre en yüksek, en düşük, toplam ve ortalama
#brüt maaş değerlerini ekrana yazdırınız
#açıklama
#max(liste) : liste en büyük
#min(liste) : liste en küçü
#sum(liste) : liste toplamı
#ortalaması
#bir öncek yılar göre bakıldığında
#artış oranı hangi yıllar arasında en büyüktür
yillara_gore_asgari_ucret = {"2016":1647,
                            "2017":1777,
                            "2018":2029,
                            "2019":2558,
                            "2020":2943,
                            "2021":3577,
                            "2022":5004
    }

import math
ucret = list(yillara_gore_asgari_ucret.values())
maksimum = max(ucret)
minimum = min(ucret)
toplam = sum(ucret)
ortalama = toplam / len(ucret)
print("Ucretler:", ucret)
print("Max: ", maksimum)
print("Min: ", minimum)
print("Toplam:", toplam)
print("Ortalama:", math.ceil(ortalama))

#bir öncek yılar göre bakıldığında
#artış oranı hangi yıllar arasında en büyüktür

yillar = list(yillara_gore_asgari_ucret.keys())
print(yillar)
uzunluk = len(yillar)

#a, b, c... olarak gösterilenler yıllara göre ücret
a = yillara_gore_asgari_ucret[yillar[0]] #"2016"
b = yillara_gore_asgari_ucret[yillar[1]]
c = yillara_gore_asgari_ucret[yillar[2]]
d = yillara_gore_asgari_ucret[yillar[3]]
e = yillara_gore_asgari_ucret[yillar[4]]
f = yillara_gore_asgari_ucret[yillar[5]]
g = yillara_gore_asgari_ucret[yillar[6]]

a_b = b / a #2016 - 2017
b_c = c / b #2017 - 2018
c_d = d / c #2018 - 2019
d_e = e / d #2019 - 2020
e_f = f / e #2020 - 2021
f_g = g / f #2021 - 2022
oranlar = dict()
oranlar["2016 - 2017"] = a_b
oranlar["2017 - 2018"] = b_c
oranlar["2018 - 2019"] = c_d
oranlar["2019 - 2020"] = d_e
oranlar["2020 - 2021"] = e_f
oranlar["2021 - 2022"] = f_g
print(oranlar)
print(max(list(oranlar.values())))


