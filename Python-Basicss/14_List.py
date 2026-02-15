
#### [List is a collection which is ordered and changeable. Allows duplicate members.]

# This_is_List = ["Apple", "Banana", "1", "Apple"]          #A list also can save duplicates
# print(This_is_List)
# print(len(This_is_List))     # Length

# list1 = ["abc", 34, True, 40, "male"]     #contain diff data types
# print(type(list1))     #type of list

# list2 = ["Tomato", "Potato", "Onion", "Carrot"]
# list2[1] = "Cabbage"       #Potato will change
# print(list2)
# list2[1:4] = "Orange", "Mango", "Banana"     #1, 2, 3 will change
# print(list2)

# list2.insert(2, "Watermelon")     #insert Watermelon without removing Onion at 2 used for adding at specific index
# print(list2)

# list2.append("Peas")      #for adding at the end
# print(list2)

# list3 = ["Mango", "Pineapple", "Papaya"]
# list3.extend(list2)              #merging list 3 with list 2
# print(list3)

# thistuple = ("kiwi", "orange")
# list3.extend(thistuple)           #merging tuple with List    #can also add tuple, sets, dictionaries
# print(list3)

# thislist = ["apple", "banana", "cherry", "kiwi"]
# thislist.remove("banana")                #remove the banana
# print(thislist)

# thislist2 = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist2.remove("banana")            #remove the first banana  #remove item wise
# print(thislist2)

# thislist.pop(1)            #remove specified index like banana    #remove index wise
# print(thislist)

# thislist.pop()               #remove last index
# thislist.__delitem__(1)      #also use for removing index
# print(thislist)

# del thislist[0]              #use to del index also
# del thislist                 #del entire list

# thislist.clear()               #emptied the list  #function
# print(thislist)

# ######Loop in List

# list4 = ["Papaya", "Grapes", "Orange", "Kiwi"]
# for x in list4:
#      print(x)

# for x in range(len(list4)):         #range(4) -> run 4 times x=0, x=1, x=2, x=3
#      print(list4[x])                 #x=0 -> Papaya so on...

# i = 0
# while(i < len(list4)):
#     print(list4[i])
#     i = i + 1

# [print(x) for x in list4]            #for printing in one line


# def appendItem(itemName, itemList = []):     #itemList = [] mutable list not safe to use
#     itemList.append(itemName)
#     return itemList


# print(appendItem('notebook'))
# print(appendItem('pencil'))
# print(appendItem('eraser'))

# def appendItem(itemName):                    #inside function everytime new list will be created
#     itemList = []
#     itemList.append(itemName)
#     return itemList


# print(appendItem('notebook'))
# print(appendItem('pencil'))
# print(appendItem('eraser'))

# itemList= []                             #global list every changes done in it
# def appendItem(itemName):
#     itemList.append(itemName)
#     return itemList

# print(appendItem('notebook'))
# print(appendItem('pencil'))
# print(appendItem('eraser'))

# def myfun(x, y):
#     x[0] = 1
#     y[1] = 2
#                                        #changing list using function (Pass by reference)(set, list, dict are mutable)
# mylist = [10, 20, 30, 40, 50]         
# myfun(mylist, mylist)
# print(mylist)

# def change_number(x):
#     x = 10  # Changes local copy only    (Pass by value)(int, float, str, bool, tuple are immutable)
#     return x

# num = 5
# change_number(num)
# print(num)

# def fun(s):
#     s += 'GFG'  
#     print("Inside Function", s)

# s = "I love Geeksforgeeks"
# fun(s)