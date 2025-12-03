###Encoder&&Decoder

import random
import string

print("What do you want Encode or Decode:")
print("1.Encode        2.Decode")
x = input("Write here: ")
a = input("Write string here which you want to be encode/decode: ")

start = ''.join(random.choice(string.ascii_letters) for i in range(3))
end = ''.join(random.choice(string.ascii_letters) for i in range(3)) 

if (x.lower().strip() == "encode" or x.lower().strip() == "encoder" or x == "1"):
    if(len(a) < 3):
        print(a[::-1])
    else:
        b = a[::-1]
        print(start + b + end)
if (x.lower().strip() == "decode" or x.lower().strip() == "decoder" or x == "2"):
    if(len(a)<3):
        print(a[::-1])
    else:
        b = a[::-1]
        c = b[3:]
        d = c[:-3]
        print(d)
        

# a = "bcdmathdog"
# # Remove 3 letters from the middle
# mid = len(a) // 2   # find the middle index  #5
# remove = 3          # number of letters to remove

# result = a[:mid - remove//2] + a[mid + (remove - remove//2):]
#      # = a[: 5  -  3//2]     + a[5   + (  3    -      3//2):]
#      # = a[: 5  -  1]        + a[5   + (  3    -  1):]
#      # = a[: 4]          +      a[7:]
# print(result)




# # a = "bcdshayanqrs"
# # b = a[3:]
# # c = b[:-3]
# # print(c)






# # #new discovery(string slicing)
# a = "shayans"
# # print(a[0:7:2])   #start : stop : step  #after each, second string is print (saas)

# # a = "shayan"
# # print(a[0:6:2])   #doesnt print 'n'  (saa)

# # #for reverse in each string
# # a = "shayan"
# # print(a[::-1]) ##:: -> take whole strings -1 move backwards

# print(a)