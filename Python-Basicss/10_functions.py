# 1
# def First_function():
#    print("This is my first function")
#    print("This is my first function")
#    print("This is my first function")

# First_function()

# 2
# def Second_Function():
#     text= "This is my Second Function"
#     print(text)
#     print(text)
#     print(text)

# Second_Function()

# 3
# def Third_Function(text):
#     print(text)
#     print(text)
#     print(text)

# Third_Function("This is my Third Function")

# #  4
# #  defining function with if, elif, else statement

# def school_calculator(age,name):
#     if age > 5:
#       print("Get him the admission in higher secondary school")
#     elif age == 5 :
#       print("Yes,", name ,"can get admission")
#     else:
#       print("Sorry!", name , "is too little")

# school_calculator(15,"Bilal")

# #  5

# def future_age(age):
#     age = age + 10
#     return age

# print(future_age(10))

# def my_function(*kids):
#   print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias", "Linus")

# def function1(*Kid1, Kid2):
#     print(Kid1[2], " and ", Kid2)

# def function(*kids, **details):
#     print(kids)
#     print(details)

# function("Ali", "Sara", age=10, city="Lahore")




# def function2():
#     pass            #doesnot give error


# #recursion
# def tri_recursion(k):                
#   if(k > 0):
#     result = k + tri_recursion(k - 1)          # 3 + trixxx(2) -> 2 + trixxx(1) -> 1 + trixxx(0) -> return 0(else)
#     print(result)                              # now 1 + 0, 2 + 1, 3 + 3
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(3)

# def evenOdd(x: int) ->str:
#     if (x % 2 == 0):
#         return "Even"
#     else:
#         return "Odd"

# print(evenOdd(16))
# print(evenOdd(7))

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

# def fun():
#     global a
#     a += " Modified globally through +="
#     print(a)                                      #Global Variable inside a function.
#     a = "This will overwrite the a globally"
#     print(a)

# a = "This is real global a"
# print(a)                          #print out the real a
# fun()                             #first print modified than overwrite
# print(a)                          #print last overwritted a

######another example

# a = 1  # Global variable

# def f():
#     print('f():', a)  # Uses global a

# def g():                                         #doesnot change globally
#     a = 2  # Local variable shadows global
#     print('g():', a)

# def h():
#     global a
#     a = 3  # Modifies global a
#     print('h():', a)

# print('global:', a)  
# f()                  
# print('global:', a) 
# g()                 
# print('global:', a)  
# h()                  
# print('global:', a)

#Recursive Example 2:

def fibonacci(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(8))