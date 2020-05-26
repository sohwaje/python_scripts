"""
프로세스의 PID를 출력한다.
$ python3.7 pidof.py java
1134 4556
"""
from __future__ import print_function
import psutil
import sys

def pidof(pgname):
    pids = []
    for proc in psutil.process_iter(['name','cmdline']):
        # 프로세스 이름과 커맨드 라인에서 일치하는 pid 찾는다.
        if proc.info['name'] == pgname or proc.info['cmdline'][0] == pgname:
            pids.append(str(proc.pid)) # pid를 pids 리스트에 추가한다.
    return pids #pids 리스트를 리턴한다.

def main():
    if len(sys.argv) != 2:  # 인자값의 유효성을 검사하고, 유효하지 않은 경 사용법을 출력한다.
        sys.exit('usage: %s pgname' % __file__)
    else:
        pgname = sys.argv[1] # python pidof.py [프로세스] = pgname
    pids = pidof(pgname)     # pidof함수를 호출한 결과를 pids에 담는다.
    if pids:
        print(" ".join(pids)) # pid 사이에 간격(" ")을 띄운다.

if __name__ == '__main__':
    main()
