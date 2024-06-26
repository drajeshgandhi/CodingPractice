#----------------------------------------#
#Basic python programs concepts: 
#09-Dec-2020
#----------------------------------------#
n = 0
while n < 4:
 n += 1
 print(n)
#----------------------------------------#
x = 0
y = 2
z = len("Python")
x = y > z
print(x,n)
type(x)
#----------------------------------------#
Val = 1
Val2 = 0
Val = Val ^ Val2
print(Val)
Val2 = Val ^ Val2
print(Val2)
Val = Val ^ Val2 
print(Val)
print(Val)
#----------------------------------------#
z, y, x = 2, 1, 0
x, z = z, y
y = y - z
#x, y, z = y, z, x
z, y, x = x, z, y
print(x, y, z)
#----------------------------------------#
a = 0
b = a ** 0
if b < a + 1:
 c = 1
elif b == 1:
 c = 2
else:
 c = 3
print(a,b,c, a + b + c)
#----------------------------------------#
0 ** 0 
#----------------------------------------#
i = 10
while i > 0 :
     i -= 3
     print("*")
     if i <= 3:
         break
else:
     print("*")
#----------------------------------------#
for i in range(1, 4, 2):
 print(i)
#----------------------------------------#
for i in range(1, 4, 2):
 print(i, end=" ")
#----------------------------------------#
for i in range(1, 4, 2):
 print(i, end="**")
#----------------------------------------#
for i in range(1, 4, 2):
 print(i, end="**")
print("***")
#----------------------------------------#
x = "20"
y = "30"
print(x > y) 
#----------------------------------------#
s = "Hello, Python!"
print(s[-14:20])

#----------------------------------------#
dict1 = { 'a': 1, 'b': 3, 'c': 7 }
for item in dict1:
 print(dict1[item])
print(dict1.pop('a'))
print(dict1)
dict1['k']='inf'
print(dict1)
if "b" in dict1:
    print ("yes")
#----------------------------------------#
s = 'python'
for i in range(len(s)):
    i = s[i].upper()
    print(i, end="")
#----------------------------------------#
lst = [i // i for i in range(1,4)]
print(lst)
sum = 0
for n in lst:
 sum += n
print(sum)

#----------------------------------------#
lst = [[c for c in range(r)] for r in range(3)]
print(lst)
for x in lst:
 for y in x:
     if y < 2:
         print('*', end='')
#----------------------------------------#
lst = [2 ** x for x in range(0, 11)]
print (lst[-1])
#----------------------------------------#
lst1 = "12,34"
lst2 = lst1.split(',')
print(lst1, len(lst1)) 
print(lst2, len(lst2))
#----------------------------------------#
def fun(a, b=0, c=5, d=1):
  return a ** b ** c
print(fun(b=2, a=2, c=3))
#First b ** c gets calculated and then a ** b**c gets calculated
#----------------------------------------#
x = 10
f = lambda x: 1 + 5
print(f(x))
#----------------------------------------#
'''using an action prior to for (we which we run after for usually) & doing it in one line is "comprehension" concept in python'''
names=['raj','jan','kri']
upper_names = [k.upper() for k in names ]
print(upper_names)
#----------------------------------------#
from random import randint
for i in range(10):
 print(randint(1, 5))
#----------------------------------------#
x = 1 # line 1
def a(x): # line 2
 return 2 * x # line 3
x = 2 + a(x) # line 4
print(a(x)) # line 5
#----------------------------------------#
a = 'hello' # line 1
def x(a): # line 2
 z = a[0] # line 3
 return z # line 4
print(x(a)) # line 5
#----------------------------------------#
s = 'SPAM'
def f(x):
 return s + 'MAPS'
print(f(s))
#----------------------------------------#
for i in range(1,5):
     print(i)
#----------------------------------------#
3%1
#----------------------------------------#
x = 0
try:
 print(x)
 print(1 / x)
except ZeroDivisionError:
 print("ERROR MESSAGE")
finally:
 print(x + 1)
print(x + 2)
#----------------------------------------#
class A:
 def a(self):
     print("A", end='')

class B(A):
 def a(self):
     print("B", end='')
class C(B):
 def b(self):
     print("B", end='')

a = A()
b = B()
c = C()
a.a()
b.a()
c.b()
#----------------------------------------#
try:
 print("Hello")
 raise Exception()
 print(1/0)
except Exception as e:
 print(e, "error occured")
#----------------------------------------#
from math import pi as xyz # line 01
print(xyz) # line 
#----------------------------------------#
name='Macdonald'
lst1=[]
lst1+=name[3].upper()
print(lst1)
#----------------------------------------#
def old_macdonald(name):
        lst1 = []
        for i in range(0,len(name)):
                if i == 0 or i == 3 :
                        lst1 += name[i].upper()
                else:
                        lst1 += name[i]
#    print(name[3].upper())
        return ''.join(lst1)

print(old_macdonald('macdonald'))
#----------------------------------------#
def master_yoda(phrase):
    return ' '.join(phrase.split()[::-1])
        
print(master_yoda('I am home')) #--> 'home am I'
print(master_yoda('We are ready ')) #--> 'ready are We'
#master_yoda('We are ready')
#----------------------------------------#
abs(200-90)
#----------------------------------------#
def paper_doll(str1):
        lst1=''
        for i in range(0,len(str1)):
                lst1 +=3*str1[i]
        return lst1

print(paper_doll('Hello')) #--> 'HHHeeellllllooo'
print(paper_doll('Mississippi')) # --> 'MMMiiissssssiiippppppiii'
#----------------------------------------#
def blackjack(n1,n2,n3):
        sum = n1+n2+n3
        if sum <= 21:
                return sum
        elif (11 in (n1,n2,n3)):
            sum=sum-10
            if sum <=21:
                    return sum
        else:
            return 'BUST'


print(blackjack(5,6,7)) #--> 18
print(blackjack(9,9,9)) #--> 'BUST'
print(blackjack(9,9,11)) #--> 19
#----------------------------------------#
def summer_69(arr):
    add = True 
    sum =0
    for i in arr:
        while add:
            if i != 6:
                sum+= i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return sum
summer_69([4, 5, 6, 7, 8, 9])    
summer_69([1,3,5])
summer_69([2, 1, 6, 9, 11])
#----------------------------------------#
x=2
(4/3)*x**3
#----------------------------------------#
x=3
if x > 1 and x < 10:
    print('True')