Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=3
>>> print a
3
>>> del a
>>> print a

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print a
NameError: name 'a' is not defined
>>> liste=[423,76,431,654,8769]
>>> print liste
[423, 76, 431, 654, 8769]
>>> del liste[2]
>>> print liste
[423, 76, 654, 8769]
>>> liste.append(4323)
>>> liste.append(3242)
>>> print liste
[423, 76, 654, 8769, 4323, 3242]
>>> del liste[2:4]
>>> print liste
[423, 76, 4323, 3242]
>>> del liste
>>> print liste

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print liste
NameError: name 'liste' is not defined
>>> isim = "Yunus"
>>> print isim
Yunus
>>> del isim
>>> print isim

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print isim
NameError: name 'isim' is not defined
>>> a = ["Yunus", 32.424]
>>> print a
['Yunus', 32.424]
>>> demet = (321,34543,76,"Yunus")
>>> print demet
(321, 34543, 76, 'Yunus')
>>> demet[3]
'Yunus'
>>> print demet[3]
Yunus
>>> print demet[1:3]
(34543, 76)
>>> demet.append(3421)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    demet.append(3421)
AttributeError: 'tuple' object has no attribute 'append'
>>> demet[1]=-100

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    demet[1]=-100
TypeError: 'tuple' object does not support item assignment
>>> a=3
>>> b=5
>>> yedek = a
>>> a=b
>>> b=yedek
>>> print a,b
5 3
>>> a=3
>>> b=5
>>> a,b=b,a
>>> a
5
>>> b
3
>>> a=1
>>> b=2
>>> c=3
>>> a,b,c=b,c,a
>>> print a,b,c
2 3 1
>>> a=1.15
>>> demet=(432,543)
>>> demet2=1,5,6,10
>>> print demet2
(1, 5, 6, 10)
>>> 
