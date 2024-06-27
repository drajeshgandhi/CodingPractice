#----------------------------------------#
#Python Programming 
#List
#Nth Smallest number
#Triplet problems
#Smallest Prime Palindrome
#Binary Search Tree
#Binary Tree 
#QuickSort
#Classes
#----------------------------------------#

# Python program to find unique triplets
# that sum up to a given value.
 
# Function to find unique triplets that
# sum up to a given value.
def findTriplets(nums, n, Sum):
    i = 0
    j = 0
    k = 0
 
    # list to store all unique triplets.
    triplet = []
 
    # list to store already found triplets
    # to avoid duplication.
    uniqTriplets = []
 
    # Variable used to hold triplet
    # converted to string form.
    temp = ""
 
    # Variable used to store current
    # triplet which is stored in vector
    # if it is unique.
    newTriplet = [0, 0, 0]
 
    # Sort the input array.
    nums.sort()
 
    # Iterate over the array from the
    # start and consider it as the
    # first element.
    for i in range(n - 2):
         
        # index of the first element in
        # the remaining elements.
        j = i + 1
 
        # index of the last element.
        k = n - 1
 
        while(j < k):
           
            # If sum of triplet is equal to
            # given value, then check if
            # this triplet is unique or not.
            # To check uniqueness, convert
            # triplet to string form and
            # then check if this string is
            # present in set or not. If
            # triplet is unique, then store
            # it in list.
            if(nums[i] + nums[j] + nums[k] == Sum):
                temp = str(nums[i]) + ":" + str(nums[j]) + ":" + str(nums[k])
                if temp not in uniqTriplets:
                    uniqTriplets.append(temp)
                    newTriplet[0] = nums[i]
                    newTriplet[1] = nums[j]
                    newTriplet[2] = nums[k]
                    triplet.append(newTriplet)
                    newTriplet = [0, 0, 0]
 
                # Increment the first index
                # and decrement the last
                # index of remaining elements.
                j += 1
                k -= 1
                 
            # If sum is greater than given
            # value then to reduce sum
            # decrement the last index.
            elif(nums[i] + nums[j] + nums[k] > Sum):
                k -= 1
                 
            # If sum is less than given value
            # then to increase sum increment
            # the first index of remaining
            # elements.
            else:
                j += 1
 
    # If no unique triplet is found, then
       # return 0.
    if(len(triplet) == 0):
        return 0
    else:
        return triplet
    # Print all unique triplets stored in
    # list.
    #for i in range(len(triplet)):
#        print(triplet[i], end = ", ")
#    return 1
 
# Driver Code
nums = [12, 3, 6, 1, 6, 9]
n = len(nums)
Sum = 24
 
# Function call
if(not findTriplets(nums, n, Sum)):
    print("No triplets can be formed.")
else:
    print(findTriplets(nums, n, Sum))
#----------------------------------------#
def findTriplet(nums, n, Sum):
    #print('entered inside the function')
    nums.sort()
    #i=j=k=0
    temp_triplet = [0,0,0]
    unique_triplet=[]
    for i in range(n-2):
        print('inside forloop', i)
        j = i+1
        k = n-1
        while(j<k):
            print('inside while',nums[i],nums[j],nums[k])
            if nums[i]+nums[j]+nums[k]==Sum:
                temp_triplet[0]=nums[i]
                temp_triplet[1]=nums[j]
                temp_triplet[2]=nums[k]
                print('successful triplet is',temp_triplet)
                if temp_triplet not in unique_triplet:
                    unique_triplet.append(temp_triplet)
                j=j+1
                k=k-1
                temp_triplet=[0,0,0]
            elif nums[i]+nums[j]+nums[k] > Sum:
                k = k-1
            else:
                j = j+1
    
    return unique_triplet

