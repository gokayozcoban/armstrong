

# BİR SAYININ HER BASAMAĞINDAKİ SAYININ BASAMAK SAYISI KADAR KUVVETİNİN
# YANİ ÜSSÜNÜN ALINARAK TOPLANMASI SONUCU BASAMAKLARI AYRILAN SAYILA EŞİTSE
# BU BİR AMSTRONG SAYIDIR.

sayı = int(input("Sayı girin: "))
basamak = int(input("Girilen sayının basamak sayısı: "))

toplam = 0
i = sayı

for x in range(0,basamak+1):
    rakam = i % 10
    toplam += rakam ** basamak
    i // 10
    print("\n"*2)
if (sayı == toplam):
    print("Bu bir Armstrong Sayıdır!")
else:
    print("Armstrong sayı değildir!")
