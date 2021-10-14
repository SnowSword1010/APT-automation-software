import os
from glob import glob
from os.path import join
import socket
import time

def send_im(ip, im1, im2):
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096 # send 4096 bytes each time step
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
        s.connect((host, port))
        print("[+] Connected.")
        time.sleep(1)
        # send the filename1 and filesize
        s.send(f"{shutdown}{SEPARATOR}{twoImage}{SEPARATOR}{filename1}{SEPARATOR}{filesize1}{SEPARATOR}{filename2}{SEPARATOR}{filesize2}".encode("utf-16"))
        print("Sent stuff")

        time.sleep(0.1)

        recMsg = s.recv(1024)
        print(recMsg)
        i1 = open(filename1, "rb")
        for k in i1:
            s.send(k)
        time.sleep(0.5)
        s.send(b"next")

        recMsg = s.recv(1024)
        print(recMsg)

        i2 = open(filename2, "rb")
        for k in i2:
            s.send(k)
        time.sleep(0.5)
        s.send(b'nex')
        print("hey")

    finally:
        print("Closing connection.")
        s.close()

def send_folder(folderPath, monitorDictionary):
    print(folderPath)
    # lists all files in the chosen directory
    allFiles = os.listdir(folderPath)
    # array that stores image files address only
    images = []
    for ext in ('*.jpeg', '*.png', '*.jpg'):
        images.extend(glob(join(folderPath, ext)))

    if(len(images) == 0):
        print("Selected folder should have atleast one PNG, JPG or JPEG image")
    elif(len(images) != len(allFiles)):
        print("Selected folder should have only PNG, JPG, AND JPEG images")
    else:
        n = len(images) # denotes number of images
        m = len(monitorDictionary) # denotes number of monitors

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
                send_im(monitorDictionary[str(monitor_no)], folderPath + "/" + allFiles[counter], folderPath + "/" + allFiles[counter+1])
                counter+=2
            
        for i in range(n1, n):
            monitor_no = i+1
            if(counter >= n):
                break
            else:
                send_im(monitorDictionary[str(monitor_no)], folderPath + "/" +  allFiles[counter], folderPath + "/" + allFiles[counter])
                counter+=1
            
        print(n1)
        print(n2)