nums = [12, 3, 6, 0, 6, 9]
n = len(nums)
Sum = 18
print('value is',findTriplet(nums,n,Sum))
#----------------------------------------#
'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = []
Output: []
Example 3:
Input: nums = [0]
Output: []
Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
Runtime: 5396 ms, faster than 11.03% of Python3 online submissions for 3Sum.
Memory Usage: 18 MB, less than 27.05% of Python3 online submissions for 3Sum.
Time Complexity O(n2)
Space Complexity O(n)'''
class Solution:
    def threeSum(self, nums) :
        #print('entered inside the function')
        nums.sort()
        n  = len(nums)
        Sum = 0
        #i=j=k=0
        temp_triplet = [0,0,0]
        unique_triplet=[]
        for i in range(n-2):
            #print('inside forloop', i)
            j = i+1
            k = n-1
            while(j<k):
                #print('inside while',nums[i],nums[j],nums[k])
                if nums[i]+nums[j]+nums[k]==Sum:
                    temp_triplet[0]=nums[i]
                    temp_triplet[1]=nums[j]
                    temp_triplet[2]=nums[k]
                    #print('successful triplet is',temp_triplet)
                    if temp_triplet not in unique_triplet:
                        unique_triplet.append(temp_triplet)
                    j=j+1
                    k=k-1
                    temp_triplet=[0,0,0]
                elif nums[i]+nums[j]+nums[k] > Sum:
                    k = k-1
                else:
                    j = j+1

        return unique_triplet

s= Solution()
nums=[-1,0,1,2,-1,-4]
k = s.threeSum(nums)
print(k)
#----------------------------------------#
'''Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.
Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Constraints:
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
Runtime: 5396 ms, faster than 11.03% of Python3 online submissions for 3Sum.
Memory Usage: 18 MB, less than 27.05% of Python3 online submissions for 3Sum.
Time Complexity O(n2)
Space Complexity O(n)'''
class Solution:
    def threeSumClosest(self, nums, target) :
        #print('entered inside the function')
        nums.sort()
        curr=float('inf')
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while(j<k):
                temp = nums[i]+nums[j]+nums[k]
                if abs(target-temp) < abs(curr):
                    curr= target - temp
                if temp > target:
                    k = k-1
                else:
                    j = j+1
            if curr==0:
                    break
        return target-curr

s= Solution()
nums=[-1,2,1,-4]
#nums = [1,1,1,0]
k = s.threeSumClosest(nums,100)
print(k)
#----------------------------------------#
curr=float('inf')
if 3 < abs(curr):
    print ('yes')
print(abs(curr))
#----------------------------------------#
list1=[0,1,4,2,3,10,21,13,32,29,19,15,7,35] 
list2=[] 
list3=[] 
for i in range(len(list1)-1): 
    list2.append(str(list1[i]))

list2.sort() 
for i in range(len(list2)-1): 
    list3.append(int(list2[i]))

print(list3[3])
print(list3)
#----------------------------------------#
'''Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.
Note: 1 ≤ k ≤ n ≤ 109.
Example:
Input:
n: 13   k: 2
Output:
10
Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.'''
class Solution:
    def findKthNumber(self, n, k):
        list1 = []
        list2 = []
        for i in range(1,n+1):
            list1.append(str(i))
        list1.sort()
        #print(list1)
        for i in range(0,n):
            list2.append(int(list1[i]))
        
        print(list2)
        return list2[k-1]

s= Solution()
p=s.findKthNumber(13,2)
print(p)
#----------------------------------------#
'''Find the smallest prime palindrome greater than or equal to N.
Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 
For example, 2,3,5,7,11 and 13 are primes.
Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 
For example, 12321 is a palindrome.
Example 1:
Input: 6
Output: 7
Example 2:
Input: 8
Output: 11
Example 3:
Input: 13
Output: 101
Note:
1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8
Name Error: function name not found error.
1) we need to call the function with self.function_name()
2) the called function shuold be defined prior to caller function since Python is a top down read happens.
'''
class Solution:
    def pali(self,p):
        #y=0
        #z=x
        #while (x > 0):
            #print(y)
       #     y=(y*10)+(x%10)
       #     x=int(x/10)
       # return y==z
       # print('entered pali function value is',p)
        m=p
        sum=0
        while(p>0):
        #    print('inside pali while loop')
            sum = (10*sum)+(p%10)
            p=int(p/10)
        if(sum == m):
         #   print('inside pali if cond')
            return True
        else:
          #  print('inside pali else cond')
            return False
    def prime(self,p):
        #print('entered prime function value is',p)
        sum = 0
        for i in range(1,p+1):
         #   print('inside prime for loop')
            if p%i==0:
                sum+=i
        if (sum==p+1):
          #  print('inside prime if condition')
            return True
        else:
           # print('inside prime else condition sum is=',sum,': and p = ', p)
            return False
    def primePalindrome(self, n):
        for k in range(n+1,10**8):
            bool1= self.pali(k)
            bool2= self.prime(k)
            if( bool1 and bool2):
                return k
                break
s=Solution()
num=s.primePalindrome(13)
print('the closest next prime_palindrome is',num)
#----------------------------------------#
'''Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''
def longSubString(str):
    k=""
    num=1
    dictionary1 = {}
    for i in range(len(str)):
        for j in range(i):
            if str[j] not in k:
                k=k+str[j]
            else:
                dictionary1[i] = k
    for key in dictionary1:
        if len(dictionary1[key]) > num:
                num = len(dictionary1[key])
    if str == "":
        return 0
    else:
        return num
        
            

