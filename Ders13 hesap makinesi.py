# -*- coding: cp1254 -*-
from __future__ import division
print """1.Toplama
2.��karma
3.�arpma
4.B�lme
5.Mod Alma
6.�s Alma"""

islem = input ("L�tfen i�lemi se�iniz: ")
sayi1 = input("�lk Say�y� Giriniz: ")
sayi2 = input("�kinci Say�y� Giriniz: ")

if islem == 1:
    print "Sonu� = ", sayi1+sayi2
#her seferinde if kullanmak yerine elif(else if) kullanarak program� h�zland�r�yoruz
elif islem == 2:
    print "Sonu� = ", sayi1-sayi2

elif islem == 3:
    print "Sonu� = ", sayi1*sayi2

elif islem == 4:
    if sayi2 == 0:
        print "B�len 0'a e�it olamaz."
    if sayi2 != 0:
        print "Sonu� = ", sayi1/sayi2

elif islem == 5:
    print "Sonu� = ", sayi1%sayi2

elif islem == 6:
    print "Sonu� = ", sayi1**sayi2

else:
    print "L�tfen 1-6 aras�nda bir say� girin."
