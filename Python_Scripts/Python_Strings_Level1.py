#----------------------------------------#
#This file contains some of the string operations and below type of problems
#Strings
#Palindrome
#Line Distance
#Exceptions
#Arrays
#Reverse of a string
#Number Programs
#----------------------------------------#
str1=input('enter a string to check: ')
lower = 0
upper = 0
for i in str1:
    #print (i)
    if i.isupper():
       upper += 1
    elif i.islower() :
#    else:
        lower += 1
#    else:
#        pass
print('number of upper letters are: ',upper)
print('number of lower letters are: {0}', format(lower))
#----------------------------------------#
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
#----------------------------------------#
def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
#----------------------------------------#
S_Lst = [1, 2, 3, -4]
#Expected Output : -24
x = 1
for i in S_Lst:
    x*=i
print(x)
#----------------------------------------#
#Pal='madam'
Pal='The quick brown fox jumps over the lazy dog'
#Pal='nurses run'
#Pal='Hello World'
#Pal= Pal.replace(" ",'')
print (Pal)
k=''.join(Pal.split())[::-1]#.replace(" ",'')
b=''.join(Pal.split()[::-1])
print (k)
print (b)
if Pal ==  k :
    print ('given string '+ format(Pal)+ ' is Palindrome')
else:
    print ('is not a palindrome')

#----------------------------------------#
class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return ((x2-x1)**2+(y2-y1)**2)**.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
#co1 = (3,2)
#co2 = (8,10)
li = Line((3,2),(8,10))
#----------------------------------------#
li.distance()
li.slope()
#----------------------------------------#
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        return 3.14*self.height*(self.radius**2)
    
    def surface_area(self):
        top=3.14*(self.radius**2)
        return (2*top)+(2*3.14*self.height*self.radius)
#----------------------------------------#
# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume()
c.surface_area()
#----------------------------------------#
class Simple:
    
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"amount {amount} deposited to account {self.owner}")
    
    def withdrawl(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"amount {amount} is withdrawn from account")
        else:
            print("Insufficient funds to withdraw")
    
    def __str__(self): #this is a special method in python to display the current object, use print(obj) to invoke
        return f'Owner is: {self.owner} \n Balance is: {self.balance}'
        

s1=Simple('Johnny',5000)
s1.owner
s1.balance
print(s1)
s1.deposit(5000)
s1.balance
s1.withdrawl(11000)
s1.withdrawl(1100)
s1.balance
print(s1)
#----------------------------------------#
try :
    for i in ['a','b','c']:
        print(i**2)
except:
    print('unsupported operand type(s) for ** or pow(): \'str\' and \'int\'')
    print('oops, an error occured')
#----------------------------------------#
x = 5
y = 0
try:
    z = x%y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')
#----------------------------------------#

def ask():
    
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
        
    print('Thank you, your number squared is: ',n**2)
ask()
#----------------------------------------#
def front_times(str1, n):
    list1 =[ ]
    for i in range(0,len(str1)):
        if i < 3:
            list1  += str1[i]
        else:
            pass
    return ''.join(list1)*n
    
front_times('CHOCOLATE',3)
#----------------------------------------#
def front_times2(str, n ):
    k=str[0:3]
    return k*n
front_times('CHOCOLATE',3)
#----------------------------------------#
'''Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello' '''
def string_bits(str):
  return str[::2]
string_bits('Heeololeo')
#----------------------------------------#
'''
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab' '''
def string_splosion(str):
  lst = []
  for i in range (0,len(str)):
    lst  +=  str[:i+1]
  return ''.join(lst)
string_splosion('Code')
#string_splosion('abc') 
#string_splosion('ab')
#----------------------------------------#
'''Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False '''

def array_front9(nums):
    for i in range (0,len(nums)):
        if i <= 3 and nums[i] == 9:
            return True  
    return False
