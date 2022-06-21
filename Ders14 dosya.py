# -*- coding: cp1254 -*-
"""
1.Dosyanın açılması (dosya:veri.txt)
    r => read,okuma
    w => write, yazma (İÇİNDEKİLER KAYBOLUR!)
    a => append, ekleme (hem okuma hem de yazma)
2.Dosya üzerindeki işlemlerin yapılması
    r => read,okuma
    w => write,yazma
3.Dosyanın kapatılması
    close =>kapatma
"""

dosya = open("veri.txt","r")

#print dir(dosya)

satirlar = dosya.readlines()
#dosyanın içindekileri satır satır yazar
for satir in satirlar:
    print satir


print dosya.readline()
#her seferinde bir satırı yazar

print dosya.read()

dosya.close()

dosya = open("veri.txt","w")
dosya.write("Yunus Gümüşsoy\nElma Armut")
dosya.close()

dosya = open("veri.txt","a")
dosya.write("\nYunus Gümüşsoy\nElma Armut")
dosya.close()

dosya = open("veri.txt","a")
for i in range(100):
    dosya.write("\nYunus Gümüşsoy\nElma Armut")
dosya.close()
