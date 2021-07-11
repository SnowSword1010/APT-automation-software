import tkinter.filedialog

# function used to update the text of select folder button ; also used to get the store the selected directory path
# parameter 1 => lineObjs => array of lines
# parameter 2 => line_no => index of the targeted line
# parameter 3 => browse_text => stores text written on 'select folder' button => type = tk.StringVar => changed using the set method
# parameter 4 => folder => stores chosen folder path => type = tk.StringVar => changed using the set method
def open_folder(lineObjs, line_no, browse_text, folder):
    folder_selected = tkinter.filedialog.askdirectory()
    if(folder_selected == ()):
        folder.set("")
    else:
        arr = folder_selected.split('/')
        text = arr[len(arr) - 1]
        text = (text[:10] + '...') if len(text) > 13 else text
        browse_text.set(text)
        folder.set(folder_selected)
    return