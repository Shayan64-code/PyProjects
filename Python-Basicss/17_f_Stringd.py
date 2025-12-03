# k = "first"       #or maybe dictionaries
# val = "Last"

# print(f"{k} == {val}")                 #print the key and value between them

# def fun(**kwargs):
#     for k, val in kwargs.items():
#         print("%s == %s" % (k, val))       #Or like like this

# # Driver code
# fun(s1='Geeks', s2='for', s3='Geeks')

# def fun(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# fun(1, 2, 3, a=4, b=5)

# name = "Shayan"
# country = "Pakistan"

# txt = (f"My name is {name} and I live in {country}.")
# print(txt)

# txt2 = (f"My name is {{name}} and I live in {{country}}.")  #to print the exact code
# print(txt2)

price = 19.999999

txt3 = (f"You can buy this in just {price:.2f}$.")
print(txt3)