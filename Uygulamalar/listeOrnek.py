
#uygulama
#rastgele üretilmiş 10 ile 20 arasındaki sayılarddan
#5 tanesinden bir liste oluşturunuz

#yine rastgele 0 ile listenin uzunluğu arasında seçilen bir indeks
#değerini listeden çıkartınız

#son olarak 10 ile 20 arasında üretilen 1
# sayının listede kaç tane olduğunu gösteriniz

#rastgele sayı üretebilmemiz için kütphaneyi dosya içine aktardık
import random
#Boş bir liste oluşturduk
liste = []
#rsatgele bir sayı oluşturduk
sayi = random.randint(10, 20)
#bu sayıyı listeye ekledik
liste.append(sayi)
sayi = random.randint(10, 20)
liste.append(sayi)
sayi = random.randint(10, 20)
liste.append(sayi)
sayi = random.randint(10, 20)
liste.append(sayi)
sayi = random.randint(10, 20)
liste.append(sayi)
#listeyi ekrana yazdırdık
print(liste)
#listeden rastgele bir eleman seçmek için
#indeks numaraları aralığı içinde bir rastgele sayı ürettik
index = random.randint(0, len(liste)) #2
print(index)
#listeden indeks ile ilgili değeri okuduk
eleman = liste[index]
#ilgil elemanı listeden sildik
liste.remove(eleman)
print(liste)
sayi = random.randint(10, 20)
print("Tutulan Sayı: ", sayi)
kac_tane = liste.count(sayi)
print(kac_tane)