# # # #karar yapıları
# # # #karşılaştırma operatörleri
# # # print(5 == 5)
# # # print("Bilişim" != "Teknolojileri")
# # # print(4 < 8 and 3 > 7)
# # # print(3 >= 7 or "a" != "b")
# # # #koşullu ifadeler
# # # #if (koşul):
# # #   #çalışacak kodlar

# yas = 20
# if yas >= 18:
#   print("Ehliyet Alabilirsin.")
  
# # print("Program sonlandı!")

# # a = 5
# # b = 7
# # if a > b and b > 8:
# #   print(a)
# # else:
# #   print(b)

# yas = int(input("Yaşınızı Giriniz:"))
# # print(type(yas))
# if yas >= 18:
#     print("Ehliyet Alabilirsiniz")
# else:
#     #pass
#     print("Ehliyet Alamazdınız")

# #######################
# #girilen bir sayınını çift olup olmadığını kontrol ediniz
# sayi = int(input("Bir Sayı Giriniz: "))
# if sayi % 2 == 0:
#     print(f"{sayi} çift sayıdır")
# else:
#     print(f"{sayi} tek sayıdır")

# #######################
# ogrenci_not = int(input("Not Giriniz(0-100):")) #55
# if ogrenci_not < 50:
#     print("Başarısız")
# elif ogrenci_not >= 50 and ogrenci_not < 70:
#     print("Başarılı")
# else:
#     print("Çok Başarılı")

# #Burası her trlü çalışır
# print("Program sonlandı")


#Kullanıcının girdiği iki ürünün toplam fiyatı 200 tl ve 
#altı ise ödenecek miktar ... tl, 200 tl 'yi geçerse, %25 indirimle
#ödenecek miktar .. tl şeklinde çıktı veren programı yazınız

# urun_adet1 = int(input("1. Ürünün Adetini Giriniz: "))
# urun_fiyat1 = int(input("1. Ürünün Fiyatını Giriniz: "))
# urun_adet2 = int(input("2. Ürünün Adetini Giriniz: "))
# urun_fiyat2 = int(input("2. Ürünün Fiyatını Giriniz: "))
# toplam = urun_adet1 * urun_fiyat1 + urun_adet2 * urun_fiyat2
# #toplam 1500
# if (toplam > 1000) :
#     #doğruysa
#     indirim = toplam * 0.25
#     toplam = toplam - indirim
#     print("Bu Alışverişten karınız: ", indirim)
#     print("Ürünlerin Toplam Fiyatı: ", toplam)
# else:
#     #yanlışsa
#     print("Ürünlerin Toplam Fiyatı: ", toplam)

#Kullanıcının girdiği ay değerine (1-12) göre;
#yaz aylarında çıktı yaz olsun
#kış aylarında çıktı kış
#ilkbahar aylarında çıktı ilkbahar
#sonbahar aylarında çıktı sonbahar
#örnek: 2 -> Şubat -> Kış
# ay = int(input("Bir Ay Giriniz (1-12):"))
# if (ay == 12 or ay == 1 or ay == 2):
#     print("Mevsim Kış")
# elif (ay == 3 or ay == 4 or ay == 5):
#     print("Mevsim İlkbahar")
# elif (ay == 6 or ay == 7 or ay == 8):
#     print("Mevsim Yaz")
# elif (ay == 9 or ay == 10 or ay == 11):
#     print("Mevsim Sonbahar")
# else:
#     print("Yanlış bir değer girdiniz.")

# if (ay == 1):
#     print("Mevsim Kıs")
# elif (ay == 2):
#     print("Mevsim Kış")


#bir öğrencinin notuna göre
#0 - 50 arasında  zayıf
#50 - 55 arası geçer
#55 - 70 arası orta
#70 - 85 arası iyi
#85 - 100 çok iyi

# ogrenci_notu = int(input("Öğrencinin Notunu Giriniz: "))
# if (ogrenci_notu >= 0 and ogrenci_notu < 50):
#     print("Zayıf")
# elif (ogrenci_notu >= 50 and ogrenci_notu < 55):
#     print("Geçer")
# elif (ogrenci_notu >= 55 and ogrenci_notu < 70):
#     print("Orta")
# elif (ogrenci_notu >= 70 and ogrenci_notu < 85):
#     print("iyi")
# elif (ogrenci_notu >= 85 and ogrenci_notu <= 100):
#     print("Çok iyi")
# else:
#     print("Yanlış Bir Not Girdiniz!")


#sıcaklık değerine göre
#sıcaklık 10 derecenin altındaysa soğuk
# 10 - 20 derece arasındaysa ılık
# 20 - 30 derece arasında sıcak
# 30 dan büyükse çok sıcak
# 0' dan küçükse çok soğuk çıktısını üreten programı yazınız.


#kullanıcının girdiği beş sayıyı bir listeye alınız
#listenin ortalaması çift ise ekranda çift
#tek ise ekranda tek yazsın


#bir öğrenciye ait vize ve final notları giriliyor
#Buna göre vizenin %40' ve finalin %60'ı ile hesaplanan ortalamaya göre
#öğrencinin ortalaması 50'nin altındaysa bütünleme sınav girişi istenmekte
#yeni girilen bütünleme nnotuna göre hesaplanan ortalama 60'ın altındaysa öğrenci kaldı
#üstündeyse geçti durumunda yazılacaktır
#şayet vize ve final ortalaması 50 nin üstündeyse öğrenci geçti diye ekranda yazdırılacaktır


#ödev
dersler = ["Matematik","ingilizce"]
#yukarıdaki liste içine 5 adet ders daha giriniz
#dersler birbirinden farklı olsun
#listeyi set e dönüştürünüz ve ekranda ikisini de yazdırınızs
#Bilgi: için ders dersler listesinde var mı yok mu kontrolü yaparak
#girişlerinizi yapınız (in)

print("Matematik" in dersler)
