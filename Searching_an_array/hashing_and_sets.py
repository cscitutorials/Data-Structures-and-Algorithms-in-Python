"""
Set is an unordered and unindexed collection of items.
The elements in a set are unique.
Set does not allow duplicated elements.
A set itself may be modified, but the elements contained in the set must be of an immutable type.

A set can be created in two ways.
First, you can define a set with the built-in set(<iter>) function:
Note curly brackets are dictionaries and can be used as sets {} and parenthesis are tuples.
Sets is declared by the function set()
Sets allow only one argument
"""
my_list = [1,3, 7, 5]
s = set(my_list)
x = {1:4,2:8, 3:0, 5:0,}
print(type(x))
s.add(4)#Adding elements to a set
print(s)
y = {1}
print(type(y))
"""
Since Sets are unordered, to ascess elements in the sets,
you will have to use a for loop.

"""
for elements in s:
    print(elements)
"""
multiple items can be added to a set by using the update() method:
Get the Length of a Set by using the len() method.
Remove an item in a set by using the remove(), or the discard() method.
can also use the pop(), method to remove an item, but this method
will remove the last item
The clear() method empties the set:
The del keyword will delete the set completely:
the union() method that returns a new set containing all items from both sets,
or the update() method that inserts all the items from one set into another:
"""

#### DICTIONARIES #### DICTIONARIES ########
"""
Python dictionaries are declared by using curly braces.
It is the same for declaring sets in python.
Unlike sets, Dictionaries must have a key and a value as pairs. This is a must
and any alteration might result to syntax error.
A dictionary are unordered, changeable and indexed
Dictionaries are used to count the frequencies of elements in an array
"""
print("Start of dictionary")
my_dictionary = {3:2, 4:0, 5:2, 6:9, 1:10}
#A key
# Print the value of an item in a dictionary by saying
print(my_dictionary[3]) # You can also say print(my_dictionary.get(3))
print(my_dictionary.get(4))
#You can change the value of a dictionary item
# Dictionaries can be used for statistics, for example a number and a frequencies
#To get the values of a dictionary, use the .values() method
my_dictionary[3] = 12
x= (my_dictionary.values())
#To print the dictionary items, use the .items()
y = my_dictionary.items()
print(y)
print(my_dictionary)
#Looping through the dictionary.
#To print out all the keys.
keys = []
for i in my_dictionary:
    keys.append(i)
print(type(keys))
keys.sort()
print(keys)
#Print all values in a dictionary 1 by 1
for i in my_dictionary:
    print(my_dictionary[i])
#Print all keys in a dictionary:
print('keys')
for i in my_dictionary:
    print(i)
#Last problem. Giving an array of integers, find the most frequent number
arr = [1,1,1,2,3,4,1,2,4,2,2,3,2,5,2,2,3,5,2,3,1]
my_dict = {}
for i in arr:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
max_value = 0
item = ""
for i in my_dict:
    if my_dict[i] > max_value:
        max_value = my_dict[i]
        item = i
print('Max is {} and the number is {} '.format(max_value, item))


print(my_dict)
