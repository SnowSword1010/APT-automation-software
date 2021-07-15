from tkinter import filedialog
import tkinter.filedialog

def open_file(top, browse_text, file):
    file_selected = tkinter.filedialog.askopenfile(parent=top, mode="rb", title="Choose a file", filetypes=[("Pdf file", "*.pdf"),("Images", "*.png"),("Images", "*.jpg"),("Images", "*.jpeg")])
    if(file_selected == ()):
        file.set("")
    else:
        arr = file_selected.name.split('/')
        text = arr[len(arr) - 1]
        text = (text[:10] + '...') if len(text) > 13 else text
        browse_text.set(text)
        file.set(file_selected)
    return