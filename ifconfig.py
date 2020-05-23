"""
stats = psutil.net_if_stats()
1. 시스템에 인스톨된 각 NIC 정보를 사전 형식으로 리턴한다.
예) {'lo0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>,
 speed=0, mtu=16384), 'gif0': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>,
 speed=0, mtu=1280), 'stf0': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>,
 speed=0, mtu=1280), 'bridge0': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>,
 speed=0, mtu=1500)}

io_counters = psutil.net_io_counters(pernic=True)
1. 각 인터페이스의 I/O 통계를 사전 형식으로 리턴한다.
예) {'lo0': snetio(bytes_sent=120899579904, bytes_recv=120899579904, packets_sent=42890571,
packets_recv=42890571, errin=0, errout=0, dropin=0, dropout=0)

net_if_addrs().items()
1. net_if_addrs() 함수는 각 NIC 이름은 Key로, address는 튜플 형식의 Value로 묶은 사전 형식의 자료형 리턴한다.
2. item() 함수는 Key와 Value의 쌍을 튜플로 묶 dic_items 객체로 돌려준다. 리스트처럼 사용가능하다.
예) dict_items([('lo0', [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1',
# netmask='255.0.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 30>,
address='::1', netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', broadcast=None, ptp=None),
snicaddr(family=<AddressFamily.AF_INET6: 30>, address='fe80::1%lo0', netmask='ffff:ffff:ffff:ffff::',
broadcast=None, ptp=None)])
"""

from __future__ import print_function
import socket
import psutil
from psutil._common import bytes2human

af_map = {
    socket.AF_INET: 'IPv4',
    socket.AF_INET6: 'IPv6',
    psutil.AF_LINK: 'MAC',
}

duplex_map = {
    psutil.NIC_DUPLEX_FULL: "full",
    psutil.NIC_DUPLEX_HALF: "half",
    psutil.NIC_DUPLEX_UNKNOWN: "Unknown",
}

def main():
    stats = psutil.net_if_stats()
    io_counters = psutil.net_io_counters(pernic=True)
    for nic, addrs in psutil.net_if_addrs().items():  # key와 value 두개의 인자값을 반복문을 통해 꺼낸다.
        print("%s:" % (nic))                          # nic를 출력한다.
        if nic in stats:                              # stats 안에 nic가 있으면
            st = stats[nic]                           # stats[nic] key에 대응하는 Value를 변수 st에 넣는다.
            # st =  snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1380)
            print("    stats          : ", end='')    # end=''를 지정하여 줄바꿈하지 않는다.
            print("speed=%sMB, duplex=%s, mtu=%s, up=%s" % ( # 즐 바꿈하지 않은 상태에서 각 요소들을 문자열 변수에 담아 출력한다.
                st.speed, duplex_map[st.duplex], st.mtu,     # 위에서 설정한 duplex_map에서 st.duplex에 해당하는 값을 가져온다.
                "yes" if st.isup else "no"                   # isup가 TRUE면 "yes"를 출력하고 그렇지 않으면 "no"를 출력.
            ))
        if nic in io_counters:                          # io_conters에 nic가 있으면, nic에 해당하는 값을 io에 담는다.
            io = io_counters[nic]
            print("    incoming       : ", end='')      # 줄바꿈하지 않은 상태에서 문자열 변수를 담아 출력한다.
            print("bytes=%s, pkts=%s, errs=%s, drops=%s" % (
                bytes2human(io.bytes_recv), io.packets_recv, io.errin,
                io.dropin       # 예) io.bytes_recv => 120899579904
            ))
            print("    outgoing       : ", end='')
            print("bytes=%s, pkts=%s, errs=%s, drops=%s" % (
                bytes2human(io.bytes_sent), io.packets_sent, io.errout,
                io.dropout
            ))
        for addr in addrs:  # addrs 딕셔너리에서 모든 addr 요소를 반복문을 통해 꺼낸다. 예) snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None)
            print("    %-4s" % af_map.get(addr.family, addr.family), end="") # af_map 딕셔너리에서 addr.family의 value를 꺼낸다.
            print(" address   : %s" % addr.address) # 모든 address를 하나씩 출력한다.
            if addr.broadcast:
                print("    broadcast      : %s" % addr.broadcast)   # address가 브로드캐스
            if addr.netmask:
                print("    netmask        : %s" % addr.netmask)    # address가 netmask
            if addr.ptp:
                print("    p2p          : %s" % addr.ptp)           # address가 ptp
        print("")   # 출력되는 nic 정보 아래에 빈 칸을 생성한다.

if __name__ == '__main__':
    main()
