import tkinter.filedialog
import os

# function used to update the text of select folder button ; also used to get the store the selected directory path in folder variable
# parameter 1 => browse_text => stores text written on 'select folder' button => type = tk.StringVar => changed using the set method
# parameter 2 => folder => stores chosen folder path => type = tk.StringVar => changed using the set method
def open_folder(browse_text, folder):
    print(os.getcwd())
    folder_selected = tkinter.filedialog.askdirectory(initialdir=os.getcwd()+'/APT_Images')
    # if no folder is selected
    if(folder_selected == ()):
        folder.set("")
    else:
        # truncates the folder name to 13 characters max
        arr = folder_selected.split('/')
        text = arr[len(arr) - 1]
        text = (text[:10] + '...') if len(text) > 13 else text
        # browse_text variable set
        browse_text.set(text)
        # folder name set
        folder.set(folder_selected)
    return