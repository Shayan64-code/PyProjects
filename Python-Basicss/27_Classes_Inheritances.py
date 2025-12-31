# class Human:
#     def __init__(self, name, occupation):
#         self.name = name;
#         self.occupation = occupation;

#     def work(self):
#         print("His name is",self.name, "and he is an", self.occupation)


# name1 = Human("Tom Cruise", "Actor")    #self = name1
# name1.work()
# print(name1.name)

# name2 = Human("Maria Sharapova", "Tennis Player")
# name2.work()


#########Inheritance

# class Vehicle:
#     def general_use(self):
#         print("General Use is Transportation.")

# class Car(Vehicle):

#     def __init__(self):
#         self.wheels = 4
#         self.doors = 4

#     def special_use(self):
#         print("I am Car.")
#         # self.general_use()   ##can also be called like this.
#         print("Special Use is can go outing with family.")

# class Bike(Vehicle):

#     def __init__(self):
#         self.wheels = 2
#         self.doors = 0

#     def special_use(self):
#         print("I am Bike.")
#         print("Special Use is can do riding.")

# b = Bike()
# b.general_use()
# b.special_use()
# b.doors
# b.wheels

# c = Car()
# c.general_use()
# c.special_use()
# c.doors
# c.wheels


##########Multiple Inheritances

# class Father:
#     def driving(self):
#         print("I Love Driving Lambo.")
#     def skills(self):
#         print("Driving and Sports.")


# class Mother:
#     def cooking(self):
#         print("I love Cooking.")
#     def skills(self):
#         print("Cooking and Eating.")

# class Child(Father, Mother):
#     def playing(self):
#         print("I Love Playing.")
    
#     def skills(self):
#         Father.skills()
#         Mother.skills()
#         print("Riding and Sports.")

#     # super #didnt known how to use.

# c = Child()

# c.playing()
# c.driving()
# c.skills()


class Student:
    def set_name(self, name):
        self.name = name

    def work(self):
        print("His name is",self.name)

s1 = Student()
s1.set_name("Ali")

print(s1.name)