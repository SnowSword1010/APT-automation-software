import tkinter
import shut_monitor
def shut_file(ip, monitor_no):
    print(ip)
    print(monitor_no)

    message = tkinter.StringVar()
    message.set("")

    success = tkinter.StringVar()
    success.set("")
    
    failure = tkinter.StringVar()
    failure.set("")

    shut_monitor.shut_monitor(ip, success, failure, monitor_no)

    if(success.get() != ""):
        message.set("Monitor shutdown successfully")
    else:
        message.set("Monitor could not be shutdown as connection could not be established.")
    
    tkinter.messagebox.showinfo("Status", message.get())