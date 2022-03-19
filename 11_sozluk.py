#sözlükler anahter değer yapısına sahip farklı veri türlerini destekleyen yapılardır
#anahtar değler eşsiz olmak zorunda
print(dir(dict()))
sozluk = {}
sozluk = dict() #dictionary
#sol anahtar(key): değer(value)
#key eşsiz olmak zorunda
#key value pairs
sozluk = {"A":1,"B":2,"C":3 }
#sözlük uzunluğu
print(len(sozluk))
print(sozluk.keys())
print("Key Type: ", sozluk.keys())
print(sozluk.values())
print(sozluk.items())
#sözlüğe elemna ekleme
sozluk["D"] = 4
print(sozluk)
#del sozluk
print(sozluk.get("A"))
#B anahtarını sil
sozluk.pop("B")
print(sozluk)
print(sozluk.fromkeys("B"))
yeni_sozluk = sozluk.copy()
print(yeni_sozluk)
yeni_sozluk.clear()
#son itemi siler
sozluk.popitem()
print(sozluk)
x = sozluk.setdefault("A")
print(x)
###sözlük içinde liste
sinif = {"9A":["Mana","Murat","Meysun","Yakup","Ela"],
         "10A":["İpek","Hikmet"],
         "11A":["Melek","Eray","Süleyman"]}
print(type(sinif))
print(sinif["9A"])
print(sinif["10A"])
print(sinif["11A"])

sozluk = {"book":["kitap"],
"pen":["kalem"],
"door":["kapı"],
"orange":["portakal","turuncu"]
}

print(list(sozluk.keys()))
print(type(list(sozluk.values())[3][0]))
print(sozluk["orange"])
sozluk["orange"].append("xxxx")
print(sozluk["orange"])
sozluk["orange"] = "yyyy"
print(sozluk)

sozluk = {"A":5,"B":7}

print(sozluk["A"])