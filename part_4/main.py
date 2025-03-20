import tkinter as tk
from tkinter import ttk
import yt_dlp


def make_rows(number_of_rows, parent):
    for i in range(0, number_of_rows):
        entry = ttk.Entry(list_container)
        entry.grid(row=i, column=0, sticky=(tk.E, tk.W))
        label = ttk.Label(list_container, text="Ready")
        label.grid(row=i, column=1, sticky=(tk.E))

        parent.grid_rowconfigure(i, weight=10)


def download_songs(list_items):
    downloader = yt_dlp.YoutubeDL(
        {"extract_audio": True, "format": "bestaudio", "outtmpl": "%(title)s.mp3"})
    for index in range(0, len(list_items), 2):
        label: ttk.Label = list_items[index]
        entry: ttk.Entry = list_items[index + 1]

        video_address = entry.get()
        label.configure(text="Downloading...")
        try:
            downloader.download(video_address)
            label.configure(text="Done!")
        except Exception as e:
            print("Got exception while downloading: " + str(e))
            label.configure(text="Oho")


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
content.grid_rowconfigure(0, pad=5, weight=0)
content.grid_columnconfigure(0, weight=1)

# Grid Row 0: Button
download_button = ttk.Button(
    content, text="Download", command=lambda: download_songs(list_container.grid_slaves()))
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

# Each of list_container's rows will have an Entry and a Label

make_rows(10, list_container)

root.mainloop()
