# -*- coding: cp1254 -*-

liste = ["elma","armut","ayva","çilek"]

for meyve in liste:
    print meyve

# 1.döngü: meyve=liste[0]
# meyve="elma"
# print meyve

# 2.döngü: meyve=liste[1]
# meyve="armut"
# print meyve

# 3.döngü: meyve=liste[2]
# meyve="ayva"
# print meyve

# 4.döngü: meyve=liste[3]
# meyve="çilek"
# print meyve

liste1 = [321,543,65,324,75,7,423,654]

for i in liste1:
    print i**2
    print "Yunus"

# döngünün içinde olmasını istediğimiz komutları aynı hizada yazdık

print "---------------------"

liste2 = range(100)
for i in liste2:
    print i**2

print "***********************"

for harf in "Yunus GÜMÜŞSOY":
    print harf

