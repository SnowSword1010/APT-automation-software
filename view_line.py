import tkinter as tk

def view(lineObjs, line_no):

    top = tk.Toplevel()

    # LINE NUMBER WIDGET
    HeadingFont = tk.font.Font(family = "Raleway", size = 13, weight="bold")
    HeadingContent = "Line" + str(line_no + 1) + " Configuration"
    HeadingLabel = tk.Label(top, text = HeadingContent, font = HeadingFont, justify="center")
    HeadingLabel.grid(row=0, column = 0, pady = 5, columnspan=6)

    # PC FIELD WIDGET
    pcFieldFont = tk.font.Font(family = "Helvetica", size = 12, weight="bold")
    pcFieldLabel = tk.Label(top, text = "PC", font = pcFieldFont)
    pcFieldLabel.grid(row=1, column = 0, padx = (10, 5), pady = 5)

    # IP ADDRESS WIDGET
    ipFieldFont = tk.font.Font(family = "Helvetica", size = 12, weight="bold")
    ipFieldLabel = tk.Label(top, text = "IP Address", font = ipFieldFont)
    ipFieldLabel.grid(row=1, column = 1, padx=15, pady = 5)

    pcObjs = []

    class PC:
        # instance variables => pc_no, ip_address, remove_button, update_ip_button, browse_button, send_file_button
        def __init__(self, pc_no):

            def click():
                print("Yo")
                return
            
            self.pc_no_label = tk.Label(top, text = pc_no)
            self.ip_address_label = tk.Label(top, text = "192.168.2.3")
            self.remove_button = tk.Button(top, text="Remove PC", command=lambda: click(), padx=10, pady=5)
            self.update_ip_button = tk.Button(top, text="Update IP", command=lambda: click(), padx=10, pady=5)
            self.browse_file_button = tk.Button(top, text="Browse File", command=lambda: click(), padx=10, pady=5)
            self.send_file_button = tk.Button(top, text="Send File", command=lambda: click(), padx=10, pady=5)

            return
    
    for i in range(0, 12):
        tempPC = PC(i)
        pcObjs.append(tempPC)
        pcObjs[i].pc_no_label.grid(row=i+2, column=0, padx=(81, 81), pady=(8,5))
        pcObjs[i].ip_address_label.grid(row=i+2, column=1, padx=(81, 81), pady=(8,5))
        pcObjs[i].remove_button.grid(row=i+2, column=2, padx=(81, 81), pady=(8,5))
        pcObjs[i].update_ip_button.grid(row=i+2, column=3, padx=(81, 81), pady=(8,5))
        pcObjs[i].browse_file_button.grid(row=i+2, column=4, padx=(81, 81), pady=(8,5))
        pcObjs[i].send_file_button.grid(row=i+2, column=5, padx=(81, 81), pady=(8,5))
    
    return