tek = [5,7,9,11,13,15]
cift = [6,8,10,12,14,16]
#a: tek ve çift sayılardan iç içe liste oluşturunuz
liste = [tek, cift]
print(liste)
#b: ekran çıktısı olarak 7 14 üreten kodu yazınız
print(liste[0][1])
print(liste[1][4])
#c: ekrana sırasıyla çift sayılar listesinden 10 ve 12;
#tek sayılar listesinden 13 yazdırınız
print(liste[1][2:4])
print(liste[0][4])
#d: cift sayılar listesine 18 ekleyiniz
print(type(liste[1]))
liste[1].append(18)
print(liste)
liste[0].insert(3, 10)
print(type(liste[0][0]))
print(liste)
#e: tek sayılar listesinden 5'i siliniz
liste[0].remove(5)
print(liste)


