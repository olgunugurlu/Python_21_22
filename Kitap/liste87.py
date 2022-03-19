ders = ['B','İ','L','İ','Ş','İ','M']
ders_copy = ders.copy()
print(ders)
#a
ders_copy.sort()
print(ders)
#b
ders_copy = ders_copy.copy()
ders_copy.reverse()
print(ders_copy)
#c
kac_tane_i = ders_copy.count('İ')
print(kac_tane_i)
#ç
#bilişim
#ş ve i yi sil
del ders[4]
del ders[4]
print(ders)
#d
alan = ders.copy()
print(alan)
#e
ders.clear()
print(ders)
#f
index = ders_copy.index('L')
print(index)