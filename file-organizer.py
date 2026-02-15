import os
import shutil

# Change this path if needed
folder_path = os.getcwd()

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Programs": [".exe", ".msi"]
}

def organize_files():
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()

            moved = False
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    target_folder = os.path.join(folder_path, folder)

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"Moved: {file} → {folder}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"Moved: {file} → Others")

if __name__ == "__main__":
    print("📂 Organizing files...")
    organize_files()
    print("✅ Done!")