array_front9([1, 2, 9, 3, 4])
array_front9([1, 2, 3, 4, 9])    
array_front9([1, 2, 3, 4, 5])
#----------------------------------------#
'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
'''

def string_match(a, b):
    if len(a) > len(b):
        upper = len(b)
    else:
        upper = len(a)
   
    count = 0 
    for i in range (upper-1):
        sub1 = a[i:i+2]
        sub2 = b[i:i+2]
        print(sub1, sub2)
        if (sub1==sub2):
            count+=1
        else:
            pass
    return count
#string_match('abc', 'abc')
string_match('abc', 'axc')
#----------------------------------------#
def reverse(str1):
    return str1[::-1]

reverse('hello')
#----------------------------------------#
'''Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
'''

def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False
first_last6([6, 1, 2, 3])
#----------------------------------------#
'''
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
'''
def same_first_last(nums):
    if nums[0]==nums[-1]:
        return True
    else:
        return False
    
same_first_last([1, 2, 1])
#----------------------------------------#
19 % 10
8 % 10 
10/(5*2)
9/(1*5)
1.8/1
2%1
10%10
9%5
4%3
16%10
16/10
10*round(46/10)
#----------------------------------------#
def make_bricks(small, big, goal):
  if goal == (big*5) + small:
    return True
  elif goal > (big*5) + small:
    return False
  else:
    goal = goal % (big*5)
    if goal % small  == 0:
      return True
    else:
      return False
make_bricks(3, 1, 8)
make_bricks(3, 1, 9)
make_bricks(3, 2, 10)
#----------------------------------------#
def lone_sum(a, b, c):
  A = (a,b,c)
  sum = 0
  for i in A:
    sum += i
  return sum
lone_sum(3, 2, 3)  
#----------------------------------------#
'''Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- 
in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
Define the helper below and at the same indent level as the main no_teen_sum().


no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3

'''

def no_teen_sum(a, b, c):
  return fix_teen(a)+fix_teen(b)+fix_teen(c)
  
def fix_teen(n):
  if n in [13,14,17,18,19]:
    return 0
  else:
    return n 

no_teen_sum(2, 1, 14)
#----------------------------------------#
'''For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, 
so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, 
so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, 
write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent 
level as round_sum().


round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10

'''
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
    
def round10(num):
    if num % 10 < 5:
        return num - (num % 10)
        
    return num + (10 - num % 10)


'''def round_sum(a, b, c):
  return int(round10(a)+round10(b)+round10(c))
def round10(num):  
  return 10*round(num/10)'''
round_sum(45, 21, 30)
#----------------------------------------#
'''
Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
'''
def count_hi(str):
  sum = 0
  k = 'hi'
#  print(len(str))
  for i in range(0,len(str)):
#    print (str[i:i+2])
    if k == str[i:i+2]:
      sum+=1
  return sum
count_hi('hi hi')
#----------------------------------------#
'''Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''
def count_code(str):
  code = 0
  for i in range(0,len(str)-3):
    if 'co' == str[i:i+2] and 'e' == str[i+3]:
      code+=1
  return code
count_code('aaacodebbb')
#----------------------------------------#
'''
Return True if the given string contains an appearance of "xyz" 
where the xyz is not directly preceeded by a period (.) So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
'''
def xyz_there(str):
  sum = 0
  for i in range(0,len(str)):
#    print(str[i:i+3], str[i-1])
    if str[i:i+3] == 'xyz' and str[i-1] != '.':
      sum+=1
    else:
      pass
  if sum > 0: 
       return True 
  else:
       return False
xyz_there('abcxyz')
#----------------------------------------#
'''

Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
'''
def big_diff(nums):
  mini = nums[0]
  maxi = nums[0]
  for i in range(0,len(nums)):
      mini = min(mini, nums[i])
      maxi = max(maxi, nums[i])
  return maxi-mini    
  
big_diff([10, 3, 5, 6])
#----------------------------------------#
def centered_average(nums):
  list1 = [ ]
  for i in nums:
    if i in list1:
      pass
    else:
      list1.append(i)   