#for i in range(len(str)):
    #if (i>0 && str[i] in str[0:i-1]):
        #anchor = i
    #result = Math.max(result, i-anchor+1)
    #https://www.youtube.com/watch?v=jSvoE-_Yhs4
##        for i, v in enumerate(nums):
#            if target-v in dictionary1:
#                return [dictionary1[target-v],i]
#            if v not in dictionary1:
#                dictionary1[v] = i
 
m = longSubString('au')
print(m)
#----------------------------------------#
'''Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray).
The subsequence must be strictly increasing.
A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is 
[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
Example 1:
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:
Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
Constraints:
0 <= nums.length <= 104
-109 <= nums[i] <= 109
Runtime: 128 ms, faster than 5.37% of Python3 online submissions for Longest Continuous Increasing Subsequence.
Memory Usage: 15.3 MB, less than 58.93% of Python3 online submissions for Longest Continuous Increasing Subsequence.

notes: this is a basic question related to sliding window problem model. In this model, we use two variables
1. anchor (to start position)
2. an index value to increase the window (i, which increases with every iteration)
we iterate just once through entire list/array so time complexity is O(n) and space complexity is also O(n)
core logic works like below
 if(i>0 and list1[i-1] >= list1[i]): # we start with second ele since we compare the current ele with previous ele, 
    anchor = i     #if current ele is > prev ele, then we increase the anchor value to current index, a fresh window will star
result = max(result, i-anchor+1) #for every index value, we compare the result, (i - anchor) whichever is >, we return it
#i-anchor + 1, here +1 is added because index starts from 0, so to return actual position of the value we add 1

'''
class Solution:
    def longestContSequence(self,list1):
        anchor = result = i = 0
                
        for i in range (0,len(list1)):
            if(i>0 and list1[i-1] >= list1[i]):
                anchor = i
            result = max(result, i-anchor+1)
        
        return result
        
s = Solution()
k = s.longestContSequence([1,3,5,4,7,8,10,3,4,5])
#k = s.longestContSequence([1])
print(k)
#----------------------------------------#
'''Binary Search Tree: Any tree with a two child nodes is a Binary Tree'''
import math
def BinSearch(arr, key):
    l=1
    h=len(arr)
    mid = math.ceil((l+h)/2)
    while (l <= h):
        if (key == arr[mid]):
            return mid
        elif(key < arr[mid]):
            h=mid-1
        else:
            l=mid+1
    return 0
