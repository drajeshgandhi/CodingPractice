#----------------------------------------#
#This file contains some of the beginner Level Python Programs
#Dictionaries
#Json Files processing
#----------------------------------------#
#Storing lists in a dictionary # Store multiple languages for each person. 
fav_languages = { 'jen': ['python', 'ruby'], 
                 'sarah': ['c'], 
                 'edward': ['ruby', 'go'], 
                 'phil': ['python', 'haskell'], } 
# Show all responses for each person. 
for name, langs in fav_languages.items(): 
    print(name + ": ") 
    for lang in langs: 
        print("- " + lang)
#----------------------------------------#
#Preserving the order of keys and values 
#Standard Python dictionaries don't keep track of the order in which keys and values are added; 
#they only preserve the association between each key and its value. If you want to preserve the order in which 
#keys and values are added, use an OrderedDict.

from collections import OrderedDict 
# Store each person's languages, keeping # track of who respoded first. 
fav_languages = OrderedDict() 
fav_languages['jen'] = ['python', 'ruby'] 
fav_languages['sarah'] = ['c'] 
fav_languages['edward'] = ['ruby', 'go'] 
fav_languages['phil'] = ['python', 'haskell'] 
# Display the results, in the same order they # were entered. 
for name, langs in fav_languages.items(): 
    print(name + ":") 
    for lang in langs: print("- " + lang)
#----------------------------------------#
'''Preventing a function from modifying a list The following example is the same as the previous one, except the original 
list is unchanged after calling print_models(). '''
def print_models(unprinted, printed): 
    """3d print a set of models.""" 
    while unprinted: 
        current_model = unprinted.pop() 
        print("Printing " + current_model) 
        printed.append(current_model) 
# Store some unprinted designs, # and print each of them. 
unprinted = ['phone case', 'pendant', 'ring'] 
printed = [] 
print_models(unprinted, printed) 
print("\nOriginal:", unprinted) 
print("Printed:", printed)
#----------------------------------------#
#Collecting an arbitrary number of keyword arguments 
def build_profile(first, last, **user_info): 
    """Build a user's profile dictionary.""" 
# Build a dict with the required keys. 
    profile = {'first': first, 'last': last} 
    # Add any other keys and values. 
    for key, value in user_info.items(): 
        profile[key] = value 
    return profile 
# Create two users with different kinds # of information. 
user_0 = build_profile('albert', 'einstein', location='princeton') 
user_1 = build_profile('marie', 'curie', location='paris', field='chemistry') 
print(user_0) 
print(user_1)
#----------------------------------------#
#Python program to read a json file
import json
#Opening a Json file
f=open('example.json',)
#return json object as a dictionary
data = json.load(f)
for item in data:
    print(item, data[item])
print("Resources: ", str(data['Resources']))
k=data['Resources']['Catpics']
for i in k:
    print(i, k[i])
#----------------------------------------#
import json

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])
#----------------------------------------#
#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) 
#and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. 
#This is a little harder than it looks and can be done without any loops. 
#make_bricks(3, 1, 8) → True
#make_bricks(3, 1, 9) → False
#make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
    if goal > big*5+small :
      #print ('entered step-1')
      return False
      if (goal%big) != 0  and (goal%big) > small:
        #print ('entered step-2')
        return False
    else:
      #print ('entered step-8')
      return True 
'''alternate approach on 09/21/2021 below
def make_bricks(small, big, target):
	if target > small+big*5 :
		return False
	elif target%big <= small:
		return True
	else :
		return False 
make_bricks(3, 2, 10)
'''
#----------------------------------------#
#Solution: If all big*5+small is not able to make its a false case. 
#If the reminder of goal after mod by 5 > small, then its false
#otherwise, we should be able to make it. 
#----------------------------------------#
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
#----------------------------------------#