#  print (list1)
  mini = list1[0]
  maxi = list1[0]
  avg = 0
  for j in range(0,len(list1)):
    mini = min(mini, list1[j])
    maxi = max(maxi, list1[j])
    avg += list1[j]
  print (avg-mini-maxi)
  if len(list1) <= 2:
    return avg-mini-maxi
  else:
    return int((avg-mini-maxi)/(len(list1)-2))
#centered_average([1, 1, 100])
#----------------------------------------#
# Above program in one line after couple of months.
def centered_average(nums):
    return (sum(nums)-min(nums)-max(nums))/(len(nums)-2)
#----------------------------------------#

'''Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7
(every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
'''
def sum67(nums):
  i = 0
  s = 0
  while i < len(nums):
    if nums[i] == 6:
      while nums[i] != 7:
        i+=1
    else:
      s += nums[i]
    i = i+1
  return s
sum67([1, 2, 2, 6, 99, 99, 7])
#----------------------------------------#
lst = ["A", "B", "C", 2, 4]
del lst[0:-2]
print(lst)
#----------------------------------------#
alien_0 = {'color': 'green', 'points': 5} 
print(alien_0) 
# Change the alien's color and point value. alien_0['color'] = 'yellow' alien_0['points'] = 10 print(alien_0)
#----------------------------------------#
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0)
del alien_0['points']
print(alien_0)
alien_0['results'] = 15
alien_0['rank'] = 1
#----------------------------------------#
for name in alien_0.keys():
    print(name, alien_0[name], end='\n')
#----------------------------------------#
for key, values in alien_0.items():
    name = key
    result = values
    print (name)
    print(result)
#----------------------------------------#
def count_hi(str):
  hi='hi'
  ret=0
  for i in range(0,len(str)-1):
    print(str[i:i+2])
    if str[i:i+2] == hi:
      print('entered')
      ret=ret+1
  return ret
#----------------------------------------#
count_hi('ABChi hi')
#----------------------------------------#
#Return the number of times that the string "code" appears anywhere in the given string, 
#except we'll accept any letter for the 'd', so "cope" and "cooe" count.
#count_code('aaacodebbb') → 1
#count_code('codexxcode') → 2
#count_code('cozexxcope') → 2

def count_code(str):
  count=0
  for i in range (0,len(str)-3):
    print(str[i:i+2]+"_"+str[i+3])
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      print(str[i:i+2]+"_"+str[i+3])
      count=count+1
  return count
count_code('codexxcode')
#----------------------------------------#
import re


def count_code(str):
    exp = '^co[a-z|A-Z]e$'
    count = 0
    for i in range(len(str) - 1):
        if re.match(exp, str[i:i + 4]):
            count = count + 1

    return count
count_code('cozexxcope')
#----------------------------------------#
#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True

def end_other(a, b):
  if a.lower() in b.lower()[-len(a):]:
    return True
  elif b.lower() in a.lower()[-len(b):]:
    return True
  else:
    return False
#----------------------------------------#
def end_other1(a, b):

    a1 = a.lower()
    b1 = b.lower()
 
    if a1.endswith(b1) or b1.endswith(a1):
        return True
    else:
        return False
end_other1('abc', 'abXabc')
#----------------------------------------#
import re
def xyz_there(str):
 return str.count('.xyz') != str.count('xyz')
xyz_there('abcdxyz') 
#----------------------------------------#
def sum13(nums):
  sum = 0
  if len(nums) == 0:
    return 0
  else:
#    for i in nums:
#        if i != 13:
#            sum+=i
#    return sum
    i = 0
    while i < len(nums):
      #print(i, 'value position is ',nums[i])
      if nums[i]==13: #or nums[i-1] == 13:
        #print('enter the 13 block')
        i = i+1
      else:
        #print ('sum is added to',nums[i] )
        sum = sum+nums[i]
        i = i+1
    return sum
