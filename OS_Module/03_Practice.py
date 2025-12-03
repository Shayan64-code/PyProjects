import os 

# print(os.path.exists("C:/Users/User/Desktop/GitHub/OS_Module"))

# # or like this

# print(os.path.exists(r"C:\Users\User\Desktop\GitHub\OS_Module"))

# print(os.path.isfile(r"C:/Users/User/Desktop/GitHub/OS_Module"))

# print(os.path.isdir(r"C:/Users/User/Desktop/GitHub/OS_Module"))

# print(os.path.getsize(r"C:/Users/User/Desktop/GitHub/OS_Module"))

# print(os.path.getmtime(r"C:/Users/User/Desktop/GitHub/OS_Module"))

# print(os.path.getctime(r"C:/Users/User/Desktop/GitHub/OS_Module"))

# print(os.path.getatime(r"C:/Users/User/Desktop/GitHub/OS_Module"))

###### Multiple Directories

# print(os.makedirs(r"C:/Users/User/Desktop/New_Folder/1stDirectory/2ndDirectory")) 

# print(os.makedirs(r"C:/Users/User/Desktop/New_Folder/1stDirectory/2ndDirectory/3rdDirectory/4thDirectory", exist_ok=True)) #exists ok will not give error if directory already exists

###### remove Files 

# os.remove(r"C:\Users\User\Desktop\GitHub\OS_Module\file1.txt")

###### remove Directories

# os.rmdir(r"C:\Users\User\Desktop\New_Folder")  #cause error if directory is not empty

# os.rename(r"C:\Users\User\Desktop\New_Folder", r"C:\Users\User\Desktop\New_Folder_Renamed") #rename directory 

# os.rename(r"C:\Users\User\Desktop\New_Folder_Renamed", r"C:\Users\User\Desktop\GitHub\OS_Module\New_Folder_Renamed") #also can move directory to another location

###########Level 2###########

# directory = r"New_Folder"
# parent_directory = r"C:\Users\User\Desktop\GitHub\OS_Module"

# path = os.path.join(parent_directory, directory)

os.chdir(r"C:\Users\User\Desktop\GitHub\OS_Module")

# os.mkdir(path)

# os.rmdir(path)

# path2 = os.path.abspath(path)
# print(path2)

# print(os.path.abspath("Projects"))  #for making full path

# print(os.path.basename(r"C:\Users\User\Desktop\GitHub\OS_Module\Nothing.py")) #for getting the name of the file

# print(os.path.dirname(r"C:\Users\User\Desktop\GitHub\OS_Module\New_Folder_Renamed")) #for getting the name of the directory

# print(os.stat("03_Practice.py"))

# print(os.path.getsize("New_Folder_Renamed"))

# print(os.path.getmtime("03_Practice.py"))

# print(os.path.split(r"C:\Users\User\Desktop\GitHub\OS_Module\New_Folder_Renamed"))  #for splitting the path into directory and file  

# print(os.path.splitext("New_Folder_Renamed.py")) #split file and extension(py or etc)

########### Enviroment Variables ###########

# print(os.environ)  # print all environment variables
# print(os.environ['USERNAME'])  # get specific variable

# # Show PATH
# print("PATH variable:")
# print(os.environ["PATH"], "\n")

# Which Python is being used
# print("Python executable:")
# print(os.path.dirname(os.sys.executable))   #python location or this python is running


# for root, dirs, files in os.walk(r"C:\Users\User\Desktop\GitHub\OS_Module"):

#     print("Current Directory:", root)
#     print("Sub-directories:", dirs)
#     print("Files:", files)
#     print("-" * 40)


# for root, dirs, files in os.walk(r"C:\Users\User\Desktop\GitHub\OS_Module"):
#     for file in files:
#         full_path = os.path.join(root, file)
#         print(full_path)


#remove through looping

# for root, dirs, files in os.walk(r"C:\Users\User\Desktop\GitHub\OS_Module\03_Practice.py"):
#     for file in files:
#         if file.endswith(".tmp"):
#             os.remove(os.path.join(root, file))
#             print("Deleted:", file)

# os.mkdir(r"Test")

# replace also used for replacing existing file with other
os.replace(r"C:\Users\User\Desktop\GitHub\OS_Module\Test", r"C:\Users\User\Desktop\GitHub\OS_Module\rename_Test")
