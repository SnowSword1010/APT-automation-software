import tkinter as tk
import tkinter.font
from PIL import Image, ImageTk

root = tk.Tk()

root.title("APT Electronics AutoConfig")
# sets the initial size of root window
# canvas = tk.Canvas(root, width=650, height=900)
# initialises the canvas (spans it into 3 invisible columns)
# canvas.grid()


# LOGO WIDGET
# converting our image to pillow image
logo = Image.open('./images/logo.png')
# converting our pillow image to Tkinter image
logo = ImageTk.PhotoImage(logo)
# putting our Tkinter image into a widget
logo_label = tk.Label(image=logo)
# critical line ; can't be skipped
logo_label.image = logo
logo_label.grid(column=0, row=0, columnspan=3)

# SUBTITLE WIDGET
subtitleFont = tkinter.font.Font(family = "Raleway", size = 12, slant="italic", weight="bold")
subtitleLabel = tk.Label(root, text = "Automation Software", font = subtitleFont, justify="center")
subtitleLabel.grid(row=1, column = 0, pady = 5, columnspan=3)

# INSTRUCTIONS WIDGET
instructionsFont = tkinter.font.Font(family = "Raleway", size = 12)
instructionsText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
instructionsLabel = tk.Label(root, text = instructionsText, font = instructionsFont, justify="center", wraplength=700)
instructionsLabel.grid(row=2, column=0, pady= (20,15), columnspan=3)

# CONFIGURE LINES WIDGET
# HeadingFont = tkinter.font.Font(family = "Raleway", size = 12, weight="bold")
# HeadingText = "Configure Lines"
# HeadingLabel = tk.Label(root, text = HeadingText, font=HeadingFont, justify="left")
# HeadingLabel.grid(row=3, column=0, sticky='W', columnspan = 3)
global lineObjs
lineObjs = []
global r
r = 0

class line:
    def __init__(self, line_button, select_dir_button, send_button) -> None:
        self.line_button = line_button
        self.select_dir_button = select_dir_button
        self.send_button = send_button

# CREATE LINE FUNCTION
def createDummyLine():
    line_button = tk.Button(root, text="Line", command=lambda: custom_click(), padx=10, pady=5)
    select_dir_button = tk.Button(root, text="Select Folder", command=lambda: custom_click(), padx=10, pady=5)
    send_button = tk.Button(root, text="Send", command=lambda: custom_click(), padx=10, pady=5)

    temp = line(line_button, select_dir_button, send_button)
    lineObjs.append(temp)
    print(lineObjs)
    j = 0
    for widgets in frame.winfo_children():
        if(j > 2):
            widgets.destroy()
            global r
            r=1
        j+=1
    
    for i in range(0, len(lineObjs)):
        lineObjs[i].line_button.grid(row=r, column=0, padx=(81, 81))
        lineObjs[i].select_dir_button.grid(row=r, column=1, padx=(81, 81))
        lineObjs[i].send_button.grid(row=r, column=2, padx=(81 , 81))
        r+=1

    # line_button.grid(row=0, column=0, padx=(81, 81))
    # select_dir_button.grid(row=0, column=1, padx=(81, 81))
    # send_button.grid(row=0, column=2, padx=(81 , 81))

# LINE FUNCTIONS
def custom_click():
    print("I was clicked")
    return

# ADD, REMOVE, UPDATE BUTTON FUNCTIONS

def add_line_clicked():
    createDummyLine()
    print("Add line clicked")
    return

def update_line_clicked():
    print("Update line clicked")
    return

def remove_line_clicked():
    print("Remove line clicked")
    return

# ADD, REMOVE, UPDATE BUTTON FRAME
frame = tk.LabelFrame(root, text="Configure Lines", pady=10)
frame.grid(row=3, column=0, columnspan=3, sticky='W')

# ADD, REMOVE, UPDATE BUTTON WIDGETS
add_button = tk.Button(frame, text="Add Line", command=lambda: add_line_clicked(), padx=10, pady=5)
update_button = tk.Button(frame, text="Update Line", command=lambda: update_line_clicked(), padx=10, pady=5)
remove_button = tk.Button(frame, text="Remove Line", command=lambda: remove_line_clicked(), padx=10, pady=5)

add_button.grid(row=r, column=0, padx=(81, 81))
update_button.grid(row=r, column=1, padx=(81, 81))
remove_button.grid(row=r, column=2, padx=(81 , 81))
r+=1

for i in range(0, len(lineObjs)):
    lineObjs[i].line_button.grid(row=r, column=0, padx=(81, 81))
    lineObjs[i].select_dir_button.grid(row=r, column=1, padx=(81, 81))
    lineObjs[i].send_button.grid(row=r, column=2, padx=(81 , 81))
    r+=1

root.mainloop()