import random
kisiler = ["Meysun", "Mana","Murat","Medine","Ela","Ahmet"]

sorular = [
    "Kenar uzunlukları verilen bir dik üçgenin Hipotenüs uzunluğunu hesaplayınız.",
    "iki kenarı girilen bir dikdörgenin, alanını ve çevresini hesaplayınız.",
    "Kullanıcıdan alının sayısal bir değerin 9 ile bölümünden kalanını ve bölümünü ekrana yazdırınız.",
    "Girişi yapılan iki basamaklı bir sayının onlar basamağındaki rakamı ekrana yazdıran programı yazınız",
    "Girişi yapılan iki basamaklı bir sayının basamak değerleri toplamını ekrana yazdıran programı yazınız",
    "Kullanıcıdan alınan bir karakterin ascii tablosundaki karlığını ekrana yazdırınız",
    "x ve y koordinatları girilen iki nokta arasındaki mesafeyi hesaplayan programı yazınız.",
    "Bir kenarı girilen küpün yüzey alanı ve hacmini bulunuz.",
    "Yarıçap ve yüksekliği girlen silindirin yüzey alanı ve hacmini bulunuz."
    "Yarıçap ve yüksekliği ve tepe açısı girilen koninin yüzey alanı ve hacmini bulunuz.",
    "Kenar uzunlukları kullanıcı tarafından girilen bir dikdörtgenin alanını ve çevresini hesaplayan",
    "Kenar uzunlukları a ve b şeklinde girilen bir dik üçgenin hipotenüs uzunluğunu bulan ve ekranda aşağıdaki gibi gösteren programı python programlama dilinde yazınız. ",
    "Rastgele üretilen birs ayının 9 ve 4'e bölümünde kalan sayıyı yazdırınz.",
    "Ekrana girilen ad ve soyad değişkenlerini birleştirerek ekranda birleşik olarak yazdırınz."    ,
    "x ve y koordinatları girilen üç nokta arasında kalan alanı hesaplayınız."
    ]

def soru_secim(k, k_soru):
    # sinav_soru_secim = []
    #print("Uzunluk: ", len(sorular))
    #kisi soruları
    for i in range(0, 8, 1):
        secim = random.choice(sorular)
        if secim not in k_soru:
            k_soru.append(secim)
    #print(k)
    for y in range(0, len(kisiler), 1):
        print(kisi_soru[y])




# kisi_soru = []
for k in range(0, len(kisiler), 1):
    kisi_soru = []
    kisi = random.choice(kisiler)
    if kisi not in kisi_soru:
        kisi_soru.append(kisi)
        soru_secim(kisi, kisi_soru)
    else:
        continue

