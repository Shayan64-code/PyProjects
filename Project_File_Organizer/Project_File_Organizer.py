import os
import shutil

# Ask user for the folder to organize
folder_path = input("C:\Users\User\Desktop\File_Organizer")

# Check if path exists
if not os.path.exists(folder_path):
    print("The folder does not exist.")
    exit()

# Define folders for file types
file_types = {
    'Images': ['.jpg', '.jpeg', '.png'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov'],
}

# Create folders if not present
for folder in file_types:
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

# Sort the files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)

        moved = False
        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                print(f"Moved: {file} → {folder}/")
                moved = True
                break

        if not moved:
            # Create 'Others' folder for unknown types
            others_folder = os.path.join(folder_path, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, file))
            print(f"Moved: {file} → Others/")

print("All files organized successfully!")
