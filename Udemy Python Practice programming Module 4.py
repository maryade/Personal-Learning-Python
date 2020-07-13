# # creating a list
# newlist = [1,2,3,4,5]
# print(newlist)
#
# fruits = ['fig','apple','grapes']
# print(fruits)

# fruitsnew = ['fig','apple','grapes', 3, True, None]
# print(fruitsnew)

# accessing list item with indexing
# print(fruits[1]) #apple
# print(fruits[0]) #fig
#
# changing an item in fruits list
# fruits[0] = 'lemon'
# print(fruits[0])

# print all items one my one...for loop
# for fruit in fruits:
#     print(fruit)

# display number of items in list
# print(len(fruits)) #3

#in keyword to check if item exists
# if 'orange' in fruits:
#     print("yes, it's in fruit list")
# else:
#     print("no,it's not in fruit list")

# adding elements
# fruits.append('orange')
# print(fruits)

# add item to a specified index
# fruits.insert(1,'lemon')
# print(fruits)

# remove item in a list
# fruits.remove('fig')
# print(fruits)
# fruits.pop()# if an index is not specified
# fruits.pop(0) #first item is removed
# del fruits[0] #delete first item
# del fruits #fruit list has been removed
# fruits.clear() #empties list

# create a copy of the list
# newlist=fruits.copy()
# print(newlist)

# make a new list my constructor
# newlist = list(('apple','lemon','orange'))
# newlist.reverse() #reverse the list
# print(newlist)

#Tuples are ordered and unchangeable
# creating a tuple
# fruits = ('lemon','orange','apple')
# print(fruits[0]) #lemon
# print(fruits[1]) #orange

# display item one by one
# for fruit in fruits:
#     print(fruit)

# in keyword to check if item exists
# if 'fig' in fruits:
#     print("yes, it's in fruit tuple")
# else:
#     print("no,it's not in fruit tuple")
#

# number in fruits
# print(len(fruits))

# tuple cant be changed
# fruits[0]='banana'

# cant remove an item from a tuple but can remove the whole tuple
# del fruits[1]
# del fruits
# print(fruits) #error

# creating a tuple by using constructor for tuple
# fruits=tuple(('banana','fig','lemon'))
# print(fruits)
# x = fruits.index('fig') #search tuple for a specific item and return position #1
# print(x)

# sets in python are unordered and unindexed
# fruits = {'fig','apple','lemon'}
# print(fruits) #position changes everytime you run print so can't ask for an index

# looping through items
# for fruit in fruits:
#     print(fruit)

# check if item exists
# print('apple' in fruits) #prints true if yes and false in no

# adding items
# fruits.add('banana')
# print(fruits)

# add multiple items
# fruits.update(['banana','grapes'])
# print(fruits)

# number of items
# print(len(fruits))

# remove an item from a set
# fruits.remove('apple')
# print(fruits)
# fruits.discard('apple')
# print(fruits)

# remove last item from a set using pop method
# x  = fruits.pop()
# print(x)
# print(fruits)

# clear the set
# fruits.clear()
# print(fruits) #get an empty set

# delete fruit sets
# del fruits
# print(fruits) #error

# creating a set by set constructor
# newfruits=set(('apple','fig','lemon'))
# print(newfruits)
# copyfruits = newfruits.copy()
# print(copyfruits)

# Dictionaries are written in {} and have keys and values
# creating a dictionary
user = {
    "name" : 'first user',
    'age': 34,
    'job' : 'teacher'
}
# print(user)

# access items
# item = user['age']
# item = user.get('name')
# print(item)

# changing values in user dictionary
# user['age'] = 45
# print(user)

# printing keys one by one
# for item in user:
#     print(item) #prints only keys

# printing all values
# for value in user:
#     print(user[value]) #prints values
# or
# for value in user.values():
#     print(value)

# printing both values and keys
# for key, value in user.items():
#     print(key,value)

# can separate with keys from values with colons using
# for key, value in user.items():
#     print(key,':',value)