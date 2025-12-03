import os 
import shutil

os.chdir(r"C:\Users\User\Desktop\GitHub\Shutil_Module")

#copy file
# shutil.copy(r"C:\Users\User\Desktop\GitHub\OS_Module\00_26_OS_Module.py", r"Copy_Folder.py")

# Same as copy(), but also preserves metadata (creation & modification time
# shutil.copy2("source.txt", "backup_with_metadata.txt")

# Copy whole folder: Subfolders and File etc in it recursively.
# shutil.copytree("C:/Projects/Folder1", "C:/Backup/Folder1_copy")
# ⚠️ Fails if the destination folder already exists (use dirs_exist_ok=True in Python 3.8+).

# move or rename file and folder 
# shutil.move("old_folder", "new_folder_location")

# Deletes everything inside — use carefully!
# shutil.rmtree("C:/Projects/Folder_to_delete")

# If the destination exists → it won’t raise an error (Python 3.8+).
# shutil.copytree("src_folder", "dst_folder", dirs_exist_ok=True)

# used for finding disk storage
# total, used, free = shutil.disk_usage("D:/")
# print("Total:", total // (2**30), "GB")
# print("Used:", used // (2**30), "GB")
# print("Free:", free // (2**30), "GB")
