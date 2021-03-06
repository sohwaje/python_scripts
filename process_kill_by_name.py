# -*- coding: utf-8 -*-
# usage : python3.7 process_kill_by_name.py java -Dserver=instance01
"""
프로세스명과 인스턴스명으로 해당 프로세스를 kill한다.
"""
import os
import sys
import psutil

def main():
    """
    # sys.argv는 배열이다. sys.argv[0]은 실행 스크립트 자기 자신이다.
    # 배열의 개수가 2개가 아니면, "usage: 스크립트명 인자"을 출력한다.
    """
    if len(sys.argv) != 3:
        sys.exit('usage: %s process_name, %s instance_name' % __file__)
    else:
        NAME = sys.argv[1]
        INSTANCE = sys.argv[2]

    killed = []  # 리스트를 초기화 한다.
    for proc in psutil.process_iter():
        pinfo = proc.as_dict(attrs=['pid','name','cmdline'])    #as_dict : 여러 프로세스의 attrs 값을 지정하여 사전으로 보여준다.
        if (pinfo['name'] == NAME and INSTANCE in pinfo['cmdline']):  # cmdline의 값(리스트) 안에 INSTANCE가 있으면 참.
            if proc.name() == NAME and proc.pid != os.getpid():
                proc.kill()
                killed.append(proc.pid)
                print("Process name : %s, PID : %s, INSTANCE : %s" % (proc.name(), proc.pid, INSTANCE))
    if not killed:
        sys.exit("%s : %s: no process found" % (NAME, INSTANCE))
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