sum13([1, 2, 13, 2, 1, 13])
#----------------------------------------#
def has22(nums):
  for i in range(0,len(nums)-1):
    print(nums[i],nums[i+1])
    if nums[i] == 2 and nums[i+1] == 2:
      print(nums[i],nums[i+1])
      return True
  return False
has22([1, 3, 2, 2])
#----------------------------------------#
#after about 2-3 months, same program, same logic. 
def sum67(nums):
  if len(nums) == 0 :
    return 0
  else:
    i=0
    sum = 0
    while i < len(nums):
      print('inside 1st while ',i)
      if nums[i] == 6:
       # i = i+1
        print('inside if block ',i)
        while nums[i] != 7:
          print('inside 2nd while ',i)
          i = i+1
        i= i+1
      else:
        print('inside else block ',i)
        sum = sum+nums[i]
        i = i+1
    return sum
sum67([1, 2, 2, 6, 99, 99, 7])
#----------------------------------------#
'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. '''
#The below solution is brute force method and time complexity is O(n**2) since two for loops.
class Solution:
    def twoSum(self, List, target):
       for i in range(0,len(List)):
           if target-List[i] in List[i+1:]:
               for j in range(i+1,len(List)):
                   if List[i]+List[j]==target:
                       return [i,j]
       return []
s = Solution()
list1=[1,10,2,7,11,15]
list2 = s.twoSum(list1,9)
print(list2)
#----------------------------------------#
#The below solution is one pass solution with time complexity if O(n) since just one loop.
class Solution:
    def twoSum(self, nums, target):
        ''':type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
        #dictionary = dict()
        dictionary = {}
        pos = 0
        while pos < len(nums):
            if (target - nums[pos]) not in dictionary:
                dictionary[nums[pos]] = pos
                pos += 1
            else:
                return [dictionary[target - nums[pos]], pos]
s = Solution()
list1=[1,10,2,7,11,15]
list2 = s.twoSum(list1,2)
print(list2)
#----------------------------------------#
'''The below solution is one pass solution with time complexity if O(n) since just one loop.
Here we have used enumerate and dictionary to store values
When you use enumerate(), the function gives you back two loop variables:
The count of the current iteration
The value of the item at the current iteration
Just like with a normal for loop, the loop variables can be named whatever you want them to be named. 
You use count and value in this example, but they could be named i and v or any other valid Python names.
Leetcode stats
Runtime: 44 ms, faster than 83.60% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 11.51% of Python3 online submissions for Two Sum.
'''
class Solution:
    def twoSum(self, nums, target):
        dictionary1 = {}
        for i, v in enumerate(nums):
            if target-v in dictionary1:
                return [dictionary1[target-v],i]
            if v not in dictionary1:
                dictionary1[v] = i
        return []
#----------------------------------------#
s = Solution()
list1=[1,10,2,7,11,15]
list2 = s.twoSum(list1,10)
print(list2)
#----------------------------------------#
'''Runtime: 68 ms, faster than 38.52% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.4 MB, less than 16.80% of Python3 online submissions for Palindrome Number.'''
class Solution:
    def isPalindrome(self, x):
        y=0
        z=x
        while (x > 0):
            #print(y)
            y=(y*10)+(x%10)
            x=int(x/10)
        return y==z
s = Solution()
print(s.isPalindrome(1001))
#----------------------------------------#
class twoSum():
    def findSum1(self,list1, num):
        print('entered inside two function ',num)
        dicti = {}
        for i in range(0,len(list1)):
            if (num-list1[i]) in dicti:
                return dicti[num-list1[i]]+1,i+1
            else:
                dicti[list1[i]] = i
                print(dicti)
        return []
    def findThree(self, list2, num):
        print('entered inside function')
        for j in range(0,len(list2)):
            print('j value is',j)
            list3 = [j]
            list3.extend(self.findSum1(list2[j+1:],num-list2[j]))
            if (len(list3) > 1):
                return (list3)
        return []    
two = twoSum()
print(two.findThree([0,1,2,4],7))
#----------------------------------------#