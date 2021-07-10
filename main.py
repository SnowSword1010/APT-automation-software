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
HeadingFont = tkinter.font.Font(family = "Raleway", size = 12, weight="bold")
HeadingText = "Configure Lines"
HeadingLabel = tk.Label(root, text = HeadingText, font=HeadingFont, justify="left")
HeadingLabel.grid(row=3, column=0, sticky='W', columnspan = 3)

global lineObjs
lineObjs = []

class line:
    def __init__(self, line_button, select_dir_button, send_button):
        self.line_button = line_button
        self.select_dir_button = select_dir_button
        self.send_button = send_button

def click():
    return


for i in range(0, 6):
    line_button = tk.Button(root, text="Line " + str(i+1), command=lambda: click(), padx=10, pady=5)
    select_dir_button = tk.Button(root, text="Select Folder", command=lambda: click(), padx=10, pady=5)
    send_button = tk.Button(root, text="Send", command=lambda: click(), padx=10, pady=5)

    temp = line(line_button, select_dir_button, send_button)
    lineObjs.append(temp)

    lineObjs[i].line_button.grid(row=i+5, column=0, padx=(81, 81), pady=(8,5))
    lineObjs[i].select_dir_button.grid(row=i+5, column=1, padx=(81, 81), pady=(8,5))
    lineObjs[i].send_button.grid(row=i+5, column=2, padx=(81 , 81), pady=(8,5))


# # ADD, REMOVE, UPDATE BUTTON WIDGETS
# add_button = tk.Button(root, text="Add Line", command=lambda: add_line_clicked(), padx=10, pady=(5))
# update_button = tk.Button(root, text="Update Line", command=lambda: click(), padx=10, pady=5)
# remove_button = tk.Button(root, text="Remove Line", command=lambda: click(), padx=10, pady=5)

# add_button.grid(row=4, column=0, padx=(81,81), pady=(5,10))
# update_button.grid(row=4, column=1, padx=(81,81), pady=(5,10))
# remove_button.grid(row=4, column=2, padx=(81,81), pady=(5,10))

root.mainloop()