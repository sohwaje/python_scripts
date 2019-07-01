"""
네트워크 관련 애플리케이션에서 socket.error 모듈을 이용하여 에러를 처리하는 코드
객체 생성, 서버 연결, 데이터 전송, 응답 대기
"""
import sys
import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action='store', dest='host', required=False)
    parser.add_argument('--port', action='store', dest='port', type=int, required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file


#첫번째 try-except block : 소켓 생성 블록

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket : %s" % e)
        sys.exit(1)


#두번째 try-except block : 주어진 host/port로 연결 시도

    try:
        s.connect((host, port))
        print("Success %s" % host)
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)


#세번째 try-except block : 데이터 보내기 시도

#    try:
#        s.sendall(("GET %s HTTP/1.0\r\n\r\n" % filename).encode())
#    except socket.error as e:
#        print("Error sending data: %s" % e)
#        sys.exit(1)

#네번째 try-except block : 원격지 호스트로부터 데이터를 수신하기 위해 기다린다

#    while 1:
#        try:
#            buf = s.recv(2048)
#        except socket.error as e:
#            print("Error receiving data: %s" % e)
#            sys.exit(1)
#            if not len(buf):
#                break
#            sys.stdout.write(buf)

if __name__ == '__main__':
    main()
