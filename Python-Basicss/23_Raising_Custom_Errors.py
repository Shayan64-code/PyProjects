
# a = int(input("Write number between 5 and 9: "))

# if(a < 5 or a > 9):
#     raise ValueError("This is an Value Error")    #raise error

#Q1: Raise error when a is not between 5 and 9 but not when input is string insted integer.

# a = None   #used when there is no value to put inside of a variable.

# a = input("Write number between 5 and 9: ")

# if(isinstance(a, int)):        #check whether it is int or not
#     if(int(a) < 5 or int(a) > 9):
#         raise ValueError("This is an Value Error")                   #Wrong attempt
#     else:
#         print(a)
# else:
#      print(a)

#Q1: Raise error when a is not between 5 and 9 but not when input is string insted integer.

# a = input("Write number between 5 and 9: ")

# if a.isdigit():
#     a = int(a)
#     if a < 5 or a > 10:
#         raise ValueError("This is a value error")  #Correct
#     else:
#         print(a)
# else:
#     print("This is a string", a)

#Q1.1: Now with try and except

a = input("Write number between 5 and 9: ")

try:
    a = int(a)
    if a > 5 and a < 10:      #change in statement with 'and'
        raise ValueError("This is a value error")       #If the error is raised it will go in the except statement.   
        print("This is if value: ", a) 
    else:
        print("This is else value: ",a)
except:
    print("This is a string: ", a)