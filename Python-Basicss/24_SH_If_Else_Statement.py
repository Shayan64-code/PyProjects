# a = 10
# b = 20
# print(a)if a > b else print("a is less than b")
# # OR
# age = 21
# print("Adult" if age > 17 else "Minor")
# OR
def check(a,b): 
    return a if a > b else b
print(check(10,20))