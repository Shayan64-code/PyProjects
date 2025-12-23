############Iterators

# a = ["Hi", "hello", "good", "awesome", "perfect"]

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

# print(next(itr))    ##raising error here, because there is no string after "perfect".

# print(dir(itr))   #next inside itr

# itr = reversed(a)

# print(next(itr))    #now printing from "perfect"

class RemoteController():

    def __init__ (self):
        self.index = -1
        self.channels = ["HBO", "CNN", "ESPN", "GEO"]

    def __iter__ (self):
        return self

    def __next__ (self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r = RemoteController()

itr = iter(r)

print(next(itr))

print(next(itr))

print(next(itr))