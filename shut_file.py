import tkinter
import shut_monitor

# A bit misleading name of the function;
# This function facilitates generation of appropriate error messages
# as that would not have been achieved by calling the shut_monitor() function directly
def shut_file(ip, monitor_no):
    # stores the state of the message to be displayed to the user
    message = tkinter.StringVar()
    message.set("")

    # tkinter StringVar success updated if connection with the chosen monitor 
    # is established and shutdown process is in execution
    success = tkinter.StringVar()
    success.set("")
    
    # tkinter StringVar failure updated if connection with the chosen monitor
    # could not be established
    failure = tkinter.StringVar()
    failure.set("")

    # function call the shut down the chosen monitor
    shut_monitor.shut_monitor(ip, success, failure, monitor_no)

    # if tkinter StringVar success changes then connection was established with the
    # monitor and hence it got to execute shutdown instruction ; otherwise not
    if(success.get() != ""):
        message.set("Monitor shutdown successfully")
    else:
        message.set("Monitor could not be shutdown as connection could not be established.")
    
    # print message for the user
    tkinter.messagebox.showinfo("Status", message.get())