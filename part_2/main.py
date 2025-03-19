import tkinter as tk
from tkinter import ttk

root = tk.Tk()

list_container_rows = 0
list_container: ttk.Frame = None

root.title("YouTube Music Downloader")
root.minsize(width=350, height=50)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Main content frame, contains everything
content = ttk.Frame(root, padding=(5, 5, 5, 5))
content.grid(row=0, column=0, sticky=(tk.N, tk.E, tk.W, tk.S))
content.grid_rowconfigure(0, pad=5)
content.grid_columnconfigure(0, weight=10)

# Grid Row 0: Button
download_button = ttk.Button(content, text="Download")
download_button.grid(row=0, column=0,
                     sticky=(tk.W, tk.E, tk.N))

# Grid Row 1: Separator
separator = ttk.Separator(content, orient=tk.HORIZONTAL)
separator.grid(row=1, column=0, sticky=(tk.E, tk.W, tk.N))

# Grid Row 2: Frame named list_container, which contains a sub-grid

content.grid_rowconfigure(2, weight=90)

list_container = ttk.Frame(content, padding=(5, 5, 5, 5))
list_container.grid(row=2, column=0, sticky=(tk.W, tk.N, tk.E))
list_container.grid_columnconfigure(0, weight=90)
list_container.grid_columnconfigure(1, weight=10)

# Each of list_container's rows will have an Entry and a Label

entry_1 = ttk.Entry(list_container)
entry_1.grid(row=0, column=0, sticky=(tk.E, tk.W))
label_1 = ttk.Label(list_container, text="Ready")
label_1.grid(row=0, column=1, sticky=(tk.S, tk.E))

list_container.grid_rowconfigure(0, weight=10)

root.mainloop()
