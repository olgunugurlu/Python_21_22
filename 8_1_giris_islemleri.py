#giriş işlemleri
#not1 = 100
#not2 = 90

not1 = input() #50 #açıklama metinin muhakkak giriniz
print(type(not1))
#input fonksiyonu kullanıcıdan veri almak için kullanılır
#input fonksiyonu içine yazılan açıklama değişkenle ilgili bir açıklamadır
not2 = input("İkinci Not Giriniz: ") #70
not3 = input("Üçüncü Not Giriniz: ") #100
print(not1 + not2 + not3) #sonuç -> 5070100
###input ile aldığımız değişkenler string veri türündedir

#Tip Dönüşümü
#string den tamsayıya dönüşüm
sayi = input("Bir Sayı Giriniz: ")
print(sayi, type(sayi), sep="-")
sayi = int(sayi)
print(sayi, type(sayi), sep="-")
#bu şekilde de yapılabilir
sayi = int(input("Bir Sayı Giriniz: "))
