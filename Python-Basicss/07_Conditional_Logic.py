# Logic Operators:
# Equal to                  ==
# Not Equal to              !=
# Greater than               >
# Less than                  <
# Greater then Equal to     >=
# Less than Equal to        <=

#print(5==5) #true 
#print(5!=5) #false
#print(5>=4) #true
#print(5<=4) #false

# Application of logic operators

#Bilal_age = 4
#Age_at_school = 5
#print(Bilal_age==Age_at_school)

# now with input

Age_at_school= 5
Bilal_age = input("What is bilal age ")
print(type(Bilal_age))  #showing string type due to string input
Bilal_age=int(Bilal_age)
print(type(Bilal_age))
print(Bilal_age>=Age_at_school)
