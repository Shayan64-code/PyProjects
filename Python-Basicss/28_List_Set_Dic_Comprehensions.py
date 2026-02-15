############ List Comprehension
### List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

list5 = ["Papaya", "Grapes", "Apple", "Orange", "Kiwi"]

# newlist = [x for x in list5 if x != "Apple"]
# print(newlist)

# newlist1 = []
# for x in list5:
#     if "a" in x:                                            
#         newlist1.append(x)
# print(newlist1)
  
# newlist = [print(x) for x in list5 if "a" in x]                #This is list comprehension ## writing whole code of above in one line
#                   #OR
# newlist = [x for x in list5 if "a" in x or "A" in x]
# print(newlist)

# newlist = [x for x in range(10) if x < 5]
# print(newlist)

# newlist = [x.upper() for x in list5]
# print(newlist)

# newlist = ['hello' for x in list5]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if x != "banana"]                     #These types are all filtering comprehensions
# print(newlist)

# newlist = [x if x != "banana" else "orange" for x in fruits]       #These are conditional comprehensions #Syntax differ
# print(newlist)

############ Set Comprehension

# s0 = set([1, 2, 3, 4, 5, 2, 3])
# print(s0)
# #OR
# s = {1, 2, 3, 4, 5, 2, 3}
# print(s0)

# even = {x for x in s0 if x % 2 == 0}
# print(even)

########## Dictionary Comprehension

cities = ["Karachi", "Mumbai", "New York", "Paris"]
countries = ["Pakistan", "India", "USA", "France"]

z = zip(cities, countries)
# print(z)   # object of zip

# [print(x) for x in z] # zip join two lists and print them

d = {city: country for city, country in z}
print(d)

#or

d2 = {city: country for city, country in zip(cities, countries)}
print(d2)