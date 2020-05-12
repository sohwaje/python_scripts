#!/usr/bin/env python3

# Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
A clone of 'netstat -antp' on Linux.
$ python scripts/netstat.py
Proto Local address      Remote address   Status        PID    Program name
tcp   127.0.0.1:48256    127.0.0.1:45884  ESTABLISHED   13646  chrome
tcp   127.0.0.1:47073    127.0.0.1:45884  ESTABLISHED   13646  chrome
tcp   127.0.0.1:47072    127.0.0.1:45884  ESTABLISHED   13646  chrome
tcp   127.0.0.1:45884    -                LISTEN        13651  GoogleTalkPlugi
tcp   127.0.0.1:60948    -                LISTEN        13651  GoogleTalkPlugi
tcp   172.17.42.1:49102  127.0.0.1:19305  CLOSE_WAIT    13651  GoogleTalkPlugi
tcp   172.17.42.1:55797  127.0.0.1:443    CLOSE_WAIT    13651  GoogleTalkPlugi
...
"""
"""
# 라이브러리 설명
psutil.process_iter
- 로컬 시스템 상의 모든 프로세스에 대해서 Process 클래스 인스턴스를 생성하는 반복자를 리턴한다.
- 모든 프로세스 인스턴스는 단 한 번만 생성되고 psutil.process_iter()에 의해 호출될 때(아직 PID가 살아 있다는 가정하에) 캐시된다.
- 또한, PID가 재사용되지 않도록 한다.
- attrs와 ad_value는 Process.as_dict()과 같은 의미다. attrs가 지정되면 Process.as_dict() 결과는
Process 인스턴스들에 첨부된 info 속성으로 저장될 것이다. attrs가 빈 리스트라면 모든 프로세스 정보를 (느리게) 다시 가져올 것이다.
"""
import socket, psutil
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM, AF_INET6



AD = "-"
# AF_INET6 = getattr(socket, 'AF_INET6', object()) # AF_INET6는 상단에 import 시킴
proto_map = {
    (AF_INET, SOCK_STREAM): 'tcp',
    (AF_INET6, SOCK_STREAM): 'tcp6',
    (AF_INET, SOCK_DGRAM): 'udp',
    (AF_INET6, SOCK_DGRAM): 'udp6',
}


def main():
    templ = "%-5s %-30s %-30s %-13s %-6s %s"
    print(templ % (
        "Proto", "Local address", "Remote address", "Status", "PID",
        "Program name"))
    proc_names = {}
    for p in psutil.process_iter(['pid', 'name']):
        proc_names[p.info['pid']] = p.info['name']
        """
        proc_names 딕셔너리에 'pid':'name' 쌍 추가한다.
        ex)
        proc_names={}
        a = 'a'
        b = 'b'
        proc_names['a'] = 'b'
        print(proc_names)
        >>> {'a': 'b'}
        """
    for c in psutil.net_connections(kind='inet'):
        laddr = "%s:%s" % (c.laddr)
        raddr = ""
        if c.raddr:
            raddr = "%s:%s" % (c.raddr)
        print(templ % (
            proto_map[(c.family, c.type)],  # c.family와 c.type값으로 proto_map 변수를 지정한다.
            laddr,
            raddr or AD,
            c.status,
            c.pid or AD,
            proc_names.get(c.pid, '?')[:15],
        ))


if __name__ == '__main__':
    main()
