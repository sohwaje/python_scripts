# local_port_scanner.py
import socket

def find_service_name():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    protocolname = 'tcp'
    for port in range(1, 1024):
        result = sock.connect_ex(('127.0.0.1',port))
        if result == 0:
            print(port, 'port is open')
        else:
            print(port, 'port is not open')

if __name__ == '__main__':
    find_service_name()
