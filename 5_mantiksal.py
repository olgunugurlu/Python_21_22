#and or not
#iki ya da daha fazla değişkenin karşılaştırılması
sayi1 = 5
sayi2 = 7
sayi3 = 8
print(sayi1 < sayi2 and sayi2 > sayi3)
#a b And(ve)
#0 0 0
#0 1 0 
#1 0 0
#1 1 1
#
print(sayi1 < sayi2 or sayi2 > sayi3)
#a b Or(veya)
#0 0 0
#0 1 1 
#1 0 1
#1 1 1
#
print(not(sayi1 < sayi2) and not(sayi2 > sayi3))
#a not 
#0 1
#1 0


#Bit Düzeyinde Mantıksal İşlemler
#Bir tam sayı için mantıksal olarak &, |, ^, ~ <<, >> işlemlerine uygulayınız
sayi = int(input("Bir sayi giriniz: "))
#örnek 5 için:
#5 binary olarak 0101 dir
#0101 & 1 -> 0101 olur
print("Mantıksal VE: ", sayi & 1) #  
print("Mantıksal VEYA: ", sayi | 1) #  
print("Mantıksal XOR: ", sayi ^ 1) # 
print("Mantıksal XOR: ", sayi & ~1 | ~sayi & 1)
print("Bir Bit Sağa Kaydır: ", sayi >> 1)
print("Bir Bit Sola Kaydır: ", sayi << 1)
print("Değili: ", ~sayi)
