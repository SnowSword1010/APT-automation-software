import send_im
import tkinter

# send_file() function => used to send chosen files to specific monitor numbers on current production line
# parameter 1 => ip => ip address of the monitor that needs to receive the files
# parameter 2 => filename1 => File Name 1
# parameter 3 => filename2 => File Name 2
# parameter 4 => monitor_no => monitor number to send files to on the current production line
def send_file(ip, filename1, filename2, monitor_no):

    # tkinter variable that stores message to be 
    # displayed once the operation is complete
    message = tkinter.StringVar()
    message.set("")

    # tkinter variable that gets changed from ""
    # if the operation is successful
    success = tkinter.StringVar()
    success.set("")
    # tkinter variable that gets changed from ""
    # if the operation is not successful
    failure = tkinter.StringVar()
    failure.set("")

    # CHECK TO ENSURE BOTH FILENAME FIELDS ARE FILLED BEFORE SENDING IMAGES TO MONTIOR
    if(filename1 == "" or filename2 == ""):
        # Message to be displayed when operation is not valid
        message.set("Kindly select both File 1 and File 2.\nIf case you want only one image to be displayed on the monitor, select the same image in both File 1 and File 2. Otherwise select distinct images.")
    else:
        # Sends the given images to the specific monitor
        send_im.send_im(ip, filename1, filename2, monitor_no, success, failure)
        if(success.get() != ""):
            # Message to be displayed when operation is successful
            message.set("Connection established.\nGiven images have been displayed on monitor")
        else:
            # Message to be displayed when operation is unsuccessful
            message.set("Connection could not be established.\nGiven images could not be displayed on monitor")
    
    # Display message to user
    tkinter.messagebox.showinfo("Status", message.get())
    



    
