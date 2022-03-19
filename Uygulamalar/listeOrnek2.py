# 1	 0	1	0 2
# 1  1	1	1 4 
# 1	 0	0	1 2
# 0	 0	1	1 2
# 0	 1	0	1 2
# 2  3  2   1 
# yukarıdaki tabloyu listelerden oluşan bir demet şeklinde yazınız
# her satırdaki 1 lerin toplamını listenin sonuna ekleyiniz
# her sütundeaki sıfırların sayısını sütunların altına ekleyiniz.
tablo = ([1,0,1,0], [1,1,1,1,], [1,0,0,1], [0,0,1,1], [0,1,0,1])
print(tablo)
toplam_bir1 = tablo[0].count(1)
toplam_iki1 = tablo[1].count(1)
toplam_uc1 = tablo[2].count(1)
toplam_dort1 = tablo[3].count(1)
toplam_bes1 = tablo[4].count(1)
tablo[0].append(toplam_bir1)
tablo[1].append(toplam_iki1)
tablo[2].append(toplam_uc1)
tablo[3].append(toplam_dort1)
tablo[4].append(toplam_bes1)
print(tablo)
tablo = list(tablo)
sut1 = [tablo[0][0] , tablo[1][0], tablo[2][0], tablo[3][0], tablo[4][0]]
toplam_sut1_0 = sut1.count(0)
sut2 = [tablo[0][1] , tablo[1][1],tablo[2][1],tablo[3][1], tablo[4][1]]
toplam_sut2_0 = sut2.count(0)
sut3 = [tablo[0][2] , tablo[1][2],tablo[2][2],tablo[3][2], tablo[4][2]]
toplam_sut3_0 = sut3.count(0)
sut4 = [tablo[0][3] , tablo[1][3],tablo[2][3],tablo[3][3], tablo[4][3]]
toplam_sut4_0 = sut4.count(0)
sut5 = [tablo[0][4] , tablo[1][4],tablo[2][4],tablo[3][4], tablo[4][4]]
toplam_sut5_0 = sut5.count(0)
sutun_sifir = [toplam_sut1_0, toplam_sut2_0,toplam_sut3_0,toplam_sut4_0,toplam_sut5_0]
tablo.append(sutun_sifir)
tablo = tuple(tablo)
print(tablo)