import socket, sys
from sys import argv
script, host = argv
"""
python2.x, python3.x
사용법: # python port_scanner.py 127.0.0.1(or www.abc.com)
"""
def check_port():
    port_open=[]
    for port in range(1, 65536):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5);
            result = s.connect_ex((host,port))
            if result == 0:
                port_open.append(port)
                print(port, 'port is open')
        except KeyboardInterrupt:
            break   # Ctrl+c를 누르면 아무런 예외 메시지 없이 프로그램 종료
        except (socket.gaierror, socket.error, socket.timeout) as e:
            pass
    print("열린 포트 : %s" % (port_open))
if __name__ == '__main__':
    check_port()
