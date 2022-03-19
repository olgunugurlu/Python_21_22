#tuple: demetler sadece okunabilir ver yapılarıdır
#eleman ekleme değiştirme işlemi yapılamaz
t2 = (2,4,6,8)
print(t2)
print(t2[2])
print(dir(tuple))
demet = ("bilişim","teknolojileri",1)
print(type(demet))
print(demet)
print(demet[2])
print(demet.index("teknolojileri"))
print(demet.count(1))
######error
# demet[1] = "Sistemleri"
print(demet)
#eleman var mı
kontrol = 1 in demet #true or false
uzunluk = len(demet) #tamsayı bir değer döner
demet2 = (2,3,4)
birlesim = demet + demet2
print(birlesim)
print(dir(demet))
