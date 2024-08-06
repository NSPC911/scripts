import os
import time
import zipfile
from pathlib import Path

# Path to the directory where .zip files are located
directory_to_watch = f"{os.path.expanduser("~")}{os.path.sep}Downloads"
print(f"Watching {directory_to_watch}")

# Function to extract and delete .zip files
def extract_and_delete_zip(zip_path):
    # Get the file name without the extension
    folder_name = zip_path.stem
    
    # Create a new folder with the same name as the file
    output_folder = zip_path.parent / folder_name
    
    # If the folder doesn't exist, create it
    if not output_folder.exists():
        output_folder.mkdir()

    # Open the .zip file as a ZIP archive and extract it
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)
    
    # Delete the original .zip file
    zip_path.unlink()

    print(f"Extracted '{zip_path.name}' to '{output_folder}', then deleted the source file.")

# Main loop to check for new .zip files
while True:
    # Get a list of all .zip files in the directory
    zip_files = list(Path(directory_to_watch).glob("*.zip"))

    for zip_path in zip_files:
        print(f'\rFound {str(zip_path).split(str(os.path.sep))[-1]}!')
        # If the folder with the same name doesn't exist, extract and delete the file
        corresponding_folder = zip_path.parent / zip_path.stem
        print(f'Extracting at {corresponding_folder}')
        extract_and_delete_zip(zip_path)
    try:
        for i in range(2):
            # Waits 8 seconds but in a cool way
            print("\r-", end="")
            time.sleep(1)
            print("\r\\", end="")
            time.sleep(1)
            print("\r|", end="")
            time.sleep(1)
            print("\r/", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\rKeyboard Interrupt")
        exit(1)
