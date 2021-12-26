#Operatörler
#+ * - / ** // %
sayi1 = 10 
sayi2 = 7
sayi1 = 18
toplama = sayi1 + sayi2
cikarma = sayi1 - sayi2
carpma = sayi1 * sayi2
bolme = sayi1 / sayi2
kalan = sayi1 % sayi2
bolum = sayi1 // sayi2
kuvvet = sayi1 ** sayi2
print("Toplam: {} Çıkarma {}".format(toplama, cikarma))
print("Çarpma: " + str(carpma))
print(f"Bölme: {bolme}")
#sep: seperator-ayırıcı
print("Bölmede Kalan", kalan, "Bölmede Bölüm", bolum, sep="|")
print("Kuvvet", kuvvet)
print("İşlem1: ", (4-1)**2)
print("********************")
ad = "murat"
soyad = "erşahin"
skor = 100
print("Ad: %(a)s Skor: %(s)s" % {'a': ad, 's': skor})

#print fonksiyonu yanındaki parantez içine gelen değerlere
#parametre denir
#tırna içindeki ifadeler örnek "abc" string ifadelerdir
# diğer adı karakter dizisidir

#işlem önceliği (2+3)**2 , (2**3+5)**2, (2+5**2)
# 1 üst alma, parantez içi
# 2 çarpma bölme
# 3 toplama çıkarma



