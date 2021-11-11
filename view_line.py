import tkinter as tk
# custom modules import
import shut_file
import browse_file
import send_file

def view(lineObjs, line_no, ip_address_table):
    # Creating a subwindow
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

    # pcObjs array would contain monitors and individual feature buttons associated with them
    pcObjs = []

    class PC:
        def __init__(self, pc_no):

            # browse_file_1_text variable stores the state of Select File 1 button
            # Initial value is "Select File 1"
            self.browse_file_1_text = tk.StringVar()
            self.browse_file_1_text.set("Select File 1")
            # file_1 variable stores the address of the chosen file
            # Initial value is ""
            self.file_1 = tk.StringVar()
            self.file_1.set("")

            # browse_file_2_text variable stores the state of Select File 1 button
            # Initial value is "Select File 2"
            self.browse_file_2_text = tk.StringVar()
            self.browse_file_2_text.set("Select File 2")
            # file_2 variable stores the path address of the chosen file
            # Initial value is ""
            self.file_2 = tk.StringVar()
            self.file_2.set("")

            # Label that displays the monitor number
            self.pc_no_label = tk.Label(top, text = (str)(pc_no+1))
            # variable to store IP address of the particular monitor
            self.ip_address = ip_address_table.get("line"+str(line_no+1)).get(str(pc_no+1))
            # browse_file_1_button and browse_file_2_button => adds browse file functionality ; updates file_1 and file_2 variables to store the address of chosen file
            self.browse_file_1_button = tk.Button(top, textvariable=self.browse_file_1_text, command=lambda: browse_file.open_file(top, self.browse_file_1_text, self.file_1), padx=10, pady=5)
            self.browse_file_2_button = tk.Button(top, textvariable=self.browse_file_2_text, command=lambda: browse_file.open_file(top, self.browse_file_2_text, self.file_2), padx=10, pady=5)
            # send_file_button => sends file_1 and file_2 to the selected monitor on the current production line
            self.send_file_button = tk.Button(top, text="Send File", command=lambda: send_file.send_file(ip_address_table["line"+str(line_no+1)][str(pc_no+1)], self.file_1.get(), self.file_2.get(), str(pc_no+1)), padx=10, pady=5)
            # shutdown_button => shut downs the selected monitor on current production line
            self.shutdown_button = tk.Button(top, text="Shutdown", command=lambda: shut_file.shut_file((ip_address_table["line"+str(line_no+1)])[str(pc_no+1)], str(pc_no+1)), padx=10, pady=5)
            return
    
    # iterates over all monitors and initialises the above variables and buttons
    # max number of monitors = 13 on each production line
    for i in range(0, 13):
        tempPC = PC(i)
        pcObjs.append(tempPC)
        # rendering the labels and buttons
        pcObjs[i].pc_no_label.grid(row=i+2, column=0, padx=(81, 81), pady=(8,5))
        pcObjs[i].browse_file_1_button.grid(row=i+2, column=1, padx=(81, 81), pady=(8,5))
        pcObjs[i].browse_file_2_button.grid(row=i+2, column=2, padx=(81, 81), pady=(8,5))
        pcObjs[i].send_file_button.grid(row=i+2, column=3, padx=(81, 81), pady=(8,5))
        pcObjs[i].shutdown_button.grid(row=i+2, column=4, padx=(81, 81), pady=(8,5))
    return