#listeler
#farklı veri türünde birden çok değer alabilen yapılara listeler denir
#listeler dinamik yapıdadırlar
#liste elemanları 0. indeks numarası ile başlar
#%%
#boş bir liste oluşturma
bos_liste1 = []
bos_liste2 = list()
#liste metodlarını gösterir
print(dir(bos_liste1))
#%%
#listeyi yazdırma
print(bos_liste1)

# %%
#Eleman ekleme
liste = ["Elma"]
liste.append("Armut")
liste.append("Armut")
liste.append("Muz")
liste.append("Karpuz")
liste.append("Çilek")
liste.append("Vişne")
liste.append("Kiraz")
#liste uzunluğu
uzunluk = len(liste)
print(f"Uzunluk: {uzunluk}")
#liste
armut_sayisi = liste.count("Armut")
print(f"Armut Sayısı: {armut_sayisi}")

# %%
#Listede seçim yapma
#baştan belli bir değere kadar
print(liste[:7])
#belirli bir aralık
print(liste[3:7])
#belirli bir aralıklı ve adımlamalı
print(liste[2:8:2])
#Son eleman
print(liste[-1:])
# %%
#Araya eleman ekleme
#istenen indeks numarasına eleman ekler sonrasını bir öteler
liste.insert(0, "Mango")
print(liste)
# %%
#listeden eleman silme
liste.remove("Armut")
print(liste)

#listenin son elemanını silme ve silineni yazdırma
liste.pop()
# %%
#listeyi sıralama
liste.sort()
print(liste)
# %%
#listeyi ters çevirme
liste.reverse()
print(liste)
# %%
#listeyi birleştirme
liste2 = [2,4,6]
# liste = liste + liste2
# print(liste)
liste.extend(liste2)
print(liste)

# %%
#listeyi temizleme
liste.clear()
print(liste)
# %%
#listede eleman var mı?
sonuc = "Armut" in liste
print(sonuc)
sonuc  = liste.__contains__("Armut")
print(sonuc)
# %%
#liste kopyalama
yeni_liste = list()
yeni_liste = liste.copy()
yeni_liste2 = yeni_liste
print(id(yeni_liste))
print(id(yeni_liste2))
yeni_liste2.append("Meyve")
print(id(liste))
print(yeni_liste)
# print(yeni_liste)
# %%
