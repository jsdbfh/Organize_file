import os
import shutil

def organize_files(directory):
    # File type categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".txt", ".pdf", ".docx"],
        "Audio": [".mp3", ".wav"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Archives": [".zip", ".rar"],
        "Others": []
    }
    
    # Create category folders if not exist
    for category in file_types.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Organize files
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_types.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, category, file_name))
                    moved = True
                    break
            # Move to "Others" if no matching type
            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", file_name))

# Specify the directory to organize
directory_path = input("Enter the folder path to organize: ")
organize_files(directory_path)

print("Files organized successfully!")
