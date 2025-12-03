
from ntpath import isdir
import os
import shutil

##### Q1

# os.chdir(r"C:\Users\User\Desktop\Practice")

# os.mkdir(r"01_Practice")

# Q2

# os.makedirs(r"C:\Users\User\Desktop\Practice\01_Practice\mkdir1\mkdir2")

####### Q10

# count = 0
# for root, dirs, files in os.walk(r"C:\Users\User\Documents"):
#     for file in files:
#         if file.endswith(".txt"):
#             count += 1
#     print("Files:", files)
#     print("-" * 40)

# print(count)

# Method 2

# files_List = []
# for root, dirs, files in os.walk(r"C:\Users\User\Documents"):
#     for file in files:
#         if file.endswith(".txt"):
#             print (root)
#             files_List.append(os.path.join(root, file))
# print("Files:", len(files_List))
# print("Files List")
# for f in files_List:
#     print(f)


# 🚀 12. Auto Backup Script

# Task:
# Write a script that:

# Checks if "Project" folder exists.

# If yes, create a backup zip file like:
# Project_backup_2025-10-04.zip

# Save it in "Backups" folder.

from datetime import datetime

# if os.path.exists(r"C:\Users\User\Desktop\Practice\Project_testing"):
#     shutil.make_archive(r"C:\Users\User\Desktop\Backup\Project_backup_{datetime.now()}", "zip", r"C:\Users\User\Desktop\Practice\Project_testing")     #mistakes

#Correct Version:

# source = r"C:\Users\User\Desktop\Practice\Project_testing"
# backup_dir = r"C:\Users\User\Desktop\Backup"

# os.mkdir(backup_dir)    #use if no dir for backup on desktop

# if os.path.exists(r"C:\Users\User\Desktop\Practice\Project_testing"):

#     timestamp= datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#     backup_name = os.path.join(backup_dir, f"Project_backup_{timestamp}")

#     shutil.make_archive(backup_name, "zip", source)

#     print("Zip file succesfuly created", backup_name,".zip")
# else:
#     print("Path not found")

# 🚀 13. File Sorter (Organizer)

# Task:
# Write a script that organizes all files in a folder by extension:
# Example — all .txt → "Text_Files", .jpg → "Images", .py → "Scripts".

# os.mkdir(r"C:\Users\User\Desktop\Organized Folder\Images")
# os.mkdir(r"C:\Users\User\Desktop\Organized Folder\Text_Files")
# os.mkdir(r"C:\Users\User\Desktop\Organized Folder\Scripts")
# os.mkdir(r"C:\Users\User\Desktop\Organized Folder\Others")

# Wrong Code:

# sourcedir = r"C:\Users\User\Desktop\Organized Folder"

# Text_Folder = r"C:\Users\User\Desktop\Organized Folder\Text_Files"
# Images_Folder = r"C:\Users\User\Desktop\Organized Folder\Images"
# Scripts_Folder = r"C:\Users\User\Desktop\Organized Folder\Scripts"
# Others_Folder = r"C:\Users\User\Desktop\Organized Folder\Others"

# if os.path.exists(sourcedir):
#     print(os.listdir(sourcedir))
#     for root, dirs, files in os.walk(sourcedir):    #root is the folder name, not the file path
#         for file in files:
#             if file.endswith(".txt"):
#                 shutil.move(root, Text_Folder)
#             elif file.endswith(".jpg"):
#                 shutil.move(root, Images_Folder)
#             elif file.endswith(".py"):
#                 shutil.move(root, Scripts_Folder)
#             else:
#                 shutil.move(root, Others_Folder)


# example of finding file and extension through splittext

# file, exten =os.path.splitext(r"C:\Users\User\Desktop\Organized Folder\Image3.jpg")

# print(file)
# print(exten)

# Correct Code:

# import os
# import shutil

