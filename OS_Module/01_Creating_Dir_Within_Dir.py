import os

# # # 1st Directory
# directory = "GeeksforGeeks"
# parent_dir = "C:/Users/User/Desktop/GitHub/OS_Module"
# path = os.path.join(parent_dir, directory)  #used for creating a path
# # os.mkdir(path)  #used for creating directory
# os.rmdir(path)

# # # 2nd Directory
# # print("Directory '% s' created" % directory)
# directory = "Geeks"
# parent_dir = "C:/Users/User/Desktop/GitHub/OS_Module"
# # # mode = 0o666     used in Linux/Mac, Not used in Windows
# path = os.path.join(parent_dir, directory)
# # os.mkdir(path)
# os.rmdir(path)
# # print("Directory '% s' created" % directory)


# cwd = os.getcwd() 
# print("Current working directory:", cwd)




# Practice

directory = "Practice"
parent_dir = "C:/Users/User/Desktop/GitHub/OS_Module"

path = os.path.join(parent_dir, directory)
#os.mkdir(path)     #Created Practice Directory
os.rmdir(path)

#print("Directory '% s' created" % directory)