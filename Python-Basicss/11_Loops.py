# while loop

# x = 1
# while(x<=10):
#     print(x)
#     x=x+1

# # for loop
# for x in range(4,11):
#     print(x)

# for m in range(1,13):
#     print(m)

# days= ("Mon","Tue","Wed","Thur","Fri","Sat","Sun")
# year= ("Jan","Feb","March","Apr","May","Jun","July","Aug","Sep","Oct","Nov","Dec")
# for y in year:
#  print("\n",y,"\n")
#  for d in days:
#      if(d== "Sun"):
#          break
#      print(d)
 

# days= ("Mon","Tue","Wed","Thur","Fri","Sat","Sun")

# for d in days:
#      if(d== "Sat"):
#          continue  #skip the specific String etc
#      print(d)


# for x in range(0, 22, 2):
#     print(x)

# name = "Shayan"
# for x in name:
#     print(x)

# name = ["Shayan", "Bilal", "Aman"]
# for x in name:
#     print(x)

# count = 1
# while(count <= 10):
#     print(count)
#     count +=1

# for x in range(6):
#   print(x)
# else:                                #else can be used with for (if for loop is finished then else)
#   print("Finally finished!") 

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:                                 #now else will not print because loop is break(and not finished)
#   print("Finally finished!")         

number_guess = int(input("Write the guess number: "))
# while(True):
#     if number_guess != 40: 
#         number_guess = int(input("Try Again: "))
#     else:
#         print("You are correct the number is:", number_guess)
#         break

while(number_guess <= 30):             #when condition become false it will break
    number_guess = int(input("Write the guess number: "))
    print(number_guess)
else:
    print("Done")