import socket

def test_socket_modes():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 소켓을 생성한다.
    s.setblocking(0)                                        # 소켓을 블록킹 모드로 설정한다.
    s.settimeout(0.5)                                       # 소켓의 타임 아웃을 0.5로 설정한다.
    s.bind(("127.0.0.1", 0))
    # 소켓을 address에 바인딩 한다. 바인딩 포트를 자동으로 지정하려면 0을, 수동으로 하려면 0대신 적절한 포트를 할당한다.

    socket_address = s.getsockname()                        # 소켓 자신의 주소를 반환한다.
    print("Trivial Server lauched on socket: %s" % str(socket_address))
    while(1):
        s.listen(2)                                          # listen(2)에 지정된 개수만큼 서버가 연결을 수락한다.

if __name__ == '__main__':
    test_socket_modes()
