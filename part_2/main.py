import tkinter as tk
from tkinter import ttk


def make_rows(parent, count):
    # Each of list_container's rows will have an Entry and a Label
    for i in range(0, count):
        entry = ttk.Entry(parent)
        entry.grid(row=i, column=0, sticky=(tk.E, tk.W))
        label = ttk.Label(parent, text="Ready")
        label.grid(row=i, column=1, sticky=(tk.S, tk.E))
    parent.grid_rowconfigure(0, weight=10)

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
                     sticky=(tk.N, tk.E, tk.W))

# Grid Row 1: Separator
separator = ttk.Separator(content, orient=tk.HORIZONTAL)
separator.grid(row=1, column=0, sticky=(tk.N, tk.E, tk.W))

# Grid Row 2: Frame named list_container, which contains a sub-grid

content.grid_rowconfigure(2, weight=90)

list_container = ttk.Frame(content, padding=(5, 5, 5, 5))
list_container.grid(row=2, column=0, sticky=(tk.N, tk.E, tk.W))
list_container.grid_columnconfigure(0, weight=90)
list_container.grid_columnconfigure(1, weight=10)

make_rows(list_container, 10)

root.mainloop()
