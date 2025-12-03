# ####### Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# # thisset = {"apple", "banana", "cherry"}
# # print(thisset)

# thisset = {"apple", "banana", "cherry", "apple"}              #duplicate item cannot be included
# print(thisset)

# thisset = {"apple", "banana", "cherry", True, 1, 2}            #True and 1 is same value and False and 0 is also
# print(thisset)

# myset = {"apple", "banana", "cherry"}
# print(type(myset))

# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets #Using the set() constructor
# print(thisset)

# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)
# print("banana" not in thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.add("Orange")
# print(thisset)

# thisset2 = {"Potato", "Tomato", "Onion"}

# thisset2.update(thisset)
# print(thisset2)

# thisset = {"apple", "banana", "cherry"}        #Set
# mylist = ["kiwi", "orange"]                    #List

# thisset.update(mylist)
# print(thisset)

################## Removing Items

thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")                        #If the item to remove does not exist, remove() will raise an error.
# print(thisset)

# thisset.discard("cherry")                       #If the item to remove does not exist, discard() will NOT raise an error.
# print(thisset)

# x = thisset.pop()      #remove a random item
# print(x)               #print the remove item
# print(thisset)         #print thisset

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()
# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# del thisset
# print(thisset)

############### Join Update

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

# myset = set1.union(set2, set3, set4)         #union or update both used for joining different sets. Can do sets with tuples etc
# print(myset)

# myset = set1|set2|set3|set4                  # '|' is also used for joining sets. but only sets with sets
# print(myset) 

# set1.update(set2)                             # '|=' is also used for update
# print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)           #Intersection: Find common item between each sets. can do sets with list, tuples etc    
# print(set3)

# set3 = set1 & set2                       # &: Operator is also used for intersection. but only sets with sets
# print(set3)

# set1.intersection_update(set2)             #can update the original set with just like set1 (&=)
# print(set1) 

# set3 = set1.difference(set2)               #difference: print item that are not present in set2 from set1
# print(set3)

# set3 = set1 - set2                         # - :same as difference but only with sets
# print(set3)

# set1.difference_update(set2)               # can update original set just like set1 (-=)
# print(set1)

# set3 = set1.symmetric_difference(set2)     #print only items that are not present in both or multiple sets(set1 and set2)
# print(set3)

# set3 = set1 ^ set2                           # ^: used for symmetric difference but with only sets.
# print(set3)

# set1.symmetric_difference_update(set2)       #change the set1 permanantaly. (^=)
# print(set1)

# set1 = set(["Geeks", "For", "Geeks"])
# print(set1)

# # loop through set
# for i in set1:
#     print(i, end=" ")
    
# # check if item exist in set    
# print("Geeks" in set1)

# S = {}    #This will make empty dictionary
# print(type(S))
# S = set()  #This will create empty set
# print(type(S))
# S = []   #This will make empty list
# print(type(S))
# S = ()   #This will make empty tuple
# print(type(S))

# City = {"Karachi", "Islamabad", "Quetta", "Peshawar"}
# Country = {"Pakistan", "Bangladesh", "Afghanistan", "India"}

# disjoint_set = City.isdisjoint(Country)               #disjoint is used to check whether both set has intersection
# print(disjoint_set)                                   #values if not than it is True.

Country1 = {"Pakistan", "Bangladesh", "Afghanistan", "India"}
Country2 = {"Pakistan", "India"}

Superset = Country1.issuperset(Country2)
print(Superset)

Subset = Country2.issubset(Country1)
print(Subset)