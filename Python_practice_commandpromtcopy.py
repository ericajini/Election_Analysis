C:\Users\erica>python
Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> type(3)
<class 'int'>
>>> type(2019)
<class 'int'>
>>> ballots = 1,341
>>> ballots
(1, 341)
>>> ballots = 1341
>>> ballots
1341
>>> type(ballots)
<class 'int'>
>>> ballots = 1,341
>>> type(ballots)
<class 'tuple'>
>>> type(73.81)
<class 'float'>
>>> type("Hello World")
<class 'str'>
>>> type(' ')
<class 'str'>
>>> type('2019')
<class 'str'>
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> help('Keywords')
No Python documentation found for 'Keywords'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

>>> 5+2*3
11
>>> 8//5-3
-2
>>> 8+22*2-4
48
>>> 16-3/2+7-1
20.5
>>> 3**3%5
2
>>> 5+9*3/2-4
14.5
>>> (5+2)*3
21
>>> (8//5)-3
-2
>>> 8+(22*(2-4))
-36
>>> 16-3/(2+7)-1
14.666666666666666
>>> 3**(3%5)
27
>>> 5+(9*3/2-4)
14.5
>>> 5+(9*3/(2_4))
6.125
>>> 5+(9*3/(2-4))
-8.5
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> my_list = list()
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> counties[0]
'Arapahoe'
>>> print(counties[2])
Jefferson
>>> print(counties[-1])
Jefferson
>>> counties[-2]
'Denver'
>>> len(counties)
3
>>> counties[0:3]
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[1:2]
['Denver']
>>> counties[1:3]
['Denver', 'Jefferson']
>>> cpimtoes[1:]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cpimtoes' is not defined
>>> counties[1:]
['Denver', 'Jefferson']
>>> counties.append("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2,"El Paso")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.remove(4,"El Paso")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: remove() takes exactly one argument (2 given)
>>> counties.remove("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.pop("El Paso")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> counties.pop(3)
'El Paso'
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties.append("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.pop[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> counties.pop(-1)
'El Paso'
>>> counties[2] = "El Paso"
>>> counties
['Arapahoe', 'Denver', 'El Paso']
>>> counties.remove("El Paso")
>>> counties
['Arapahoe', 'Denver']
>>> counties.append("Jefferson")
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties.insert(1,"El Paso")
>>> counties
['Arapahoe', 'El Paso', 'Denver', 'Jefferson']
>>> counties.pop[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> counties.pop(0)
'Arapahoe'
>>> counties
['El Paso', 'Denver', 'Jefferson']
>>> counties[2] = "Denver"
>>> counties
['El Paso', 'Denver', 'Denver']
>>> counties[1] = "Jefferson"
>>> counties
['El Paso', 'Jefferson', 'Denver']
>>> counties.append("Arapahoe")
>>> counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']
>>> my_tuple = tuple()
>>> counties_tuple = ("Arapahoe","Denver","Jefferson")
>>> counties_tuple
('Arapahoe', 'Denver', 'Jefferson')
>>> len(counties_tuple)
3
>>> counties[1]
'Jefferson'
>>> counties_tuple[1]
'Denver'
>>> counties_tuple[:-1]
('Arapahoe', 'Denver')
>>> counties_tuple[1:2]
('Denver',)
>>> counties[:2]
['El Paso', 'Jefferson']
>>> counties[-2]
'Denver'
>>> counties_tuple[:2]
('Arapahoe', 'Denver')
>>> my_dictionary = dict{}
  File "<stdin>", line 1
    my_dictionary = dict{}
                        ^
SyntaxError: invalid syntax
>>> counties_dict = {}
>>> counties_dict["Arapahoe"] = 422829
>>> counties_dict
{'Arapahoe': 422829}
>>> counties_dict["Denver"] = 463353
>>> counties_dict["Jefferson"] = 432438
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> len(counties_dict)
3
>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
>>> counties_dict.values()
dict_values([422829, 463353, 432438])
>>> counties_dict.get("Denver")
463353
>>> print(counties_dict['Arapahoe'])
422829
>>> counties_dict['Arapahoe']
422829
>>> print(counties_dict.get("Arapahoe"))
422829
>>> counties_dict['Arapahoe']
422829
>>> counties_dict["Arapahoe"]
422829
>>> voting_data = []
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (3 given)
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829}), ({"county":"Denver", "registered_voters": 463353})
(None, {'county': 'Denver', 'registered_voters': 463353})
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> len(voting_data)
4
>>> voting_data.append({"county":"El Paso", "registered_voters": 461149})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 461149}]
>>> voting_data.remove({'Arapahoe', 'registered_voters': 422829})
  File "<stdin>", line 1
    voting_data.remove({'Arapahoe', 'registered_voters': 422829})
                                                       ^
SyntaxError: invalid syntax
>>> voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 461149}]
>>> voting_data.remove({'Arapahoe', 'registered_voters': 422829})
  File "<stdin>", line 1
    voting_data.remove({'Arapahoe', 'registered_voters': 422829})
                                                       ^
SyntaxError: invalid syntax
>>> voting_data.pop(1)
{'county': 'Denver', 'registered_voters': 463353}
>>> voting_data.pop(0)
{'county': 'Arapahoe', 'registered_voters': 422829}
>>> voting_data
[{'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 461149}]
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data
[{'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}]
>>> votin_data.pop(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'votin_data' is not defined
>>> voting_data.pop(0)
{'county': 'Jefferson', 'registered_voters': 432438}
>>> voting_data.insert(1,{"county":"Jefferson", "registered_voters": 432438})
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}]
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]
>>>