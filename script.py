import os
import re
import sys
import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        organize_file(file_path, folder_to_write)

def organize_existing_files(folder_to_watch, folder_to_write):
    for root, _, files in os.walk(folder_to_watch):
        for file in files:
            file_path = os.path.join(root, file)
            organize_file(file_path, folder_to_write)

def organize_file(file_path, folder_to_write):
    filename = os.path.basename(file_path)
    
    # Extracting date/time and file name
    date_time, file_name = extract_date_time_and_name(filename)
    
    if date_time and file_name:
        folder_path = os.path.join(folder_to_write, file_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        new_file_path = os.path.join(folder_path, filename)
        
        # Check for duplicate files in the destination folder
        if os.path.exists(new_file_path):
            fileext = os.path.splitext(filename);
            new_filename = find_available_name(folder_path, fileext[0], fileext[1])
            new_file_path = os.path.join(folder_path, new_filename)
            
        move_fileto(file_path, new_file_path)
    else:
        print(f"No match found for: {filename}")

def move_fileto(file_path, new_file_path):
    retries = 3
    while(retries > 0):
        retries -= 1
        try:
            os.rename(file_path, new_file_path)
            print(f"Moved {filename} to {new_filename} folder")
        except (IOError, OSError) as e:
            print("error")
            time.sleep(3)
        except:
            pass

def find_available_name(folder_path, base_name, extension):
    # Append a numerical suffix to the base name until an available name is found
    suffix = 2
    while True:
        new_name = f"{base_name} ({suffix}){extension}"
        new_path = os.path.join(folder_path, new_name)
        if not os.path.exists(new_path):
            return new_name
        suffix += 1

def extract_date_time_and_name(filename):
    # Define a pattern to capture the date/time information
    pattern = r'(\d{1,2}_\d{1,2}_\d{4} \d{1,2}_\d{1,2}_\d{1,2} [APMapm]+|\d{4}-\d{2}-\d{2} \d{2}-\d{2}-\d{2})'
    
    parts = re.split(pattern, filename, maxsplit=1)
    
    if len(parts) > 1:
        file_name = parts[0].strip()
        date_time = parts[1].strip()
        return date_time, file_name
    else:
        return None, None

def watch_folder(folder_path):
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)  # Do nothing; let the event handler handle file creation events
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <folder_to_watch> <folder_to_write>")
        sys.exit(1)

    folder_to_watch = sys.argv[1]
    folder_to_write = sys.argv[2]

    if not os.path.exists(folder_to_watch) or not os.path.isdir(folder_to_watch):
        print(f"Error: {folder_to_watch} is not a valid directory.")
        sys.exit(1)

    if not os.path.exists(folder_to_write) or not os.path.isdir(folder_to_write):
        print(f"Error: {folder_to_write} is not a valid directory.")
        sys.exit(1)

    organize_existing_files(folder_to_watch, folder_to_write)
    watch_folder(folder_to_watch)
