import time
import os
import socket

# send_im() function => does the heavylifting of sending filename1 (name of image 1)
# and filename2 (name of image 2) to the chosen monitor
# parameter 1 => ip => denotes ip address of chosen monitor
# parameter 2 => filename1 => denotes name of image 1
# parameter 3 => filename2 => denotes name of image 2
# parameter 4 => monitor_no => denoted monitor number of chosen monitor on the current production line
# parameter 5 => connected => tkinter variable updated when connection with monitor is successful
# parameter 6 => failed => tkinter variable updated when connection with monitor is unsuccessful
def send_im(ip, filename1, filename2, monitor_no, connected, failed):
    # used to separate different parameters received from socket stream
    SEPARATOR = "<SEPARATOR>"
    # send/receive 1024 bytes each time
    BUFFER_SIZE = 1024
    # host and port of monitor; essential for socket connection establishment
    host = str(ip)
    port = 5002

    # Getting filesizes of the filenames
    filesize1 = os.path.getsize(filename1)
    filesize2 = os.path.getsize(filename2)

    # doesn't have any practical significance but since the montiors accept only
    # the specified format of input, shutdown variable is given False value
    shutdown = False

    # Creating a socket
    s = socket.socket()
    print(f"[+] Trying to connect to {host}:{port}")
    try:
        # The program has 15 seconds to establish connection
        # with the monitor. It'll timeout after that.
        s.settimeout(15)
        s.connect((host, port))
        # If the connection is established, then the timout
        # must be removed as different image sizes may have
        # different transfer times
        s.settimeout(None)

        print("[+] Connected.")
        # small delay before the transfer begins
        time.sleep(5)
        # send the shutdown, filename1, filesize1, filename2 and filesize2 variables
        # The encoding is done because a socket can only transfer a sequence of bytes
        # String is a sequence of characters, therefore it is encoded to bytes
        s.send(f"{shutdown}{SEPARATOR}{filename1}{SEPARATOR}{filesize1}{SEPARATOR}{filename2}{SEPARATOR}{filesize2}".encode("utf-16"))
        
        # Helpful in debugging ; checks whether the above data
        # gets sent successfully or not ; uncomment to use
        # print("Sent stuff")

        # small delay to prevent data loss; facilitates synchronisation
        time.sleep(4)

        # waiting for acknowledgement from monitor side
        recMsg = s.recv(BUFFER_SIZE)

        # Helpful in debugging ; checks whether acknowlegement
        # from monitor gets received or not ; uncomment to use
        # print(recMsg)

        # transfer image im1 1024 bytes at a time
        with open(filename1, "rb") as f1:
            while True:
                bytes_read = f1.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.send(bytes_read)
        
        # small delay to prevent data loss; facilitates synchronisation
        time.sleep(4)
        # The byte string b'n' when received by the monitor would
        # mark the end of filename1. The monitor would prepare to
        # receive the next image
        s.send(b'n')

        recMsg = s.recv(BUFFER_SIZE)
        # Helpful in debugging ; checks whether acknowlegement
        # from monitor gets received or not ; uncomment to use
        # print(recMsg)

        # transfer image im2 1024 bytes at a time
        with open(filename2, "rb") as f2:
            while True:
                bytes_read = f2.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.send(bytes_read)
        
        # small delay to prevent data loss; facilitates synchronisation
        time.sleep(4)

        # The byte string b'nex' when received by the monitor would
        # mark the end of filename2. The monitor would prepare to close
        # the connection
        s.send(b'nex')
        

        recMsg = s.recv(BUFFER_SIZE)
        # Helpful in debugging ; checks whether acknowlegement
        # from monitor gets received or not ; uncomment to use
        # print(recMsg)

        # If the code reaches at this point without any exceptions
        # then it could be concluded that the monitor has successfully
        # received the images; so connected tkinter StringVar needs to be updated
        connected.set(connected.get() + str(monitor_no) + " ")

    except:
        # If an exception occurs in the code then the monitor has not
        # successfully received the images; so so failed tkinter StringVar needs to be updated
        failed.set(failed.get() + str(monitor_no) + " ")
        pass

    finally:
        # for debugging
        print("Closing connection.")
        s.close()