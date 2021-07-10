import tkinter as tk
import tkinter.font
from PIL import Image, ImageTk
import tkinter.filedialog

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

# each element represents line buttons (line, select folder, send)
global lineObjs
lineObjs = []

class line:

    # instance variables => {browse_text, line_button, select_dir_button, send_button}
    def __init__(self):

        # variable that stores the state of our select folder button
        self.browse_text = tk.StringVar()

        # function used to update the text of select folder button ; also used to get the store the selected directory path
        def open_folder():
            folder_selected = tkinter.filedialog.askdirectory()
            print(folder_selected)
            if(folder_selected == ()):
                self.browse_text.set("Select Folder")
            else:
                arr = folder_selected.split('/')
                text = arr[len(arr) - 1]
                text = (text[:10] + '...') if len(text) > 13 else text
                self.browse_text.set(text)
            return

        # line_button => gives info pertaining to a line
        self.line_button = tk.Button(root, text="Line " + str(i+1), command=lambda: click(), padx=10, pady=5)

        # select_dir button => adding browse functionality
        self.select_dir_button = tk.Button(root, textvariable=self.browse_text, command=lambda: open_folder(), padx=10, pady=5)
        self.browse_text.set("Select Folder")


        self.send_button = tk.Button(root, text="Send", command=lambda: click(), padx=10, pady=5)

def click():
    return

for i in range(0, 6):
    temp = line()
    lineObjs.append(temp)
    lineObjs[i].line_button.grid(row=i+5, column=0, padx=(81, 81), pady=(8,5))
    lineObjs[i].select_dir_button.grid(row=i+5, column=1, padx=(81, 81), pady=(8,5))
    lineObjs[i].send_button.grid(row=i+5, column=2, padx=(81 , 81), pady=(8,5))

root.mainloop()