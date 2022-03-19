
#silindirin yüzey alanı ve hacmini bulunuz.
print("Silindir")
PI = 3.14
yari_cap = float(input("Yarı Çapı Giriniz: "))
yukselik = float(input("Yükseklik Giriniz: "))
#hacim
hacim = PI * yari_cap ** 2 * yukselik
yuzey_alani = (2 * (2 * PI * yari_cap)) + (2 * PI * yari_cap * yukselik)
print(f"Hacim: {hacim} ve Alan: {yuzey_alani}")

##koninin yüzey alanı ve hacmini bulunuz.
print("Koni")
yari_cap_koni = float(input("Yarı Çapı Giriniz: "))
yukselik_koni = float(input("Yükseklik Giriniz: "))
aci = float(input("Açı Giriniz: "))
yuzey_alani = ((aci / 360) * PI * yukselik_koni**2) + (2 * PI * yari_cap_koni)
hacim_koni = PI * yari_cap_koni ** 2 * yukselik_koni / 3
print(f"Hacim: {hacim_koni} ve Alan: {yuzey_alani}")

#küpün yüzey alanı ve hacmini bulunuz.
print("Küp")
kenar = float(input("Küp için Kenar Giriniz: "))
hacim_kup = kenar**3
alan_kup = 6 * 4 * kenar
print(f"Hacim: {hacim_kup} ve Alan: {alan_kup}")

#Küre
yari_cap_kure = float(input("Küre için Yarıçap Giriniz: "))
hacim_kure = 4/3 * PI * yari_cap_kure ** 3
alan_kure = 4 * PI * yari_cap_kure ** 2
print(f"Hacim: {hacim_kure} ve Alan: {alan_kure}")
