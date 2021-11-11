import socket
import time

# function to shut down one monitor remotely
# The main idea is to be able to send a boolean
# value shutdown = true so that the monitor 
# identifies it and executes the shutdown 
# routine
def shut_monitor(ip, connected, failed, monitor_no):
    
    # used to separate different parameters received from socket stream
    SEPARATOR = "<SEPARATOR>"
    # send 1024 bytes each time
    BUFFER_SIZE = 1024
    # host and port of monitor; 
    # essential for socket connection establishment
    host = str(ip)
    port = 5002

    # Critical line for this function to do its job properly
    # SHUTDOWN must be True
    SHUTDOWN = True

    # doesn't have any practical significance but since the montiors accept only
    # the specified format of input, two filenames and their sizes must be given
    filename1 = 'fin1'
    filename2 = 'fin2'
    filesize1 = len(filename1)
    filesize2 = len(filename2)

    # Creating a socket
    s = socket.socket()
    print(f"Trying to shutdown {host}:{port}")
    try:
        # The program has 15 seconds to establish connection
        # with the monitor. It'll timeout after that.
        s.settimeout(15)
        s.connect((host, port))
        # If the connection is established, then the timout
        # must be removed as different image sizes may have
        # different transfer times
        s.settimeout(None)

        print("Connection established")

        # small delay before the transfer begins
        time.sleep(5)
        # send the shutdown, filename1, filesize1, filename2 and filesize2 variables
        # The encoding is done because a socket can only transfer a sequence of bytes
        # String is a sequence of characters, therefore it is encoded to bytes
        s.send(f"{SHUTDOWN}{SEPARATOR}{filename1}{SEPARATOR}{filesize1}{SEPARATOR}{filename2}{SEPARATOR}{filesize2}".encode("utf-16"))

        # Helpful in debugging ; checks whether the above data
        # gets sent successfully or not ; uncomment to use
        # print("Shutdown instruction sent")

        # small delay to prevent data loss; facilitates synchronisation
        time.sleep(4)

        # waiting for acknowledgement from monitor side
        recMsg = s.recv(BUFFER_SIZE)

        # Helpful in debugging ; checks whether acknowlegement
        # from monitor gets received or not ; uncomment to use
        # print(recMsg)

        # If the code reaches at this point without any exceptions
        # then it could be concluded that the monitor has successfully
        # been shutdown; so connected tkinter StringVar needs to be updated
        connected.set(connected.get() + str(monitor_no) + " ")
        
    except:
        # If an exception occurs in the code then the monitor has not
        # been shutdown; so failed tkinter StringVar needs to be updated
        failed.set(failed.get() + str(monitor_no) + " ")

    finally:
        # for debugging
        # print("Closing connection.")
        s.close()
    pass