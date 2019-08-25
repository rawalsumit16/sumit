Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l1=[1,2,3,4,'a','B','c',7,6,9]
>>> l1
[1, 2, 3, 4, 'a', 'B', 'c', 7, 6, 9]
>>> dir(l1)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> l1.append()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    l1.append()
TypeError: append() takes exactly one argument (0 given)
>>> l1.append(10)
>>> l1
[1, 2, 3, 4, 'a', 'B', 'c', 7, 6, 9, 10]
>>> '''
append = add data in list to the end
'''
'\nappend = add data in list to the end\n'
>>> l1.clear()
>>> l1
[]
>>> '''
clear = it clear all the data in list
'''
'\nclear = it clear all the data in list\n'
>>> l1.copy()
[]
>>> l1=[1,2,3,4,'a','B','c',7,6,9]
>>> l1.copy()
[1, 2, 3, 4, 'a', 'B', 'c', 7, 6, 9]
>>> '''
copy = copy data presented in list and disply data as it is.
'''
'\ncopy = copy data presented in list and disply data as it is.\n'
>>> l1.count(4)
1
>>> '''
count = count the data which user wants
'''
'\ncount = count the data which user wants\n'
>>> l1.extend('x')
>>> l1
[1, 2, 3, 4, 'a', 'B', 'c', 7, 6, 9, 'x']
>>> '''
extend = add data in list and modify list
'''
'\nextend = add data in list and modify list\n'
>>> l1.index(3)
2
>>> '''
index = it shows the position of no 3 in the list, that is place of 2
'''
'\nindex = it shows the position of no 3 in the list, that is place of 2\n'
>>> 
>>> l1.pop()
'x'
>>> l1
[1, 2, 3, 4, 'a', 'B', 'c', 7, 6, 9]
>>> '''
pop = it delete last digit of list, it cannot delete char or string value
'''
'\npop = it delete last digit of list, it cannot delete char or string value\n'
>>> '''
pop = it can not delete middle data
'''
'\npop = it can not delete middle data\n'
>>> l1.remove(3)
>>> l1
[1, 2, 4, 'a', 'B', 'c', 7, 6, 9]
>>> '''
remove = it removes the element and also show updated list.
'''
'\nremove = it removes the element and also show updated list.\n'
>>> l1.reverse()
>>> l1
[9, 6, 7, 'c', 'B', 'a', 4, 2, 1]
>>> '''
reverse = it reverse the list and show updated list.
'''
'\nreverse = it reverse the list and show updated list.\n'
>>> l1.sort()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    l1.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> l2=[1,3,4,2,8,5]
>>> l2.sort()
>>> l2
[1, 2, 3, 4, 5, 8]
>>> '''
sort = it shows the list in ascending order and modify original list.
'''
'\nsort = it shows the list in ascending order and modify original list.\n'
>>> 
