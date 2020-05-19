# -*- coding: utf-8 -*-
# # usage : python3.7 killall_process_by_name.py java
import os
import sys
import psutil

def main():
    """
    # sys.argv는 배열이다. sys.argv[0]은 실행 스크립트 자기 자신이다.
    # 배열의 개수가 2개가 아니면, "usage: 스크립트명 인자"을 출력한다.
    """
    if len(sys.argv) != 2:
        sys.exit('usage: %s name' % __file__)
    else:
        NAME = sys.argv[1]
        # NAME 변수에는 sys.argv[1] 즉, 프로세스 이름이 인자값으로 들어간다.

    killed = []  # 리스트를 초기화 한다.
    # 실행중인 프로세스의 정보(name, pid, username)을 가져온다.
    for proc in psutil.process_iter():
        if proc.name() == NAME and proc.pid != os.getpid():
            print("Process name : %s, PID : %s " % (proc.name(), proc.pid))
            # 프로세스 이름(proc.name)이 인자값 NAME과 같고, 그 프로세스의 pid가 현재 pid(os.getpid())과 다르면 proc.kill()이 동작한다.
            proc.kill()
            killed.append(proc.pid)
            # kill시킨 pid를 리스트에 추가한다.
            # print(killed)
    if not killed:
        # killed 리스트에 없으면, 아래를 출력하고 스크립트를 종료한다.
        sys.exit('%s: no process found' % NAME)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
