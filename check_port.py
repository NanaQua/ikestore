import socket
import os
import subprocess

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex(('127.0.0.1', port))
        return result == 0

port = 8000
if check_port(port):
    print(f"Port {port} is in use.")
    # Attempt to find the process using the port
    try:
        # This command will work on Windows
        output = subprocess.check_output(f"netstat -ano | findstr :{port}", shell=True).decode()
        print(f"Processes using port {port}:\n{output}")
    except subprocess.CalledProcessError:
        print("Could not retrieve process information.")
else:
    print(f"Port {port} is free.")