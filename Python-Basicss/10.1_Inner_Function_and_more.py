
# def fun(msg):           #Outer Function

#     def fun2():         #Inner Function
#         print(msg)
#     fun2()
    
# fun("Hello")

# a = "I am a global var"
# b = "I am also global here"

# def fun():
#     b = "I am enclosing var"

#     def fun2():
#         global a                                  #It is used to change value globally.
#         nonlocal b                                #nonlocal is used to change value in the function.

#         a = "Changing the Global"
#         b = "Changing the nonglobal inside function"

#     fun2()
#     print(b)

# fun()                #Change and print nonglobal b
# print(a)             #Change globally through function 
# print(b)             #Doesn't change globally

# Error Example.
# # Global variable
# global_a = 'geeksforgeeks'

# def outer():
#     def inner():
#         nonlocal global_a # Attempting to reference global variable    #always produce error
#         global_a = 'GeeksForGeeks'  # Modifying the variable
#         print(global_a)
#     inner()
# outer()

# def fun1():
#     name = "geek"
    
#     def fun2():
#         name = "Geek"
        
#         def fun3():
#             nonlocal name  
#             name = 'GEEK'  # Modify before using   #Modify the nearest enclosing Scope
#             print(name)  
        
#         fun3()
#         print(name)  # Modified value in fun2()  #fun2 will change
    
#     fun2()
#     print(name)  # Unchanged value in fun1()     #fun3 will be non affected

# fun1()

# # Output:
# # GEEK
# # GEEK
# # geek

# #Example 2:
# def fun1():
#     name = "geek"
    
#     def fun2():
#         nonlocal name              #But this will change fun1() also
#         name = "Geek"
        
#         def fun3():
#             nonlocal name  
#             name = 'GEEK'  # Modify before using
#             print(name)  
        
#         fun3()
#         print(name)  # Modified value in fun2()
    
#     fun2()
#     print(name)  # Unchanged value in fun1()

# fun1()

# # Output:
# # GEEK
# # GEEK
# # GEEK

# def counter():
#     count = 0  # Enclosed variable

#     def increment():
#         nonlocal count  # Reference count from the outer function
#         count += 1
#         return count

#     return increment

# # Create a counter instance
# counter1 = counter()           #for saving value
# print(counter1())  
# print(counter1())  
# print(counter1())

#############Closure in Functions (Inner)

# #Example 1:
# def Outer(x):

#     def Inner(y):
#         return x + y
    
#     return Inner

# Inner2 = Outer(10)     
# print(Inner2(5))       #Inner2 is the closure here which run Inner 

# #Example 2:
# def Outer(x):

#     def Inner1(y):
#         return x + y

#     def Inner2(z):
#         return x + z
    
#     return Inner1(), Inner2()

# Inner1_Cl, Inner2_Cl = Outer(5)        #Inner1_Cl = Inner1 and Inner2_Cl = Inner2
# print(Inner1_Cl(3))
# print(Inner2_Cl(5))

# #Example 3
# def Outer(x):

#     def Inner1(y):

#         def Inner2(z):
#             return x + y + z
#         return Inner2()
#     return Inner1()

# Inner1_Cl = Outer(10)
# Inner2_Cl = Inner1_Cl(20)
# result = Inner2_Cl(5)

# print(result)

def process_data(data):

    def clean_data():
        return [item.strip() for item in data]      #remove spaces
    
    return clean_data()

print(process_data([" Spaces is Everywhere ", " Please remove them "]))