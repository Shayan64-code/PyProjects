###Dictionaries are used to store data values in key:value pairs.
#[A dictionary is a collection which is ordered*, changeable and do not allow duplicates.]

thisdic = {                             #dictionary doesnot duplicate two item with same key
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  :  1964
}
# print(thisdic)

# print(thisdic["brand"])             #Calling "brand" vakue of dictionary
# x = thisdic.get("brand")            #Calling "brand" vakue of dictionary using get() method
# print(x)

# print(len(thisdic))            #Len is 3

thisdic = {                             
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  :  1964,
    "colors": ["red", "white", "blue"],                 #List
    "showroom": {"Karachi", "Lahore", "Islamabad"}      #Sets, can save any data type
}
# print(thisdic)

# print(type(thisdic))

# thisdict = dict(name = "Shayan", age = 19, country = "Karachi")      #dict Constructor
# print(thisdict)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()           #give only keys 
# print(x)

# car["color"] = "White"
# print(x)

# y = car.values()         #give only values
# print(y)

# car["year"] = 2020
# print(y)

# z = car.items()           #give both keys and values
# print(z)

# if "model" in car:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

# car.update({"year" : "2020"})         #adding value through update
# car.update({"color" : "green"})       #adding item
# print(car)

# car["color"] = "blue"                   #also like this
# car["year"] = "2020"
# print(car)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"color": "blue"
}
# car.pop("model")     #pop() method remove the specified key name. 
# print(car)

# car.popitem()        #remove the last item
# print(car)

# del car["color"]        #delete color
# print(car)

# del car  #delete car dictionary

# car.clear()
# print(car)

# for x in car.values():            #print car values
#   print(x)

# for x in car.keys():              #print car keys
#   print(x)

# for x in car:                       #print keys
#   print(x)

# for x in car:                        #print values
#   print(car[x])       

# for x in car.items():               #print both
#   print(x)

# mycar = car.copy()        #copy with copy() method
# print(mycar)

# mycar = dict(car)         #copy with dict constructor
# print(mycar)

################# Nested Dictionaries

myfamily = {
    "Child1": {
        "Name":"Shayan",
        "Age": 19
    },
    "Child2": {
        "Name":"Ahtesham",            ###Nested Dictionary
        "Age": 21
    },
    "Child3": {
        "Name": "Kainat",
        "Age": 24
    }
}

# print(myfamily)

###### OR

Child1 = {
    "Name":"Shayan",
    "Age": 19
}
Child2 = {
    "Name": "Kashan",
    "Age": 28
}
Child3 = {
    "Name": "Kulsoom",
    "Age": 40
}
myfamily2 = {
    "Child1": Child1,
    "Child2": Child2,            ###Or like this
    "Child3": Child3
}
# print(myfamily2["Child1"]["Name"])

# for x, obj in myfamily2.items():
#     print(x, myfamily2[x])               #also iterate like this in nested dictionary 

# for x, obj in myfamily2.items():
#     print(x)                             #also iterate like this for every particular obj
#     for y in obj:
#      print(y + ":", obj[y])
    
# ✅ Common Use Case: Grouping items in a dictionary

words = ["apple", "banana", "apricot", "blueberry", "avocado"]
grouped = {}

for word in words:
    first_letter = word[0]
    grouped.setdefault(first_letter, []).append(word)     #complex example from chatgpt with setdefault

print(grouped)


def addItemToDictionary(itemName, quantity, itemList = {}):
    itemList[itemName] = quantity
    return itemList
                                                 #dictionary with function
print(addItemToDictionary('notebook', 4))                   
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))