###########Iterators

a = ["Hi", "hello", "good", "awesome", "perfect"]

# for i in a:
#     print(i) #iterating in a

# print(dir(a))

# itr = iter(a)

# # print(itr)

# print(next(itr))   #give the first element

# print(next(itr))

# print(next(itr))

# print(next(itr))

# print(next(itr))

# # print(next(itr))    ##raising error here, because there is no string after "perfect".

# # print(dir(itr))   #next inside itr

# itr = reversed(a)

# print(next(itr))    #now printing from "perfect"

# class RemoteController():

#     def __init__ (self):
#         self.index = -1
#         self.channels = ["HBO", "CNN", "ESPN", "GEO"]
    
#     def __iter__ (self):
#         return self      #object itself is iterators (which store each state)

#     def __next__ (self):
#         self.index += 1
#         if self.index == len(self.channels):
#             raise StopIteration

#         return self.channels[self.index]

# r = RemoteController()

# itr = iter(r)      #calls built-in iter which call __iter__()

# print(next(itr))   #same for next just like iter

# print(next(itr))

# print(next(itr))

##Working of function/method __iter__

# iter(obj)
#    ↓
# obj.__iter__()
#    ↓
# returns iterator
#    ↓
# next(iterator)
#    ↓
# iterator.__next__()


# class Student():
#     def show(self):
#         print(self)

# s1 = Student()
# s2 = Student()

# s1.show()
# s2.show()

#####Generator

# def Remote_control_next():
#     yield "cnn"
#     yield "HBO"   #similar to return but it can preserve the state of last execution 

# itr = Remote_control_next()

# print(next(itr))

# print(next(itr))

# for c in Remote_control_next():      #we can run for loop on generator
#     print(c)

def fib():           #fibonacci series generator
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a+b  #(0,1),(1,1),(1,2),(2,3),(3,5),(5,8)

for f in fib():
    if f > 50:
        break
    print(f)