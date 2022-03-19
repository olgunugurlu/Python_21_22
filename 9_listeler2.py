# y = []
# y.append("armut") #0
# y.append("muz") #1
# y.append("karpuz") #2
# y.append("muz")
# print("Listenin Uzunluğu: " , len(y))
# print("y'nin 0. indeksinde ne var? ", y[0])
# print("Listedeki Muz Sayısı:", y.count("muz"))
# print("###########")
# #print(y)
# #y.remove("muz")
# print(y)
# print(y.index("muz"))
# y.insert(1, "elma")
# print(y)
# z = ["kiraz", "vişne"]
# #iki listeyi birleştirme
# #y.extend(z)
# #iki listeyi birleştirme
# y = y + z
# print(y)
# liste1 = [2,4,6,8]
# liste2 = [2,6,7,8]
# katsayi = 2
# #print(liste1)
# liste1 = liste1 + liste2
# print(liste1)
# ###############################
# import random
# sayilar = []
# for i in range(10):
#     sayi = random.randint(10,100)
#     sayilar.append(sayi)

# print(sayilar)
# #listeyi küçükten büyüğe sıralama
# sayilar.sort()
# print(sayilar)
# #listeyi ters sıralar
# sayilar.reverse()
# print(sayilar)
# #listenin son elemanını siler
# sayilar.pop()
# print(sayilar)
# #listenin içeriğini temizler
# #sayilar.clear()
# print(sayilar)
# #listenin 0. indeksini yazdırır
# print(sayilar[0])
# #listenin 0. indeksinin değerini değiştirir
# sayilar[0] = 92
# print(sayilar)

# #indeksi verilen elemanı siler
# index = 2
# del sayilar[index]

##copy işlemi##################
bos_liste = []
dolu_liste = [1,3,5,7]
#dolu listenin kopyasını boş listeye aktar
bos_liste = dolu_liste.copy()

print(bos_liste)
print(bos_liste == dolu_liste)
print(bos_liste is dolu_liste)
print(id(bos_liste))
print(id(dolu_liste))

bos_liste2 = []
dolu_liste2 = [2,4,6,8]
bos_liste2 = dolu_liste2
print(bos_liste2 == dolu_liste2)
print(bos_liste2 is dolu_liste2)
print(id(bos_liste2))
print(id(dolu_liste2))

#remove - object, del -> index silme