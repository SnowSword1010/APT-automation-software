import send_im
import tkinter


def send_file(ip, filename1, filename2, monitor_no):
    print(monitor_no)
    print(ip)
    print(filename1)
    print(filename2)

    message = tkinter.StringVar()
    message.set("")

    success = tkinter.StringVar()
    success.set("")
    
    failure = tkinter.StringVar()
    failure.set("")

    if(filename1 == "" or filename2 == ""):
        message.set("Kindly select both File 1 and File 2.\nIf case you want only one image to be displayed on the monitor, select the same image in both File 1 and File 2. Otherwise select distinct images.")
    else:
        send_im.send_im(ip, filename1, filename2, monitor_no, success, failure)
        if(success.get() != ""):
            message.set("Connection established.\nGiven images have been displayed on monitor")
        else:
            message.set("Connection could not be established.\nGiven images could not be displayed on monitor")
    
    tkinter.messagebox.showinfo("Status", message.get())
    



    
