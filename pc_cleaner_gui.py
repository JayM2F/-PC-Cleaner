import os # Interact with OS
import shutil # Delete folders/files
import ctypes # To use windows features
import time # For Delays
from datetime import datetime # for the timestamps in log file
import tkinter as tk
from tkinter import messagebox, scrolledtext

#Colours
light_blue = "#2596be"
red = "#ea4f4f"
grey = "#292929"
green = "#008702"





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

# Task -> Main Cleaner

def run_cleaner():
    log_text.insert(tk.END, "\n🚀 Running PC Cleaner...\n")
    log_text.see(tk.END)
    root.update()

    temp_paths = [
        r"C:\Windows\Temp",
        r"C:\Users\%USERNAME%\AppData\Local\Temp",
        r"C:\Windows\Prefetch"
    ]
    total_space_free = 0

    # Clean temp folders
    for path in temp_paths:
        cleaned = delete_in_path(os.path.expandvars(path))
        log_text.insert(tk.END, f"✔ Cleaned: {path} - Freed {format_size(cleaned)}\n")
        log_text.see(tk.END)
        total_space_free += cleaned
        root.update()

    # Clean recycle bin
    if empty_recycle_bin():
        log_text.insert(tk.END, "🗑 Recycle Bin emptied successfully!\n")
    else:
        log_text.insert(tk.END, "❌ Recycling Bin could not be emptied!\n")
    log_text.see(tk.END)
    root.update()

    # Clean browser caches
    cleaned_browsers = clean_browser_caches()
    log_text.insert(tk.END, f"🌐 Browser Caches Freed: {format_size(cleaned_browsers)}\n")
    log_text.see(tk.END)
    total_space_free += cleaned_browsers
    root.update()

    # Final summary
    summary_message = f"Cleaning Complete!\n\nTotal Space Freed: {format_size(total_space_free)}"
    log_text.insert(tk.END, f"\n💾 TOTAL Space Freed: {format_size(total_space_free)}\n")
    log_text.see(tk.END)
    root.update()

    messagebox.showinfo("PC Cleaner Summary", summary_message)


# Task -> GUI SETUP (Tkinter)
root = tk.Tk() # Make Window
root.title("PC Cleaner") # Window Title Bar
root.geometry("600x500") # Window Size
root.resizable(False, False) # Not Resizable
root.configure(bg="white") # Backdrop

#Title Label at the Top
title_label = tk.Label(root, text="PC Cleaner Tool", font=("Helvetica", 40, "bold"))
title_label.place(x=100, y=0)

#Owner Name at Top
title_label_jaym2f = tk.Label(root, text="by JayM2F", font=("Helvetica", 10, "bold"))
title_label_jaym2f.place(x=250, y=65)

#Run Cleaner Button
run_button = tk.Button(root, text="Run Cleaner", font=("Helvetica", 15), bg=green, fg="white", command=run_cleaner)
run_button.place(x=220, y= 100)

#Exit Cleaner Button
exit_button = tk.Button(root, text="Exit Cleaner", font=("Helvetica", 10), bg=red, fg="white", command=root.quit)
exit_button.place(x=10, y = 460)

#Log Display
log_text = scrolledtext.ScrolledText(root, width=50, height=10)
log_text.place(x=100, y=160)

#Log Realtime Stats
log_text.insert(tk.END, "Press 'Run Cleaner' to start the process\n")
log_text.see(tk.END)
root.update
root.mainloop()
