Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ["hello", 2.0, 5, [10,20]]
['hello', 2.0, 5, [10, 20]]
>>> a = ["hello", 2.0, 5, [10,20]]
>>> print a[0]
hello
>>> print a[2]
5
>>> print a[3][1]
20
>>> a[3]
[10, 20]
>>> a[3][1]
20
>>> a[3][0]
10
>>> a
['hello', 2.0, 5, [10, 20]]
>>> a[1]='Good Bye'
>>> a
['hello', 'Good Bye', 5, [10, 20]]
>>> 
>>> a[-1]
[10, 20]
>>> len(a)
4
>>> a[-2]=10
>>> a
['hello', 'Good Bye', 10, [10, 20]]
>>> 
>>> a[1.2]

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a[1.2]
TypeError: list indices must be integers, not float
>>> a[1.0]

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a[1.0]
TypeError: list indices must be integers, not float
>>> a[4]=2

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a[4]=2
IndexError: list assignment index out of range
>>> a[-5]=1

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a[-5]=1
IndexError: list assignment index out of range
>>> q=range(0,5)
>>> q
[0, 1, 2, 3, 4]
>>> a
['hello', 'Good Bye', 10, [10, 20]]
>>> type (q)
<type 'list'>
>>> q[0]=43546
>>> q
[43546, 1, 2, 3, 4]
>>> q[1:1]=range[5.1,-1]

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    q[1:1]=range[5.1,-1]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> q[1:1]=range(5.1,-1)

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    q[1:1]=range(5.1,-1)
TypeError: range() integer start argument expected, got float.
>>> q[1:1] = range(5,1,-1)
>>> q
[43546, 5, 4, 3, 2, 1, 2, 3, 4]
>>> q
[43546, 5, 4, 3, 2, 1, 2, 3, 4]
>>> [43546, 5, 4, 3, 2, 1, 2, 3, 4]
[43546, 5, 4, 3, 2, 1, 2, 3, 4]
>>>  q=range(0,5)
 
  File "<pyshell#33>", line 2
    q=range(0,5)
    ^
IndentationError: unexpected indent
>>>  q=range(0,5)
 
  File "<pyshell#34>", line 2
    q=range(0,5)
    ^
IndentationError: unexpected indent
>>>  q=range(0,5)
 
  File "<pyshell#35>", line 2
    q=range(0,5)
    ^
IndentationError: unexpected indent
>>> q
[43546, 5, 4, 3, 2, 1, 2, 3, 4]
>>> del q
>>> q

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> z

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> ÿ
SyntaxError: invalid syntax
>>> ÿ
SyntaxError: invalid syntax
>>> 
>>> 
