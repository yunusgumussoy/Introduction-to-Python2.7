# -*- coding: cp1254 -*-
"""
1.Dosyan�n a��lmas� (dosya:veri.txt)
    r => read,okuma
    w => write, yazma (���NDEK�LER KAYBOLUR!)
    a => append, ekleme (hem okuma hem de yazma)
2.Dosya �zerindeki i�lemlerin yap�lmas�
    r => read,okuma
    w => write,yazma
3.Dosyan�n kapat�lmas�
    close =>kapatma
"""

dosya = open("veri.txt","r")

#print dir(dosya)

satirlar = dosya.readlines()
#dosyan�n i�indekileri sat�r sat�r yazar
for satir in satirlar:
    print satir


print dosya.readline()
#her seferinde bir sat�r� yazar

print dosya.read()

dosya.close()

dosya = open("veri.txt","w")
dosya.write("Yunus G�m��soy\nElma Armut")
dosya.close()

dosya = open("veri.txt","a")
dosya.write("\nYunus G�m��soy\nElma Armut")
dosya.close()

dosya = open("veri.txt","a")
for i in range(100):
    dosya.write("\nYunus G�m��soy\nElma Armut")
dosya.close()
