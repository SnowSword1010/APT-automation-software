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
logo_label.grid(column=0, row=0)

# SUBTITLE WIDGET
subtitleFont = tkinter.font.Font(family = "Raleway", size = 12, slant="italic", weight="bold")
subtitleLabel = tk.Label(root, text = "Automation Software", font = subtitleFont, justify="center")
subtitleLabel.grid(row=1, column = 0, pady = 5)

# INSTRUCTIONS WIDGET
instructionsFont = tkinter.font.Font(family = "Raleway", size = 12)
instructionsText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
instructionsLabel = tk.Label(root, text = instructionsText, font = instructionsFont, justify="center", wraplength=700)
instructionsLabel.grid(row=2, column=0, pady= (20,0))

root.mainloop()