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
print(liste[:7])
print(liste[3:7])
print(liste[2:8:2])
#Son eleman
print(liste[-1:])
# %%
