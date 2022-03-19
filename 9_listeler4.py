sayilar = [35,26,81,64, 26]
#a: listeyi büyükten küçüğe doğru sıralayın
sayilar.sort()
print(sayilar)
#b: listeyi tersten yazdırın
sayilar.reverse()
print(sayilar)
#c: listede kaç tane 26 elemanı var
y = sayilar.count(26)
print(f'Listede {y} tane 26 var')
#ç: listedeki 81 sayısını siliniz
sayilar.remove(81)
print(sayilar)
#d: listenin tüm elemanlarını siliniz
#sayilar.clear()
#print(sayilar)
#e: 64 elemanının indeksini bulunuz
indeks = sayilar.index(64)
print(indeks)
del sayilar[indeks]
print(sayilar)
#f: listeli ondalıklı sayılar isimli elanmarı, 
# 1.4 ve 6.8 olan liste ile birleştiniz
ondalikli = [1.4, 6.8]
sayilar = sayilar + ondalikli
#sayilar.extend(ondalikli)
print(sayilar)

