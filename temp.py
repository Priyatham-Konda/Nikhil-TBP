import tkinter as tk
from tkinter import filedialog

def select_file():
    filename = filedialog.askopenfilename()
    file_label.config(text=filename)

def submit():
    header_text = header_entry.get()
    file_path = file_label.cget("text")
    
    # Process the header_text and file_path here
    
    # For demonstration, print them
    print("Header Text:", header_text)
    print("File Path:", file_path)

# Create main window
root = tk.Tk()
root.title("File Upload")

# Header label and entry
header_label = tk.Label(root, text="Header:")
header_label.pack(pady=(10, 0))

header_entry = tk.Entry(root)
header_entry.pack(pady=(0, 10), padx=10, ipadx=50)

# File selection button and label
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack(pady=10)

file_label = tk.Label(root, text="No file selected")
file_label.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

# Run the main event loop
root.mainloop()
