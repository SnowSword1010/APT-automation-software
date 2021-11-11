import shut_file
import tkinter as tk

# custom functions import
import browse_file
import send_file

def view(lineObjs, line_no, ip_address_table):

    top = tk.Toplevel()

    # LINE NUMBER WIDGET
    HeadingFont = tk.font.Font(family = "Raleway", size = 13, weight="bold")
    HeadingContent = "Line " + str(line_no + 1) + " Configuration"
    HeadingLabel = tk.Label(top, text = HeadingContent, font = HeadingFont, justify="center")
    HeadingLabel.grid(row=0, column = 0, pady = 5, columnspan=6)

    # PC FIELD WIDGET
    pcFieldFont = tk.font.Font(family = "Helvetica", size = 12, weight="bold")
    pcFieldLabel = tk.Label(top, text = "Monitor", font = pcFieldFont)
    pcFieldLabel.grid(row=1, column = 0, padx = (10, 5), pady = 5)

    pcObjs = []

    class PC:
        # instance variables => pc_no, ip_address, remove_button, update_ip_button, browse_button, send_file_button
        def __init__(self, pc_no):

            self.browse_file_1_text = tk.StringVar()
            self.file_1 = tk.StringVar()
            self.browse_file_1_text.set("Select File 1")
            self.file_1.set("")

            self.browse_file_2_text = tk.StringVar()
            self.file_2 = tk.StringVar()
            self.browse_file_2_text.set("Select File 2")
            self.file_2.set("")

            self.pc_no_label = tk.Label(top, text = (str)(pc_no+1))
            self.ip_address = ip_address_table.get("line"+str(line_no+1)).get(str(pc_no+1))
            self.browse_file_1_button = tk.Button(top, textvariable=self.browse_file_1_text, command=lambda: browse_file.open_file(top, self.browse_file_1_text, self.file_1), padx=10, pady=5)
            self.browse_file_2_button = tk.Button(top, textvariable=self.browse_file_2_text, command=lambda: browse_file.open_file(top, self.browse_file_2_text, self.file_2), padx=10, pady=5)
            self.send_file_button = tk.Button(top, text="Send File", command=lambda: send_file.send_file(ip_address_table["line"+str(line_no+1)][str(pc_no+1)], self.file_1.get(), self.file_2.get(), str(pc_no+1)), padx=10, pady=5)
            self.shutdown_button = tk.Button(top, text="Shutdown", command=lambda: shut_file.shut_file((ip_address_table["line"+str(line_no+1)])[str(pc_no+1)], str(pc_no+1)), padx=10, pady=5)

            return
    
    for i in range(0, 12):
        tempPC = PC(i)
        pcObjs.append(tempPC)
        pcObjs[i].pc_no_label.grid(row=i+2, column=0, padx=(81, 81), pady=(8,5))
        pcObjs[i].browse_file_1_button.grid(row=i+2, column=1, padx=(81, 81), pady=(8,5))
        pcObjs[i].browse_file_2_button.grid(row=i+2, column=2, padx=(81, 81), pady=(8,5))
        pcObjs[i].send_file_button.grid(row=i+2, column=3, padx=(81, 81), pady=(8,5))
        pcObjs[i].shutdown_button.grid(row=i+2, column=4, padx=(81, 81), pady=(8,5))
    
    return