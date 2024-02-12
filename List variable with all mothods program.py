num=[10,15,20,50,45,86]
num[0]
10
//Index

num[4]
45
num[-1]
86
num[-5]
15


//floating vaulues entering

num.append(0.9)
num=[10, 15, 20, 50, 45, 86, 0.9]
num.append(5.9)
num=[10, 15, 20, 50, 45, 86, 0.9, 5.8]

//Entering String values in a variable

num.append('Krishna')
num

num.append("Madhavi")
num
[10, 15, 20, 50, 45, 86, 0.9, 5.8, 'Krishna', 'Madhavi']

//Entering the Boolean values in List variable:
    

num.append(True)
num
[10, 15, 20, 50, 45, 86, 0.9, 5.8, 'Krishna', 'Madhavi', True]
num.append(False)
num
[10, 15, 20, 50, 45, 86, 0.9, 5.8, 'Krishna', 'Madhavi', True, False]


Adding Mutliple data types in alist variable:
    
SyntaxError: invalid syntax

num.Extend(99,100,500)
num.extend([99,100,500,'Yashashvi','shashvita sai'])
num
[10, 15, 20, 50, 45, 86, 0.9, 5.8, 'Krishna', 'Madhavi', True, False, 99, 100, 500, 'Yashashvi', 'shashvita sai']
num.extend([99,100,500,98.99,78.53,70.9,'Yashashvi','shashvita sai'])
num
[10, 15, 20, 50, 45, 86, 0.9, 5.8, 'Krishna', 'Madhavi', True, False, 99, 100, 500, 'Yashashvi', 'shashvita sai', 99, 100, 500, 98.99, 78.53, 70.9, 'Yashashvi', 'shashvita sai']


Replace the datatypes in List Variables:
    

num['Krishna']='Pallavi'

num[9]='Pallavi'
num
[10, 15, 20, 50, 45, 86, 0.9, 5.8, 'Krishna', 'Pallavi', True, False, 99, 100, 500, 'Yashashvi', 'shashvita sai', 99, 100, 500, 98.99, 78.53, 70.9, 'Yashashvi', 'shashvita sai']
num
[10, 15, 20, 50, 45, 86, 0.9, 5.8, 'Krishna', 'Pallavi', True, False, 99, 100, 500, 'Yashashvi', 'shashvita sai', 99, 100, 500, 98.99, 78.53, 70.9, 'Yashashvi', 'shashvita sai']

Remove or delete the datatypes from the List variable:
    
SyntaxError: invalid syntax

num.pop[9]

num.pop(1)
15
num
[10, 20, 50, 45, 86, 0.9, 5.8, 'Krishna', 'Pallavi', True, False, 99, 100, 500, 'Yashashvi', 'shashvita sai', 99, 100, 500, 98.99, 78.53, 70.9, 'Yashashvi', 'shashvita sai']
num.pop(0:3)
SyntaxError: invalid syntax
num
[10, 20, 50, 45, 86, 0.9, 5.8, 'Krishna', 'Pallavi', True, False, 99, 100, 500, 'Yashashvi', 'shashvita sai', 99, 100, 500, 98.99, 78.53, 70.9, 'Yashashvi', 'shashvita sai']
num.pop(5)
0.9
num
[10, 20, 50, 45, 86, 5.8, 'Krishna', 'Pallavi', True, False, 99, 100, 500, 'Yashashvi', 'shashvita sai', 99, 100, 500, 98.99, 78.53, 70.9, 'Yashashvi', 'shashvita sai']
num
[10, 20, 50, 45, 86, 5.8, 'Krishna', 'Pallavi', True, False, 99, 100, 500, 'Yashashvi', 'shashvita sai', 99, 100, 500, 98.99, 78.53, 70.9, 'Yashashvi', 'shashvita sai']


Complete list variable deleting:
    
SyntaxError: invalid syntax

num.clear()
num
[]

num
[]



num[10, 20, 50, 45, 86, 100,200,500,1,2,3]

num1[10, 20, 50, 45, 86, 100,200,500,1,2,3]


Sorting Orders Assending and Dessending orders in List variables:
    
SyntaxError: invalid syntax

Namenum=[10, 20, 50, 45, 86, 100,200,500,1,2,3]
num=[10, 20, 50, 45, 86, 100,200,500,1,2,3]

num
[10, 20, 50, 45, 86, 100, 200, 500, 1, 2, 3]
num.sort()
num
[1, 2, 3, 10, 20, 45, 50, 86, 100, 200, 500]
num
[1, 2, 3, 10, 20, 45, 50, 86, 100, 200, 500]
Dessending orders
SyntaxError: invalid syntax

num.reverse()
num
[500, 200, 100, 86, 50, 45, 20, 10, 3, 2, 1]
num
[500, 200, 100, 86, 50, 45, 20, 10, 3, 2, 1]
 or
 

fruits=["apple","guava","orrange","kiwi","banana"]
frouits
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    frouits
NameError: name 'frouits' is not defined. Did you mean: 'fruits'?
fruits
['apple', 'guava', 'orrange', 'kiwi', 'banana']
fruits
['apple', 'guava', 'orrange', 'kiwi', 'banana']
fruits
['apple', 'guava', 'orrange', 'kiwi', 'banana']
fruits.sort()
fruits
['apple', 'banana', 'guava', 'kiwi', 'orrange']
fruits
['apple', 'banana', 'guava', 'kiwi', 'orrange']

fruits.sort(reverse'True)
            
SyntaxError: unterminated string literal (detected at line 1)
>>> fruits.sort(reverse=True)
...             
>>> fruits
...             
['orrange', 'kiwi', 'guava', 'banana', 'apple']
>>> fruits.sort(reverse'True
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> 
>>> 
>>> 
>>> num
...             
[500, 200, 100, 86, 50, 45, 20, 10, 3, 2, 1]
>>> num.sort()
...             
>>> num
...             
[1, 2, 3, 10, 20, 45, 50, 86, 100, 200, 500]
>>> num.minimum()
...             
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    num.minimum()
AttributeError: 'list' object has no attribute 'minimum'
>>> num.min()
...             
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    num.min()
AttributeError: 'list' object has no attribute 'min'
>>> num.min(num)
...             
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    num.min(num)
AttributeError: 'list' object has no attribute 'min'
>>> num.minimum(num)
...             
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    num.minimum(num)
AttributeError: 'list' object has no attribute 'minimum'
>>> 
