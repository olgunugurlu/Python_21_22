sayi1 = 5
sayi2 = 10
print("sayi1", sayi1)
print("sayi2", sayi2)
#değişkenin bellekteki adresi 10'luk tabanda
print("sayi1 ID", id(sayi1))
print("sayi2 ID", id(sayi2))
#değişkenin bellekteki adresi 16'lık tabanda
print("sayi1 ID", hex(id(sayi1)))
print("sayi2 ID", hex(id(sayi2)))
sayi3 = sayi2
print("sayi1", sayi1)
print("sayi2", sayi2)
print("sayi3", sayi3)
print("sayi2 ID", id(sayi2))
print("sayi3 ID", id(sayi3))
print("sayi2 ID", hex(id(sayi2)))
print("sayi3 ID", hex(id(sayi3)))
sayi4 = 5
print("sayi4", sayi4)
print("sayi4 ID", id(sayi4))
print("sayi4 ID", hex(id(sayi4)))
print(sayi3 is sayi2)
print(sayi4 == sayi1)
sayi2 = 6
print("sayi1", sayi1)
print("sayi2", sayi2)
print("sayi3", sayi3)
print("sayi4", sayi4)
print(sayi3 is sayi2)
print(sayi4 == sayi1)

#dir




#help