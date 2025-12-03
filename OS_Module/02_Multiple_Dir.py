
import os

# # 1st Directory
# directory = "Shayan"
# parent_dir = "C:/Users/User/Desktop/GitHub/OS_Module"
# path = os.path.join(parent_dir, directory)
# os.makedirs(path)
# print("Directory '% s' created" % directory)

# 2nd Directory
# directory = "c"
# parent_dir = "C:/Users/User/Desktop/GitHub/OS_Module/a/b" 
# path = os.path.join(parent_dir, directory)
# os.makedirs(path)     #created multiple directories recursively
# print("Directory '% s' created" % directory)


#List all the directories in the current working directory

# os.chdir("C:/Users/User/Desktop/GitHub/OS_Module")
# print(os.listdir())     

##Deleting File or Directory

os.chdir("C:/Users/User/Desktop/GitHub/OS_Module")
os.rmdir("New_Folder")   #for removing empty directory/folder
#or
# os.remove("C:/Users/User/Desktop/GitHub/OS_Module/New_Folder")   #for removing file

