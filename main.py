import tkinter as tk
from tkinter import ttk

root = tk.Tk()
song_counter_value = tk.DoubleVar()

list_container_rows = 0
list_container = None

def main():
    root.title("YouTube Music Downloader")
    root.minsize(width=350, height=50)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Main content frame, contains everything
    content = ttk.Frame(root, padding=(5, 5, 5, 5))
    content.grid(row=0, column=0, sticky=(tk.N, tk.E, tk.W, tk.S))

    # Grid Row 0: Label & spinbox

    song_label = ttk.Label(content, text="Songs")
    song_label.grid(row=0, column=0, stick=(tk.E))

    song_counter_value.set(0)
    song_counter_value.trace_add("write", on_value_changed)
    song_counter_picker = ttk.Spinbox(
        content, from_=0, to=20, wrap=True, width=5, textvariable=song_counter_value)
    song_counter_picker.set(0)
    song_counter_picker.grid(row=0, column=1, sticky=(tk.W))

    content.grid_rowconfigure(0, weight=20)
    content.grid_columnconfigure(0, weight=100)
    content.grid_columnconfigure(1, weight=100)

    # Grid Row 1: Separator
    separator = ttk.Separator(content, orient=tk.HORIZONTAL)
    separator.grid(row=1, column=0, columnspan=2, sticky=(tk.E, tk.W))

    # Grid Row 2: Frame, scrollbar
    # Frame's grid has rows of:
    # Editbox, Label

    list_container = ttk.Frame(content, padding=(5, 5, 5, 5))
    list_container.grid(row=1, column=0)

    content.grid_rowconfigure(1, weight=80)

    root.mainloop()


def on_value_changed(var, index, mode):
    new_val = song_counter_value.get()
    update_list(new_val)


def update_list(new_count):
    if (list_container == None):
        return

    if (new_count == list_container_rows):
        return

    difference = new_count - list_container_rows
    if (difference < 0):
        # remove rows
        raise NotImplementedError()
    else:
        # add rows
        raise NotImplementedError()


main()
