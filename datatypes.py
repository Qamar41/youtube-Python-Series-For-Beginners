                                    # Dataypes in Python


# i) Strings 
    # series of characters , enclosed in qutation marks  " " ,
    #  single or double quotes ' ', " " 
# print(type('hello') , "how are you ? " )

# ii) integers
    # positive or negative whole numbers

    # x= 6 
#     y=-67
# current_year = 2020
# print(type(current_year))

# iii)floats
    # pi =3.1416
# iv)Boolean
    # True
    # False


# v) None
    # nothing = None

# vi)List

'''A list in Python is an ordered collection of values.
     Lists can hold values of different data types, 
    and support operations to add, remove and change values.
     Lists have the type list'''

# names=['Sammar', 'Qamar', 'Umar', '20','22','True']

# vii)Tuple
'''A tuple is an ordered collection of values, similar to a list,
 however it is not possible to add, remove or modify values in a tuple.
  A tuple is created by enclosing values within parantheses ( and ), separated by commas.
  Any data structure that cannot be modified after creation is called immutable.
'''

# fruits = ('apple', 'cherry', 'dates')
# viii)Dictionaries

'''A dictionary is an unordered collection of items. 
Each item stored in a dictionary has a key and value.
Keys are used to retrieve values from the dictionary.
Dictionaries have the type dict.

Dictionaries are often used to store many pieces of information 
e.g. details about a person, in a single variable. 
Dictionaries are created by enclosing key-value pairs within curly brackets { and }.'''

# person1 = {
#     'name': 'John Doe',
#     'sex': 'Male',
#     'age': 32,
#     'married': True
# }

# .....


        # Type Casting


# Need why??

# print ('hello' + str(6))

# Commonly Types
''' i)   str()
    ii)  int()
    iii) float()
    iv)  bool()'''

# String to integer
name = 'Qamar'
check = type(name)
after =int(name)
print(after)
# print(check)
