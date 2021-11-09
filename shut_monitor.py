import os
import socket
import time


def shut_monitor(ip):
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 1024 # send 1024 bytes each time step
    host = str(ip)
    port = 5002
    SHUTDOWN = True
    filename1 = 'fin1'
    filename2 = 'fin2'

    filesize1 = len(filename1)
    filesize2 = len(filename2)
    s = socket.socket()
    print(f"Trying to shutdown {host}:{port}")
    try:
        s.settimeout(15)
        s.connect((host, port))
        s.settimeout(None)

        print("Connection established")
        time.sleep(4)
        s.send(f"{SHUTDOWN}{SEPARATOR}{filename1}{SEPARATOR}{filesize1}{SEPARATOR}{filename2}{SEPARATOR}{filesize2}".encode("utf-16"))
        print("Shutdown instruction sent")
        time.sleep(4)
        recMsg = s.recv(BUFFER_SIZE)
        print(recMsg)
        print(f"{host}:{port} successfully turned off")
        
    except:
        pass
    finally:
        print("Closing connection.")
        s.close()
    pass