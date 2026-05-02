# File organizer script
import os, shutil, argparse

parser = argparse.ArgumentParser(
    prog="OrganizeFiles",
    description="Organize files into folders based on extensions"
)

parser.add_argument("--dry-run", action='store_true', help="Run without actually moving files")
args = parser.parse_args()

# Path where to organize the files
path = os.path.expanduser("~/Downloads")

# Path where to put the files
destination_path = os.path.expanduser("~/Downloads")

# Folders and their extensions
categories = {
    'Archives': ['.gz', '.rar', '.7z', '.zip'],
    'Artworks': ['.kra'],
    'Music': ['.mp3', '.flac'],
    'Images': ['.png', '.jpg', '.webp', '.gif'],
    'Books': ['.epub', '.pdf'],
    'Exe': ['.exe'],
    'Other': []
}

def find_file_category(extension):
    for category, extensions in categories.items():
        if extension in extensions:
            return category
    return 'Other'

def move_files():
    if not os.path.exists(path):
        print("Path not found")
        return  
    directory_list = os.listdir(path)
    for item in directory_list:
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path) and not item.startswith('.'):               
            _, file_extension = os.path.splitext(item)
            destination_path = os.path.join(path, find_file_category(file_extension))
            os.makedirs(destination_path, exist_ok=True)
            if args.dry_run:
                print(f"Would move {item} to {destination_path}")
            else:
                try:
                    shutil.move(item_path, destination_path)
                    print(f"Moved {item} to {destination_path}")
                except Exception as e:
                    print(f"Error occured while moving files.\n{e}")

if __name__ == '__main__':
    move_files()
