# -*- coding: cp1254 -*-
sonuc = []

for i in range(100):
    sonuc.append(i**2)

#print sonuc

sonuc2 = [i**2 for i in range(100)]
print sonuc2

print [i**2 for i in range(100)]

sonuc3 = [i**2 for i in xrange(100)]
#xrange her birimi tek tek ürettiğinden range den hızlı çalışır
print sonuc3
    

