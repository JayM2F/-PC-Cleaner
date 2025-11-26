import os # Interact with OS
import shutil # Delete folders/files
import ctypes # To use windows features
import time # For Delays
from datetime import datetime # for the timestamps in log file

# Task  -> Convert bytes to MB/GB
def format_size(bytes_value):
    if bytes_value > 1024 * 1024 * 1024:
        return f"{bytes_value / (1024*1024*1024):.2f} GB" # Format to gigabytes
    else:
        return f"{bytes_value / 1024*1024:.2f} MB" # Format to Megabytes


# Task  -> Delete all the files in path

def delete_in_path(path):
    total_deleted = 0 # Keep track of whats deleted
    if not os.path.exists(path): #If path doesnt exist
        return 0

    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                file_path = os.path.join(root, file) #gets the full file path
                size = os.path.getsize(file_path) # gets file path size
                os.remove(file_path) # remove the file
                total_deleted += size # shows total size
            except:
                pass # ignore protected system files
        for folder in dirs:
            try:
                folder_path = os.path.join(root, folder) # gets the folder path
                shutil.rmtree(folder_path) # delete the folder
            except:
                pass
    return total_deleted

# Task  -> Empty the recycling bin

def empty_recycle_bin():
    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x00000001) #shemtpyreciclebinw -> clears windows recycle bin
        return True
    except:
        return False

# Task -> Clear browser Caches

def clean_browser_caches():
    print("\n🌐 Cleaning Browser Caches...\n")
    
    # paths for Chrome, Edge, Firefox caches
    browser_paths = {
        "Google Chrome": os.path.expandvars(
            r"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Cache"
        ),
        "Chrome Code Cache": os.path.expandvars(
            r"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Code Cache"
        ),
        "Chrome GPUCache": os.path.expandvars(
            r"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\GPUCache"
        ),
        "Microsoft Edge": os.path.expandvars(
            r"C:\Users\%USERNAME%\AppData\Local\Microsoft\Edge\User Data\Default\Cache"
        ),
        "Edge Code Cache": os.path.expandvars(
            r"C:\Users\%USERNAME%\AppData\Local\Microsoft\Edge\User Data\Default\Code Cache"
        ),
        "Mozilla Firefox": os.path.expandvars(
            r"C:\Users\%USERNAME%\AppData\Local\Mozilla\Firefox\Profiles"
        ),
    }

    total_cleaned = 0

    # clean each browser path
    for name, path in browser_paths.items():
        cleaned = delete_in_path(path)
        print(f"✔ {name} — Freed {format_size(cleaned)}")
        total_cleaned += cleaned

    return total_cleaned

# Task -> Logs
def write_log(message):
    log_folder = os.path.expandvars(r"C:\Users\%USERNAME%\Documents\PC_Cleaner_Logs")
    os.makedirs(log_folder, exist_ok=True)  # make folder if it doesn't exist
    log_file = os.path.join(log_folder, "cleaner_log.txt")
    with open(log_file, "a") as f:
        f.write(message + "\n")



# Task  -> Main cleaner function
def run_cleaner():
    print("\n Running PC Cleaner...")
    time.sleep(0.5) # 0.5 seconds
    temp_paths = [
        r"C:\Windows\Temp",
        r"C:\Users\%USERNAME%\AppData\Local\Temp",
        r"C:\Windows\Prefetch"
  ]
    total_space_free = 0
    
    # Go through every path
    for path in temp_paths:
        cleaned = delete_in_path(os.path.expandvars(path)) # delete junk
        print(f"Cleaned: {path} - Freed {format_size(cleaned)}") # Show The path cleaned and how much space it freed
        total_space_free += cleaned # add to the total
    
    # Go thorugh recycling bin
    if empty_recycle_bin():
        print("Recycle Bin has been Emptied Successfully")
    else:
        print("Error -> Recycling Bin could not be Emptied")
    print(f"Total Space Freed:{format_size(total_space_free)}")
    print(f"Thanks for using my Tool, Cleaing is Done!")
if __name__ == "__main__":
    run_cleaner()
