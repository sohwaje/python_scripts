# host_to_ip.py
import socket
from sys import argv
from binascii import hexlify

script, file_name = argv
"""
파일(ex:hosts.txt)에 담긴 호스트 주소나 도메인을 IP 주소로 변환하고 그 값을 화면에 출력한다.
"""
remote_host_ip_list = []

def get_remote_machine_info():
    """
    file_name은 절대 경로를 사용할 수 있다. ex) '/home/python/hosts.txt'
    """
    file = open(file_name, encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        remote_host = line.rstrip('\n')
        try:
            remote_host_ip_list.append(socket.gethostbyname(remote_host))
            #print("Ip address of %s: %s" % (remote_host, socket.gethostbyname(remote_host)))
        except OSError as err:
            print("%s: %s" % (remote_host, err))

"""
get_remote_machine_info에서 얻은 IP 주소를 패킷 바이너리 포맷(ex:7dd1de8e)으로 변환한다.
"""
def convert_ip4_address():
    get_remote_machine_info()
    for ip_addr in remote_host_ip_list:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP Address: %s => Packed: %s, Unpacked: %s" % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

if __name__ == '__main__':
    convert_ip4_address()
