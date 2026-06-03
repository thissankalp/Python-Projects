import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))

files = os.listdir(script_dir)

categories = {
    ".jpg" : "Images", 
    ".png" : "Images", 
    ".jpeg" : "Images", 
    ".gif" : "Images", 
    ".svg" : "Images", 
    ".webp" : "Images",
    ".pdf" : "Documents", 
    ".doc" : "Documents", 
    ".docx" : "Documents", 
    ".txt" : "Documents", 
    ".csv" : "Documents",
    ".mp4" : "Videos", 
    ".mp3" : "Audios", 
    ".py" : "Codes"
}

for file in files:
    source_path = os.path.join(script_dir, file)
    
    if file == os.path.basename(__file__):
        continue
    if os.path.isdir(source_path):
        continue
        
    extension = os.path.splitext(file)[1].lower()
    
    if extension in categories:
        folder_name = categories[extension]
        target_folder_path = os.path.join(script_dir, folder_name)
        os.makedirs(target_folder_path, exist_ok=True)
        
        destination = os.path.join(target_folder_path, file)
        
        if os.path.exists(destination):
            print(f"Skipped: {file} (already exists in {folder_name})")
            continue
        try:
            shutil.move(source_path, destination)
            print(f"Moved: {file} -> {folder_name}")
        except Exception as e:
            print(f"Error moving {file}: {e}")