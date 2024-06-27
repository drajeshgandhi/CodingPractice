#----------------------------------------#
#Python Programming Paranthesis Check 
#Closest to zero 
#String programs
#----------------------------------------#
# Python3 code to Check for 
# balanced parentheses in an expression
def check(expression):
      
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    queue = []
  
    for i in expression:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"
# Driver code
string = "{[]{()}}"
print(string, "-", check(string))
string = "((()"
print(string,"-",check(string))
#----------------------------------------#
open_list = ["[","{","("]
close_list = ["]","}",")"]
  
# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
  
  
# Driver code
string = "{[]{()}}"
print(string,"-", check(string))
  
string = "[{}{})(]"
print(string,"-", check(string))
  
string = "((()"
print(string,"-",check(string))
#----------------------------------------#
Open_List = ['{','(','[']
Close_List = ['}',')',']']

def checkBalance(mystr):
    stack = []
    for i in mystr:
        if i in Open_List:
            stack.append(i)
        elif i in Close_List:
            pos = Close_List.index(i)
            if len(stack) != 0 and ( Open_List[pos]== stack[len(stack) - 1]):
                stack.pop()
        else:
                return "Unbalanced"
    if len(stack) == 0:
        return "balanced"
    else:
        return "Unbalanced"

string1 = "{[]{()}}"
print(string1,'-',checkBalance(string1))

string = "[{}{})(]"
print(string,"-", checkBalance(string))
  
string = "((()"
print(string,"-",checkBalance(string))
#----------------------------------------#
def nextBig(arr1,k):
    #h = -1
    print(arr1.index(k), len(arr1))
    for i in range(arr1.index(k)+1,len(arr1)):
        print(arr1[i],k)
        if arr1[i] > k:
            return arr1[i]
    return -1

arr1 = [13, 7, 6, 12]
#arr1=[4, 5, 2, 25]
p = nextBig(arr1,6)

print("nextBig value of 6 in ", arr1, " is ", p)
#----------------------------------------#
def StringReverseStak(str1):
    stack = []
    str2=''
    for i in str1:
        stack.append(i)
    print(stack)
    while len(stack) != 0:
        str2 += stack.pop()
    print('reverse of ',str1, ' is ', str2)

StringReverseStak("Hello")    
#----------------------------------------#
def closestToZero(ts):
    closest = ts[0]
    a_c = abs(closest)
    for i in ts:
        num = ts[i]
        a_n = abs(num)
        
        if closest > a_n:
            closest = num
        elif a_c == a_n and closest < 0:
            closest = num
    return closest

ts = [7,-10, 13, 8, 4, -7,-12,-3,3,-2,-9, 6,-1, -6,7]
print('the closest value is ', closestToZero(ts))
#we compare each and every element in the list with one random number (here the first in the list) and then, compare the
#absolute of first ele and absolute of current ele in the loop, get the minimum of the two, assign original value from list 
#as closest
#----------------------------------------#
def clap(str1):
    for c in list(str1):
        print(c)

str1="Hello"
clap(str1)
#----------------------------------------#
print(3//3)
#----------------------------------------#