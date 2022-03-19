sozluk_bilim_insani = {"Bilim İnsanı":"Aziz Sancar",
                        "Şair":"Mehmet Akif Ersoy",
                        "Astronom":"Ali Kuşçu",
                        }

#a: kopya_sozluk yap
sozluk_kopya = sozluk_bilim_insani.copy()
#b: değerlerini ekrana yazdır
degerler = list(sozluk_kopya.values())
# degerler = ["Aziz Sancar", "Mehmet Akif Ersoy", "Ali Kuşçu"]
print(degerler[0]) # "Aziz Sancar"
print(degerler.index("Mehmet Akif Ersoy")) # 1
#c: içini boşalt
sozluk_kopya.clear()
#ç: Matematikçi Cahit Arf ekle
sozluk_bilim_insani["Matematikçi"] = "Cahit Arf" #new key value->yeni anahtar değer çifti
print(sozluk_bilim_insani)
#d: İçinde "Sanatçı" anahtar var mı yok mu?
kontrol = "Sanatçi" in tuple(sozluk_bilim_insani.keys())
print(kontrol)
#e: Bilim İnsani anahtarını Canan Dağdeviren yapınız
sozluk_bilim_insani["Bilim İnsanı"] = "Canan Dağdeviren" #update: güncelleme
#f: "Şair" anahtarlı değeri yazdırınız
print(sozluk_bilim_insani["Şair"])
#print(dir(dict()))