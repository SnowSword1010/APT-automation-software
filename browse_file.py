from tkinter import filedialog
import tkinter.filedialog

# open_file() function => 
# parameter 1 => top => tkinter top level ; on which the entire content specific to production line is rendered
# parameter 2 => browse_text => stores the state of select file button
# parameter 3 => file => stores the state of filename
def open_file(top, browse_text, file):
    # Only files ending with .PNG, .JPG/.JEPG are allowed to be selected
    file_selected = tkinter.filedialog.askopenfile(parent=top, mode="rb", title="Choose a file", filetypes=[("Images", "*.png"),("Images", "*.jpg"),("Images", "*.jpeg")])
    # if no file is selected
    if(file_selected == ()):
        file.set("")
    else:
        # truncates the file name to 13 characters max
        arr = file_selected.name.split('/')
        text = arr[len(arr) - 1]
        text = (text[:10] + '...') if len(text) > 13 else text
        # browse_text variable set
        browse_text.set(text)
        # file name set
        file.set(file_selected.name)
    return