A=[1,2,3,4,5,6]
k=BinSearch(A,5)
print('element found at position',k)
#----------------------------------------#
# Python3 program to illustrate deletion in a Binary Tree
# class to create a node with data, left child and right child.
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
  
# Inorder traversal of a binary tree
def inorder(temp):
    if(not temp):
        return
    inorder(temp.left)
    print(temp.data, end = " ")
    inorder(temp.right)

    
def preorder(temp):
    if not(temp):
        return
    print(temp.data, end = " ")
    preorder(temp.left)
    preorder(temp.right)

def postorder(temp):
    if not(temp):
        return
    postorder(temp.left)
    postorder(temp.right)
    print(temp.data, end = " ")

def bfs(temp):
        node = temp
        #d = []
        queue = []
        queue.append(node)
        while len(queue)!= 0:
            node = queue.pop(0)
            #d.append(node.data)
            print(node.data, end = " ") 
            if(node.left): queue.append(node.left)
            if(node.right): queue.append(node.right)
            
        #return data
        
      
# function to delete the given deepest node (d_node) in binary tree
def deleteDeepest(root,d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
  
# function to delete element in binary tree
def deletion(root, key):
    if root == None :
        return None
    if root.left == None and root.right == None:
        if root.key == key :
            return None
        else :
            return root
    key_node = None
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node :
        x = temp.data
        deleteDeepest(root,temp)
        key_node.data = x
    return root

# Driver code
if __name__=='__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.left.left.left = Node(4)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree inorder traverse:")
    inorder(root)
    key = 11
    #root = deletion(root, key)
    print()
    print("The tree preorder traverse ;")
    preorder(root)
    print()
    print("The tree postorder traverse ;")
    postorder(root)
    print()
    print('BFS traverse is ')
    bfs(root)
#----------------------------------------#
# Python program to insert element in binary tree
class newNode():
 
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
         
""" Inorder traversal of a binary tree"""
def inorder(temp):
 
    if (not temp):
        return
 
    inorder(temp.left)
    print(temp.key,end = " ")
    inorder(temp.right)
 
 
"""function to insert element in binary tree """
def insert(temp,key):
 
    if not temp:
        root = newNode(key)
        return
    q = []
    q.append(temp)
 
    # Do level order traversal until we find
    # an empty place.
    while (len(q)):
        temp = q[0]
        q.pop(0)
 
        if (not temp.left):
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)
 
        if (not temp.right):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)
     
# Driver code
if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(15)
    root.right.right = newNode(8)
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root)
 
    key = 12
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)
#----------------------------------------#
# Python Program to find the size of binary tree
  
# A binary tree node
class Node:
  
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
  
# Computes the number of nodes in tree
def size(node):
    if node is None:
        return 0 
    else:
        return (size(node.left)+ 1 + size(node.right))

# Returns maximum value in a
# given Binary Tree
def findMax(root):
  
    # Base case
    if (root == None):
        return float('-inf')
  
    # Return maximum of 3 values:
    # 1) Root's data 2) Max in Left Subtree
    # 3) Max in right subtree
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if (lres > res):
        res = lres
    if (rres > res):
        res = rres
    return res  
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
  
s = size(root)    
print ('Size of the tree is ', s)

maxi = findMax(root)
print('Maximum element is', maxi)
#----------------------------------------#
'''Quick Sort: i , j , pivot. we search else greater than i and less than j and swap them if i< j, 
if they cross (i>j), we swap pivot and j'''

class quickSorting:
    def swap (self, A, l, h):
        temp = A[l]
        A[l]=A[h]
        A[h]=temp
        
    def partition(self, A, l, h):
        i = l 
        j = h-1
        pivot = A[l]
        
        while (i < j):
            while True:
                i=i+1
                if (A[i]>=pivot):
                    break
                    
            while True:
                j=j-1
                if(A[j]>=pivot):
                    break
            self.swap (A,i,j)
        if (i > j):
            self.swap (A,l,j)
            print("j actual value is:",j)
            return j
    
    def quicksort(self, l, h, arr):
        print (l, " ", h)
        if (l < h):
            j = self.partition(arr,l,h)
            print ("j value is:", j)
            self.quicksort(l,j,arr)
            self.quicksort(j+1,h,arr)

