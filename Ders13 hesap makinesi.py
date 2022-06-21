# -*- coding: cp1254 -*-
from __future__ import division
print """1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
5.Mod Alma
6.Üs Alma"""

islem = input ("Lütfen işlemi seçiniz: ")
sayi1 = input("İlk Sayıyı Giriniz: ")
sayi2 = input("İkinci Sayıyı Giriniz: ")

if islem == 1:
    print "Sonuç = ", sayi1+sayi2
#her seferinde if kullanmak yerine elif(else if) kullanarak programı hızlandırıyoruz
elif islem == 2:
    print "Sonuç = ", sayi1-sayi2

elif islem == 3:
    print "Sonuç = ", sayi1*sayi2

elif islem == 4:
    if sayi2 == 0:
        print "Bölen 0'a eşit olamaz."
    if sayi2 != 0:
        print "Sonuç = ", sayi1/sayi2

elif islem == 5:
    print "Sonuç = ", sayi1%sayi2

elif islem == 6:
    print "Sonuç = ", sayi1**sayi2

else:
    print "Lütfen 1-6 arasında bir sayı girin."
