from pathlib import Path

p = Path(r"C:\Users\User\Desktop\PathLib Testing")

#for checking if the path exists
# print(p.exists())
# print(p.is_file())
# print(p.is_dir())
# print(p.is_absolute())
# print(p.parent) #for getting the parent directory means the directory above the current directory
# print(p.parents) #for getting the parent directories means the directories above the current directory
# print(p.anchor) #for getting the anchor of the path means C:\
# print(p.drive) #for getting the drive of the path means C:
# print(p.root) #for getting the root of the path means '\'
# print(p.parts) #for getting the parts of the path means ('C:', 'Users', 'User', 'Desktop', 'PathLib Testing')
# print(p.name) #for getting the name of the path means PathLib Testing with extension
# print(p.stem) #for getting the stem of the path means PathLib Testing without extension
# print(p.suffix) #for getting the suffix of the path means ('.py') extension
# print(p.suffixes) #for getting the suffixes of the path means ('.py',) extensions

# cwd = Path.cwd()
# print(cwd)

p1 = p / "New_Directory" / "New_Directory"
# print(p1.parts)
p2 = p / "New_File.txt" ####for creating a new file in the current directory
# p1.mkdir(parents=True, exist_ok=True) ####for creating a new directory in the current directory
# p2.touch() ####for creating a new file in the current directory
# p2.write_text("Hello, World!") ####for writing text to a file
# print(p2.read_text()) ####for reading text from a file
# p1.rmdir() ####for removing a directory in the current directory (for empty directory)first delete
# p1.parent.rmdir() ####for removing the parent directory (for empty directory)
# p2.rename("File_Renamed.txt") ####for renaming a file
# p2.unlink(missing_ok=True) ####for removing a file (for empty file)

# print(p2.iterdir()) ####for iterating through the directory
# for item in p2.iterdir():
#     print(item)

p = Path(r"C:\Users\User\Desktop\Organized Folder")

# print(list(p.iterdir())) ####like os.listdir() ###iterdir() gives full path
# [print(dir) for dir in p.iterdir() if dir.is_dir()] ####for iterating through the directory (just Organized Folder)

# [print(f) for f in p.glob("*.txt")] #### print file/forlder , for now file ".txt"  *

# [print(f) for f in p.rglob("*.py")] #### print file /folders recursively(search through every directory for .py)

# src = Path(r"C:\Users\User\Desktop\Organized Folder\New Text Document.txt")
# dst_folder = Path(r"C:\Users\User\Desktop\Organized Folder\Text_Files")


# dst = dst_folder / src.name

# src.replace(dst)

############ Delete latest file without even knowing name

# import shutil

# p = Path(r"C:\Users\User\Desktop\PathLib Testing")

# dirs = [d for d in p.iterdir() if d.is_dir()]

# # get the newest folder
# latest = max(dirs, key=lambda d: d.stat().st_mtime)

# shutil.rmtree(latest)

# print(p.resolve())

