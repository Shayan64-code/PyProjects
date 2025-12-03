import os 
cwd = os.getcwd() 
print("Current working directory:", cwd)   #In which folder we are working

os.chdir("C:/Users/User/Desktop/GitHub/OS_Module")  #change the working directory
# cwd = os.getcwd() 
# print("Current working directory:", cwd)   #In which folder we are working

# os.mkdir("New_Folder")  #create a new folder
# #os.rmdir("New_Folder")  #remove a folder

# os.listdir()  #list all the files and folders in the current working directory
# #or
# print(os.listdir())

# print(os.listdir(path="."))   #path="." means current working directory
# print(os.listdir(path="C:/Users/User/Desktop/GitHub/OS_Module"))   #path="C:/Users/User/Desktop/GitHub/OS_Module" means other directory
# print(os.listdir(os.getcwd()))   #os.getcwd() means current working directory

# Check if file or directory exists
print(os.path.exists("New_Folder"))   #os.path.exists("New_Folder") means check if New_Folder exists
print(os.path.exists("C:/Users/User/Desktop/GitHub/OS_Module/New_Folder"))   #os.path.exists("C:/Users/User/Desktop/GitHub/OS_Module/New_Folder") means check if New_Folder exists in other directory
print(os.path.exists(os.getcwd()))   #os.path.exists(os.getcwd()) means check if current working directory exists

# Check if file or directory is a file or directory
print(os.path.isfile("New_Folder"))   #os.path.isfile("New_Folder") means check if New_Folder is a file
print(os.path.isdir("New_Folder"))   #os.path.isdir("New_Folder") means check if New_Folder is a directory

# Check if file or directory is a file or directory in other directory