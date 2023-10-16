import socket
import threading
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()

ip = input("Enter IP: ")
thread_count = (int(input("Enter thread count (150 recommended): ")))

def scan_ip(ip, port):
    socket__ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket__.settimeout(1)
    try:
        socket__.connect((ip, port))
        socket__.close()
        with lock:
            print(f"Open Port: {port}")
    except:
        pass

with ThreadPoolExecutor(max_workers=thread_count) as exe:
    for port in range(65535):
        exe.submit(scan_ip, ip, port + 1)
