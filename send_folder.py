import os
from glob import glob
from os.path import join
import send_im
import tkinter

# send_folder() function => used to send specific files in the selected folder to specific 
# monitors on the current production line
# parameter 1 => folder_path => stores the folder_path from which images are to be sent
# parameter 2 => monitorDictionary => copy of ip_address_table of chosen production line
def send_folder(folderPath, monitorDictionary, root):

    # tkinter variable that stores the monitor numbers with which
    # the software could successfully establish socket connection
    connected = tkinter.StringVar()
    # initial value of connected
    connected.set("Monitors successfully connected: ")
    # tkinter variable that stores the monitor numbers with which
    # the software couldn't successfully establish socket connection
    failed = tkinter.StringVar()
    # initial value of failed
    failed.set("Monitors not successfully connected: ")

    # allFiles is an array that stores all the files in the chosen folder
    allFiles = os.listdir(folderPath)
    # sorting the files
    allFiles.sort()
    
    # array that only stores image file addresses from the chosen folder
    # it is due to this array that we can apply checks on extensions of images present in the folder
    images = []
    # only JPEG/JPG and PNG extensions available for use
    for ext in ('*.jpeg', '*.png', '*.jpg'):
        # pushes the images with appropriate extensions inside the images array
        images.extend(glob(join(folderPath, ext)))

    # len(images) == 0  means that the folder is empty
    if(len(images) == 0):
        tkinter.messagebox.showinfo("Error","Selected folder should have atleast one PNG, JPG or JPEG image.")
    # len(images) != len(allFiles) indicates that the folder despite containing images with appropriate extensions also some other files
    # such folders are not selected for the efficiency of the algorithm
    elif(len(images) != len(allFiles)):
        tkinter.messagebox.showinfo("Error","Make sure all the files in the chosen folder end with .png (or) .jpg (or) .jpeg\nNote even if all the extensions are the same as specified, ensure that the file name also ends with the extension.\nExample: 'image_no.png (2)' will not work")
    # if the above two cases are not match then the system would prepare to establish connections with the monitors on the chosen line
    else:

        ###################### DECISION MAKING ALGORITHM ######################
        # 1. Calculate total no of images to send (n) and total no of monitors (m)
        # 2. It is assumed that all monitors would display two images with a specified lag - 
        # some would display two different images while others would display the same image twice
        # n1 = monitors with different displays
        # n2 = monitors with duplicate displays
        # 3. Calculate n-m
        # 4. if n-m > 0:
        #       n1 = n-m ; n2 = m
        #    else:
        #       n1 = 0 ; n2 = n
        # 5. Loop over monitors with multiple displays and call the send_im function giving
        #    ip_address, image_address_1 and image_address_2 as 3 parameters
        # 6. Loop over monitors with single displays and call the send_im function giving 
        #    the ip_address and image_address twice as 3 parameters
        #######################################################################

        # denotes number of images
        n = len(images)
        # denotes number of monitors
        m = len(monitorDictionary)
        # denotes the number of monitors involved;
        monitors_involved = 0

        if(n-m > 0):
            # n1 monitors will have multiple displays
            # n2 monitors will have single display
            n1 = n-m
            n2 = m
            monitors_involved = 13
        else:
            # all monitors will have single display
            n1 = 0
            n2 = n
            monitors_involved = n

        # counter is pointer to the index of the image to be sent
        counter = 0

        # tkinter Toplevel window to show status of connections
        progressBar = tkinter.Toplevel(root)
        # prevents the users from interacting with any window other than progressBar
        progressBar.grab_set()
        progressBar.geometry('400x100')
        progressBar.title("Status of connections")
        # Contents of progressBar window
        tkinter.Label(progressBar, text="The application is running.", font=("Raleway 10 bold italic")).pack()
        tkinter.Label(progressBar, text="This may take upto a few minutes. Please wait!\n", font=("Raleway 10 bold italic", 10)).pack()
        tkinter.Label(progressBar, text="Monitors involved: "+str(monitors_involved), font=("Helvetica 11 bold")).pack()
        status = tkinter.Label(progressBar, text="Starting ...", font=("Helvetica 11 bold"))
        status.pack()
        # this line is critical to render the above tkinter labels properly
        progressBar.update()

        for i in range(0, n1):
            monitor_no = i+1
            if(counter >= n):
                break
            else:
                try:
                    # removes the last item packed
                    status.pack_forget()
                    status = tkinter.Label(progressBar, text="Reaching out to monitor " + str(monitor_no) + " ...", font=("Helvetica 11 bold"))
                    # packs the current label
                    status.pack()
                    # this line is critical to render the currently packed tkinter label properly
                    progressBar.update()
                    # sending image
                    send_im.send_im(monitorDictionary[str(monitor_no)], folderPath + "/" + allFiles[counter], folderPath + "/" + allFiles[counter+1], monitor_no, connected, failed)
                except:
                    pass
                # counter is incremented by 2 because two distinct images are being sent
                counter+=2
            
        for i in range(n1, n):
            monitor_no = i+1
            if(counter >= n):
                break
            else:
                try:
                    # removes the last item packed
                    status.pack_forget()
                    status = tkinter.Label(progressBar, text="Reaching out to monitor " + str(monitor_no) + " ...", font=("Helvetica 11 bold"))
                    # packs the current label
                    status.pack()
                    # this line is critical to render the currently packed tkinter label properly
                    progressBar.update()
                    # sending image
                    send_im.send_im(monitorDictionary[str(monitor_no)], folderPath + "/" +  allFiles[counter], folderPath + "/" + allFiles[counter], monitor_no, connected, failed)
                except:
                    pass
                # counter is incremented by 1 because only one distinct image is being sent
                counter+=1

        # destroys progressBar tkinter toplevel
        progressBar.destroy()
        # displays a message box mentioning monitor_numbers that were successfully
        # and unsuccessfully connected
        tkinter.messagebox.showinfo("Connection Status", "Monitors Involved: " + str(monitors_involved) + "\n\n" + connected.get() + "\n\n" + failed.get())