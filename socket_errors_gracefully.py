import sys, socket, argparse

def main():
    """
    Title: Handling socket errors gracefully
    >>> python socket_errors.py -h
    usage: socket_errors_gracefully.py [-h] [--host HOST] [--port PORT] [--file FILE]

    optional arguments:
    -h, --help   show this help message and exit
    --host HOST
    --port PORT
    --file FILE
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    args = parser.parse_args()
    host = args.host
    port = args.port
    filename = args.file

    try:
        """
        create socket
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)

    try:
        """
        connect to given host/port
        # Address-related error connectig to server: [Errno 8] nodename nor servname provided, or not known
        # Connection error: [Errno 61] Connection refused
        """
        s.connect((host,port))
    except socket.gaierror as e:
        print("Address-related error connectig to server: %s" % e)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)

    try:
        """
        sending data
        # Error sending data: [Errno 57] Socket is not connected
        """
        msg = "GET %s HTTP/1.0\r\n\r\n" % filename
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(1)

    while 1:
        try:
            """
            waiting to receive data from remote host
            """
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf.decode('utf-8'))
if __name__ == '__main__':
    main()
