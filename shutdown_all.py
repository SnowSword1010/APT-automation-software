import shut_monitor

def shutdown_all(ips):
    m = len(ips)
    print(m)
    for i in range(0, m):
        monitor_no = i+1
        shut_monitor.shut_monitor(ips[str(monitor_no)])
        pass