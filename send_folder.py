import os
from glob import glob
from os.path import join
import socket
import time
# import signal

def handler(signum, frame):
    raise Exception("end of time")

# def countdown():
#     global my_timer
#     my_timer = 20
#     for x in range(20):
#         my_timer = my_timer-1
#         time.sleep(1)
    
#     print("Out of time")

def send_im(ip, im1, im2):
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 1024 # send 1024 bytes each time step
    host = str(ip)
    port = 5002

    filename1 = im1
    filename2 = im2

    print("filename1: " + str(filename1))
    print("filename1: " + str(filename2))

    filesize1 = os.path.getsize(filename1)
    filesize2 = os.path.getsize(filename2)

    shutdown = False
    twoImage = True
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    try:
        # signal.signal(signal.SIGALRM, handler)
        # signal.alarm(20)
        s.settimeout(15)
        s.connect((host, port))
        s.settimeout(None)
        # except Exception as exc:
        #     print(exc)
            # s.close()
            # return

        print("[+] Connected.")
        time.sleep(10)
        # send the filename1 and filesize
        s.send(f"{shutdown}{SEPARATOR}{twoImage}{SEPARATOR}{filename1}{SEPARATOR}{filesize1}{SEPARATOR}{filename2}{SEPARATOR}{filesize2}".encode("utf-16"))
        print("Sent stuff")

        time.sleep(4)

        recMsg = s.recv(1024)
        print(recMsg)

        print(filename1)
        with open(filename1, "rb") as f1:
            while True:
                bytes_read = f1.read(1024)
                if not bytes_read:
                    break
                s.send(bytes_read)
        # i1 = open(filename1, "rb")
        # for k in i1:
        #     s.send(k)
        
        time.sleep(4)
        s.send(b'n')

        print("blah")
        recMsg = s.recv(1024)
        print(recMsg)

        print(filename2)
        with open(filename2, "rb") as f2:
            while True:
                bytes_read = f2.read(1024)
                if not bytes_read:
                    break
                s.send(bytes_read)

        # i2 = open(filename2, "rb")
        # for k in i2:
        #     s.send(k)
        
        time.sleep(4)
        s.send(b'nex')
        print("hey")
        recMsg = s.recv(1024)
        print(recMsg)

    finally:
        print("Closing connection.")
        s.close()

def send_folder(folderPath, monitorDictionary):
    print(folderPath)
    # lists all files in the chosen directory
    allFiles = os.listdir(folderPath)
    allFiles.sort()
    # array that stores image files address only
    images = []
    for ext in ('*.jpeg', '*.png', '*.jpg'):
        images.extend(glob(join(folderPath, ext)))

    if(len(images) == 0):
        print("Selected folder should have atleast one PNG, JPG or JPEG image")
    elif(len(images) != len(allFiles)):
        print("Make sure all the files in the chosen folder end with .png / .jpg / .jpeg")
    else:
        n = len(images) # denotes number of images
        m = len(monitorDictionary) # denotes number of monitors
        
        print(images)
        print(monitorDictionary)

        if(n-m > 0):
            # n1 monitors will have multiple displays
            # n2 monitors will have single display
            n1 = n-m
            n2 = m
        else:
            # all monitors will have single display
            n1 = 0
            n2 = n
        
        print(allFiles)
        counter = 0
        for i in range(0, n1):
            monitor_no = i+1
            if(counter >= n):
                break
            else:
                try:
                    send_im(monitorDictionary[str(monitor_no)], folderPath + "/" + allFiles[counter], folderPath + "/" + allFiles[counter+1])
                except:
                    pass

                counter+=2
            
        for i in range(n1, n):
            monitor_no = i+1
            if(counter >= n):
                break
            else:
                try:
                    send_im(monitorDictionary[str(monitor_no)], folderPath + "/" +  allFiles[counter], folderPath + "/" + allFiles[counter])
                except:
                    pass
                counter+=1
            
        print(n1)
        print(n2)