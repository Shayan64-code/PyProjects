
# f = open("First_File.txt")           #for txt file opening by default
# b = open("First_Binary.txt", 'b')    #for binary opening (binary is used for images) 

# with open("Second_File.txt", 'w') as w:                  #also initialize variable like this 'w'
#     w.write("This is the File I created.")               #'w' is for writing it overwrite the file and also create file
#     w.close()

# with open("Second_File.txt", 'r') as r:                  #'r' for reading file.
#     print(r.read())
#     r.close()

# with open("Second_File.txt", 'a') as a:                  #'a' for appending end of the file also create
#     a.write("""Hello! Welcome to This file is for testing purposes.
# Good Luck!""")
#     a.close()

# with open("Second_File.txt", 'r') as r2:
#     print(r2.readline())                                 #readline for reading each line
#     print(r2.readline())
#     r2.close()


# with open("Third_File.txt", 'w') as w:                  
#     w.write("This is the third File I created.")               
#     w.close()
# import os
# if os.path.exists("Third_File.txt"):
#     os.remove("Third_File.txt")
#     print("File has been deleted successfuly")
# else:
#     print("file doesn't exists")