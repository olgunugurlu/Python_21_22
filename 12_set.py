#set: küme işlemleri için uygun bir veri türüdür
set_methodlari = list(dir(set))
kullanilacak_metodlar = []
for m in set_methodlari:
    if "__" not in str(m):
        kullanilacak_metodlar.append(m)
print(kullanilacak_metodlar)
# kume = set()
# print(kume)
# kume.add(5)
# kume.add(1)
# print(kume)
# liste = [1,1,1,2,2,2,3,3,3,4,4,4]
# print(liste)
# print(list(set(liste)))
A = set()
B = set()
A.add(1)
A.add(2)
A.add(3)
A.add(4)
A.add(5)

B.add(4)
B.add(5)
B.add(6)
B.add(7)
print("A: ", A)
print("B: ", B)
print("Kesişim Kümesi: ", A.intersection(B))
print("Birleşim Kümesi: ", A.union(B))
print("A fark B: ", A.difference(B))
print("B fark A: ", B.difference(A))

B.remove(7)
B.discard(6)
print(B)
