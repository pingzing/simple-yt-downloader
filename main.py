import tkinter as tk
from tkinter import ttk
import itertools

root = tk.Tk()
song_counter_value = tk.DoubleVar()

list_container_rows = 0
list_container: ttk.Frame = None

def main():
    root.title("YouTube Music Downloader")
    root.minsize(width=350, height=50)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Main content frame, contains everything
    content = ttk.Frame(root, padding=(5, 5, 5, 5))
    content.grid(row=0, column=0, sticky=(tk.N, tk.E, tk.W, tk.S))

    # Grid Row 0: Label, spinbox, button

    song_label = ttk.Label(content, text="Songs")
    song_label.grid(row=0, column=0, stick=(tk.E))

    song_counter_value.set(0)
    song_counter_picker = ttk.Spinbox(
        content, from_=0, to=20, wrap=True, width=5, textvariable=song_counter_value)
    song_counter_picker.set(0)
    song_counter_picker.grid(row=0, column=1, sticky=(tk.W))

    create_button = ttk.Button(content, text="Create", command=generate_list)
    create_button.grid(row=0, column=2, sticky=(tk.E))

    content.grid_rowconfigure(0, weight=10)
    content.grid_columnconfigure(0, weight=100)
    content.grid_columnconfigure(1, weight=100)

    # Grid Row 1: Separator
    separator = ttk.Separator(content, orient=tk.HORIZONTAL)
    separator.grid(row=1, column=0, columnspan=3, sticky=(tk.E, tk.W))

    content.grid_rowconfigure(1, weight=10)

    # Grid Row 2: Frame, scrollbar
    # Frame's grid has rows of:
    # Editbox, Label

    global list_container
    list_container = ttk.Frame(content, padding=(5, 5, 5, 5))
    list_container.grid(row=2, column=0)

    content.grid_rowconfigure(2, weight=80)

    root.mainloop()


def generate_list():
    new_count = int(song_counter_value.get())

    for list_item in list_container.grid_slaves():
        list_item.grid_remove()

    for i in range(0, new_count):
        label = ttk.Label(list_container, text=f"Test {i}")
        label.grid(row=i, column=0)


main()
