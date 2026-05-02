# Clean up files in the home directory
import os

folder_source = '/home/user/'
folder_destination = '/home/user/CleanedUp'
try:
    os.mkdir(folder_destination)
except FileExistsError as e:
    print(f"Folder exists \n{e}")
    
entries = os.scandir(folder_source)
for entry in entries:
    if os.path.isfile(entry):
        # Omit dotfiles
        if not entry.name.startswith('.'):
            print(f'File: {entry.name}')
            os.rename(os.path.join(folder_source, entry.name), os.path.join(folder_destination, entry.name))