k = quickSorting()
list1=[10,16,8,12,15,6,3,9,5]
print(list1)
k.quicksort(0,9,list1)
print(list1)
#----------------------------------------#
ab = { 'raj':'drg@mail.com',
     'krishna':'dk@gmail.com'}
for i, v in ab.items():
    print (i, "-->", v)
#----------------------------------------#
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        A string is good if it can be formed by characters from chars (each character can only be used once).

        Return the sum of lengths of all good strings in words.



        Example 1:

        Input: words = ["cat","bt","hat","tree"], chars = "atach"
        Output: 6
        Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
        Example 2:

        Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
        Output: 10
        Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


        Constraints:

        1 <= words.length <= 1000
        1 <= words[i].length, chars.length <= 100
        words[i] and chars consist of lowercase English letters.

        """
        s = 0
        for i in words:
          #print('word is :',i)
          p=0
          for j in range(0,len(i)) :
            #print(i[j])
            if i[j] in chars:
                        p+=1
                        #print('char found and p value is increased to: ', p)
            else:
                    continue
                    #print('char not found and p value is still same: ', p)
            #print('length is: ',len(i), ', count is:', p)
            if len(i)==p:
                #print('length is: ',len(i), ', count is:', p)
                s+= len(i)       
        return s   
#----------------------------------------#
words = ["cat","bt","hat","tree"]
chars = "atach"
words1=["hello","world","leetcode"]
chars1="welldonehoneyr"
S= Solution()
count=S.countCharacters(words1, chars1)
print('total chars are',count)
#----------------------------------------#

'''Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7
(every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
'''
def sum67(list):
    flag= True
    sum=0
    for i in range(0,len(list)):
        #print('i value is', i)
        if list[i] == 6 :
            #print('entered the 6 if block')
            flag = False
            continue
        elif list[i]== 7:
            flag = True
            continue
        while flag:
            #print(i, list[i])
            sum+=list[i]
            break
    return sum            
    
print(sum67([1,2,2]))        
print(sum67([1, 2, 2, 6, 99, 99, 7])) 
print(sum67([1, 1, 6, 7, 2]))
#----------------------------------------#
'''You have d dice and each die has f faces numbered 1, 2, ..., f. You are given three integers d, f, and target.

Return the number of possible ways (out of fd total ways) modulo 109 + 7 to roll the dice so the sum of the face-up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000'''

def dice_target(dice, face, target):
    count = 0
    mod = 1000000000+7
    print(mod)
    '''sum = 0
    for d in range(1,dice+1):
        for f in range(1,face+1):
            if sum+f == target:
                count+= 1'''
    if target > dice*face :
        return False
    elif dice%target <= face:
        return True
    else :
        return False 
    #print(count)
print(dice_target(1,2,3))
#----------------------------------------#
'''Problem Statement: Given an array of binary digits, 0 and 1, sort the array so that all the zeros are at one end and all ones
are at the other.
Which end does not matter. To sort the Array, swap any two adjacent elements. Determine the minimum number of swaps to sort the 
array.
Example: arr = [0,1,0,1] output = 1
switching elements 1 and 2, yields [0,0,1,1] a sorted array.
Example: arr = [1,1,1,1,0,1,0,1] output = 3 , [1,1,1,1,1,0,0,1] →[1,1,1,1,1,0,1,0] →[1,1,1,1,1,1,0,0]


For the first pass, we only count how many "1" in the array, we also count how many swaps we need to make all 0 in the beginning.
We go from left to right. For each "0', if we know how many 1 before it, we will know how many swaps we need. 
That is the meaning of dis.

After we finish the first pass, we know how many "1" in the array, use total to minus that we will get how many 0 in there.
To get the swaps for all "1" go to the left, we calculate the maximum swaps time(two situations: move all 1 on left + move 
all 1 on right) first and then minus the situation that "moving all 1 to right". That will be dis1 = count1 * count0 - dis

In the end, we compare which swap strategy will have minimum swaps.
My notes:dis 0 is to move all 0's to right, dis1 is to move all 1's to right. Main logic is figuring out dis0 first based on 1s 
encountered. Then, from toal moves (i.e., total ele * no of moves for zeros to move right) minus moves needed for zeros to move 
right.

'''

def minMoves(arr):
  count1 = 0
  dis0 = 0 
  for num in arr:
      if num ==1:
          count1+=1
          #print('count1 is: ', count1)
      if num==0:
          dis0+=count1
          #print('dis0 is: ', dis0)
          
  count0 = len(arr) - count1
  #print('after for loop, count0 is:', count0)
  
  dis1 = count1 * count0 - dis0
  #print('after for loop, dis1 is:', dis1)
  #print('minimum of dis0, dis 1 is:', dis0, dis1)
  return min(dis0, dis1)
    
print('the number of swaps required is: ', minMoves([1, 1, 1, 1, 0, 0, 0, 0]))
#----------------------------------------#
def Run(nums):
    sum = 1
    prev = 1
    for i in range(1,len(nums)):
        if nums[i - 1] == nums[i] + 1:
            sum += prev + 1
            prev+=1
            print('after :', i,' iteration for element :', nums[i], 'the values of sum, prev are :',sum, prev)
        else :
            prev = 1
            sum+=1
            print('after :',i,' iteration for element :', nums[i], 'inside the else block the values of sum, prev are :',sum, prev)
    return sum
print(Run([4,3,5,4,3]))
#----------------------------------------#
def password_Strength(word):
    sum = 1
    prev = 1
    for i in range(1,len(word)):
        if nums[i - 1] == nums[i] + 1:
            sum += prev + 1
            prev+=1
            print('after :', i,' iteration for element :', nums[i], 'the values of sum, prev are :',sum, prev)
        else :
            prev = 1
            sum+=1
            print('after :',i,' iteration for element :', nums[i], 'inside the else block the values of sum, prev are :',sum, prev)
    return sum
print(Run([4,3,5,4,3]))
#----------------------------------------#
class Student: 
    def __init__(self):
        print("Engine Started")
        self.name = "Corolla"
        self.__make = 'Toyota'
        self._model = 2017
#----------------------------------------#
std = Student()
print(std.name)
print(std._model)
#----------------------------------------#
import array
a = array.array('i', [1, 2, 3])
for i in a:
    print(i, end=' ')    #OUTPUT: 1 2 3
b = [10,20, 'hello', 10.5, 'world']
print('\n')
for j in b:
    print(j, end = ' ')
a = array.array('i', [1, 2, 'string'])    #OUTPUT: TypeError: an integer is required (got type str)
a = [1, 2, 'string']
for i in a:
   print(i, end=' ')    #OUTPUT: 1 2 string
#----------------------------------------#
list1=[3,4,5,6,7,8]
list1.pop(1)
print(list1)
print("Hello World"[::-1])
#----------------------------------------#
func = lambda a, b : (a ** b)
print(func(float(10),20))
#----------------------------------------#
list1 = ['s', 'r', 'a', 's'] 
list2 = ['a', 'a', 'n', 'h']
print(["".join([i, j]) for i, j in zip(list1, list2)])
print(time.time())
#----------------------------------------#
class Person:
   def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name

first_name = "XYZ"
person = Person(first_name, "ABC")
first_name = "LMN"
person.last_name = "PQR"
print(person.first_name, person.last_name)
#----------------------------------------#
class X:
    def __init__(self):
        self.__num1 = 5
        self.num2 = 2

    def display_values(self):
        print(self.__num1, self.num2)
class Y(X):
    def __init__(self):
        super().__init__()
        self.__num1 = 1
        self.num2 = 6 
obj = Y()
obj.display_values()
#----------------------------------------#
