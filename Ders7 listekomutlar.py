Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> liste=[321,54,65,12,432]
>>> print liste
[321, 54, 65, 12, 432]
>>> dir(liste)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> liste.append("Yunus")
>>> print liste
[321, 54, 65, 12, 432, 'Yunus']
>>> liste.append("Gumussoy")
>>> print liste
[321, 54, 65, 12, 432, 'Yunus', 'Gumussoy']
>>> liste.append(65)
>>> liste.append(65)
>>> print liste
[321, 54, 65, 12, 432, 'Yunus', 'Gumussoy', 65, 65]
>>> liste.count(65)
3
>>> liste.count("Yunus")
1
>>> liste2=["elma","armut","ayva"]
>>> print liste2
['elma', 'armut', 'ayva']
>>> print liste
[321, 54, 65, 12, 432, 'Yunus', 'Gumussoy', 65, 65]
>>> liste.extend(liste2)
>>> print liste
[321, 54, 65, 12, 432, 'Yunus', 'Gumussoy', 65, 65, 'elma', 'armut', 'ayva']
>>> liste.index("Yunus")
5
>>> liste.index(65)
2
>>> liste.insert("abc")

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    liste.insert("abc")
TypeError: insert() takes exactly 2 arguments (1 given)
>>> liste.insert(1,"abc")
>>> print liste
[321, 'abc', 54, 65, 12, 432, 'Yunus', 'Gumussoy', 65, 65, 'elma', 'armut', 'ayva']
>>> liste.index("Yunus")
6
>>> liste.insert(6,"elma")
>>> print liste
[321, 'abc', 54, 65, 12, 432, 'elma', 'Yunus', 'Gumussoy', 65, 65, 'elma', 'armut', 'ayva']
>>> liste.index("elma")
6
>>> liste.pop()
'ayva'
>>> print liste
[321, 'abc', 54, 65, 12, 432, 'elma', 'Yunus', 'Gumussoy', 65, 65, 'elma', 'armut']
>>> liste.pop()
'armut'
>>> print liste
[321, 'abc', 54, 65, 12, 432, 'elma', 'Yunus', 'Gumussoy', 65, 65, 'elma']
>>> liste.extend(liste2)
>>> print liste2
['elma', 'armut', 'ayva']
>>> print liste
[321, 'abc', 54, 65, 12, 432, 'elma', 'Yunus', 'Gumussoy', 65, 65, 'elma', 'elma', 'armut', 'ayva']
>>> liste.pop(7)
'Yunus'
>>> liste.pop(7)
'Gumussoy'
>>> liste.remove("abc")
>>> print liste
[321, 54, 65, 12, 432, 'elma', 65, 65, 'elma', 'elma', 'armut', 'ayva']
>>> liste.remove(65)
>>> print liste
[321, 54, 12, 432, 'elma', 65, 65, 'elma', 'elma', 'armut', 'ayva']
>>> liste.reverse()
>>> print liste
['ayva', 'armut', 'elma', 'elma', 65, 65, 'elma', 432, 12, 54, 321]
>>> liste.sort()
>>> print liste
[12, 54, 65, 65, 321, 432, 'armut', 'ayva', 'elma', 'elma', 'elma']
>>> 
