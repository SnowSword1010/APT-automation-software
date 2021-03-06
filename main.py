import tkinter as tk
import tkinter.font
from PIL import Image, ImageTk
import tkinter.filedialog

# custom modules import
import view_line
import open_folder
import send_folder
import shutdown_all

# IP ADDRESSES OF RASPBERRY PIs
ip_address_table = {
    "line1" : {
        "1" : "10.0.0.10",
        "2" : "10.0.0.11",
        "3" : "10.0.0.12",
        "4" : "10.0.0.13",
        "5" : "10.0.0.14",
        "6" : "10.0.0.15",
        "7" : "10.0.0.16",
        "8" : "10.0.0.17",
        "9" : "10.0.0.18",
        "10" : "10.0.0.19",
        "11" : "10.0.0.20",
        "12" : "10.0.0.21",
        "13" : "10.0.0.22"
    },
    "line2" : {
        "1" : "10.0.0.40",
        "2" : "10.0.0.41",
        "3" : "10.0.0.42",
        "4" : "10.0.0.43",
        "5" : "10.0.0.44",
        "6" : "10.0.0.45",
        "7" : "10.0.0.46",
        "8" : "10.0.0.47",
        "9" : "10.0.0.48",
        "10" : "10.0.0.49",
        "11" : "10.0.0.50",
        "12" : "10.0.0.51",
        "13" : "10.0.0.52"
    },
    "line3" : {
        "1" : "10.0.0.70",
        "2" : "10.0.0.71",
        "3" : "10.0.0.72",
        "4" : "10.0.0.73",
        "5" : "10.0.0.74",
        "6" : "10.0.0.75",
        "7" : "10.0.0.76",
        "8" : "10.0.0.77",
        "9" : "10.0.0.78",
        "10" : "10.0.0.79",
        "11" : "10.0.0.80",
        "12" : "10.0.0.81",
        "13" : "10.0.0.82"
    }
}

# Creation of root window
root = tk.Tk()
# Setting the title of root window
root.title("APT Electronics AutoConfig")


# LOGO WIDGET
# converting our logo to pillow image
logo = Image.open('./images/logo.png')
# converting our pillow image (logo) to Tkinter image
logo = ImageTk.PhotoImage(logo)
# putting our Tkinter image (logo) into a widget
logo_label = tk.Label(image=logo)
# critical line ; can't be skipped
logo_label.image = logo
# positioning the logo in grid
logo_label.grid(column=0, row=0, columnspan=4)

# SUBTITLE WIDGET
subtitleFont = tkinter.font.Font(family = "Raleway", size = 12, slant="italic", weight="bold")
subtitleLabel = tk.Label(root, text = "Automation Software", font = subtitleFont, justify="center")
subtitleLabel.grid(row=1, column = 0, pady = 5, columnspan=4)

# INSTRUCTIONS WIDGET
instructionsFont = tkinter.font.Font(family = "Raleway", size = 12)
instructionsText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
instructionsLabel = tk.Label(root, text = instructionsText, font = instructionsFont, justify="center", wraplength=700)
instructionsLabel.grid(row=2, column=0, pady= (20,15), columnspan=4)

# CONFIGURE LINES WIDGET
HeadingFont = tkinter.font.Font(family = "Raleway", size = 12, weight="bold")
HeadingText = "Configure Lines"
HeadingLabel = tk.Label(root, text = HeadingText, font=HeadingFont, justify="left")
HeadingLabel.grid(row=3, column=0, sticky='W', columnspan = 4)

# each element of lineObjs represents line buttons (line, select folder, send)
# this variable is useful when passing line button details to other modules
global lineObjs
lineObjs = []

class line:

    # instance variables => {browse_text, line_button, select_dir_button, send_button}
    def __init__(self, line_no):

        # variable that stores the state of our select folder button
        self.browse_text = tk.StringVar()
        # folder variable stores the path address of the chosen folder
        self.folder = tk.StringVar()

        # line_button => gives info pertaining to a line
        self.line_button = tk.Button(root, text="Line " + str(line_no+1), command=lambda: view_line.view(lineObjs, line_no, ip_address_table), padx=10, pady=5)


        # select_dir button => adds browse folder functionality ; updates folder variable to store the path address of chosen folder
        self.select_dir_button = tk.Button(root, textvariable=self.browse_text, command=lambda: open_folder.open_folder(self.browse_text, self.folder), padx=10, pady=5)
        # initial value of browse_folder variable
        self.browse_text.set("Select Folder")
        # initial value of set folder varible
        self.folder.set("")

        # send_button => sends specific files in the selected folder to specific monitors on the current production line
        self.send_button = tk.Button(root, text="Send", command=lambda: send_folder.send_folder(self.folder.get(), ip_address_table["line"+str(line_no+1)], root), padx=10, pady=5)

        # shutdown_button => shuts down all the monitors on the given line
        self.shutdown_button = tk.Button(root, text="Shutdown all monitors", command=lambda: shutdown_all.shutdown_all(ip_address_table["line"+str(line_no+1)]), padx=10, pady=5)

# Since the max number of production lines is 3, this loop iterates thrice creating line_button, select_folder_button, 
# send_button and shutdown_button for every line
for i in range(0, 3):
    temp = line(i)
    lineObjs.append(temp) 
    lineObjs[i].line_button.grid(row=i+5, column=0, padx=(50, 50), pady=(8,5))
    lineObjs[i].select_dir_button.grid(row=i+5, column=1, padx=(50, 50), pady=(8,5))
    lineObjs[i].send_button.grid(row=i+5, column=2, padx=(50, 50), pady=(8,5))
    lineObjs[i].shutdown_button.grid(row=i+5, column=3, padx=(50, 50), pady=(8,5))

root.mainloop()