# Paths
# sourcedir = r"C:\Users\User\Desktop\Organized Folder"
# Text_Folder = os.path.join(sourcedir, "Text_Files")
# Images_Folder = os.path.join(sourcedir, "Images")
# Scripts_Folder = os.path.join(sourcedir, "Scripts")
# Others_Folder = os.path.join(sourcedir, "Others")

# # Create folders if they don't exist
# for folder in [Text_Folder, Images_Folder, Scripts_Folder, Others_Folder]:
#     os.makedirs(folder, exist_ok=True)

# # Sort files
# if os.path.exists(sourcedir):
#     for file in os.listdir(sourcedir):
#         full_path = os.path.join(sourcedir, file)

#         if os.path.isfile(full_path):  # make sure it's a file, not a folder
#             if file.endswith(".txt"):
#                 shutil.move(full_path, Text_Folder)
#             elif file.endswith((".jpg", ".jpeg", ".png")):
#                 shutil.move(full_path, Images_Folder)
#             elif file.endswith(".py"):
#                 shutil.move(full_path, Scripts_Folder)
#             else:
#                 shutil.move(full_path, Others_Folder)

#     print("✅ Files organized successfully!")
# else:
#     print("❌ Source directory does not exist.")

###Written by me

# sourcedir = r"C:\Users\User\Desktop\Organized Folder"
# Text_Folder = os.path.join(sourcedir, "Text_Files")
# Images_Folder = os.path.join(sourcedir, "Images")
# Scripts_Folder = os.path.join(sourcedir, "Scripts")
# Others_Folder = os.path.join(sourcedir, "Others")

# for folders in [Text_Folder, Images_Folder, Scripts_Folder, Others_Folder]:
#     os.makedirs(folders, exist_ok= True)

# if os.path.exists(sourcedir):
#     for files in os.listdir(sourcedir):
#         fullPath = os.path.join(sourcedir, files )

#         if os.path.isfile(fullPath):
#             if files.endswith(".txt"):
#                 shutil.move(fullPath, Text_Folder)
#             elif files.endswith(".py"):
#                 shutil.move(fullPath, Scripts_Folder)
#             elif files.endswith((".png", ".jpg", ".jpeg")):
#                 shutil.move(fullPath, Images_Folder)
#             else:
#                 shutil.move(fullPath, Others_Folder)
    
#     print("Files Sorted Successfuly")
# else:
#     print(sourcedir, "Path doesn't Exist")


############### 14. Duplicate File Cleaner

sourcedir = r"C:\Users\User\Desktop\Organized Folder"

# dic = {}

# for root, dirs, files in os.walk(sourcedir):
#     for file in files:
#         file_path = os.path.join(root, file)
#         size = os.path.getsize(file_path)
#         key = (size, file)
        
#         if key in dic.items():   # check size and file
#             os.remove(file_path)
#             print("Duplicate File has been removed", file_path)
#         else:
#             dic[size] = file_path



##############🚀 15. Automated Folder Tree Visualizer

def print_tree(startpath, indent=""):
    items = os.listdir(startpath)

    for index, item in enumerate(items):
        path = os.path.join(startpath, item)
        is_last = (index == len(items) - 1)

        # draw structure lines
        connector = "└── " if is_last else "├── "
        print(indent + connector + item)

        # if folder → go deeper
        if os.path.isdir(path):
            next_indent = indent + (" 1   " if is_last else "│   ")
            print_tree(path, next_indent)

# Provide your folder path here
start_directory = r"C:\Users\User\Desktop\Organized Folder"

print("📁 Folder Tree Structure:\n")
print_tree(start_directory)


#Testing of Enumerate function
# items = os.listdir(sourcedir)
# for index, item in enumerate(items):
#     print(index, ": " ,item)

#Created My own os.walk using recursion:

# def walk_in_dirs(source):
    
#     items = os.listdir(source)

#     for item in items:
#         path = os.path.join(source, item)
#         print(item)

#         if isdir(path):
#             walk_in_dirs(path)
    

# walk_in_dirs(sourcedir)
