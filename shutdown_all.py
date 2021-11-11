import shut_monitor
import tkinter



# function to shutdown all monitors of the chosen
# production line
# parameter1 = ips = denotes a dictionary of all
# monitors of a line mapped with their ip addresses
def shutdown_all(ips):

    # tkinter variable that stores the monitor numbers
    # that shutdown successfully
    connected = tkinter.StringVar()
    # initial value of connected
    connected.set("Monitors successfully shutdown: ")
    # tkinter variable that stores the monitor numbers
    # that shutdown successfully
    failed = tkinter.StringVar()
    # initial value of failed
    failed.set("Monitors not successfully shutdown: ")

    # loop over the dictionary ips 
    for i in range(0, len(ips)):
        monitor_no = i+1
        # shutting down individual monitors
        shut_monitor.shut_monitor(ips[str(monitor_no)], connected, failed, monitor_no)

    # displays a message box mentioning monitor_numbers that were successfully
    # and unsuccessfully connected
    tkinter.messagebox.showinfo("Shutdown Status", connected.get() + "\n" + failed.get())