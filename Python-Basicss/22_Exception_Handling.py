
a = int(input("Write the number for multiplication table: "))  #but what if i put "harry" instead of integer it will
print(f"The multiplication table of {a} is:")                  #show error and entire code will stop running

for i in range(1,11):
    print(f"The multiplication of {a} x {i} is {a*i}")

print("This is the end of the table.")

#Exception Handling

# a = input("Write the number for multiplication table: ")  
# print(f"The multiplication table of {a} is:")                  

# try:
#     for i in range(1,11):
#         print(f"The multiplication of {int(a)} x {i} is {int(a)*i}")
# except Exception as e:
#     print(e)                                               #tell us about what error is occured
#     print("Invalid Input!")
#     print("There is error in the input")                     #we can also print or run whole block of code here          

# print("This is the end of the table.")


# #Exception Handling2

# a = int(input("Write the number for multiplication table: "))  
# print(f"The multiplication table of {a} is:")                  

# try:
#     for i in range(1,11):
#         print(f"The multiplication of {a} x {i} is {a*i}")
# except:                                                     #we doesn't need to known about error.
#     print("Invalid Input!")
#     print("There is error in these lines of code")                     #we can also print or run whole block of code here          

# print("This is the end of the table.")

#Exception Handling 3

# try:
#     num = int(input("Write the number for multiplication table: "))
#     a = [6, 8]
#     print(a[num])
# except ValueError:                     #This will handle specific error in a specific way.
#     print("This is Value Error.")     #if we put input instead of a int.
# except IndexError:
#     print("This is an Index Error.")