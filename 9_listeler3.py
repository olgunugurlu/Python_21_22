liste = [2,4,6,8,10,12,14,16,18]

#listeden eleman seçme
print(liste[:2]) #0. index 1. index
#arkaya doğru seçim
print(liste[5:]) #5. ..... son indeks
#aralık seçimi
print(liste[4:6]) # 4. 5. 
#atlamalı seçim
print(liste[1:6:2])
#tersten eleman seçme
print(liste[-1])
#tersten aralık seçme
print(liste[-3:-1])
#tersten atlamalı seçim
print(liste[-5:-1:2])
#eleman karşılaştırma
print(liste[len(liste)-1] == liste[-1])
#eleman listede var mı yok mu?
sonuc = 2 in liste
print(sonuc)
#iç içe listeler

