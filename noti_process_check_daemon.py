#!/opt/python3/bin/python3
# -*- coding: utf-8 -*-
import telegram, os, socket, string, sys, psutil, daemon, time
"""
서버 라벨 설정
"""
serverName = 'TEST_SERVER'
title = '[' + serverName + ' 서버]\n'

"""
Telegram bot 설정
"""
sigong_token = '851723999:AAFUkV3XFAHbujWNbbJO2AXr6dr3SKg8AWA'
sigong = '137532606'
bot = telegram.Bot(token = sigong_token)

"""
메세지 송신 함수
"""
def send(chat):
    bot.sendMessage(sigong, chat, parse_mode='HTML')

"""
데몬 생성 함수
"""
def daemon():
        try:
            pid = os.fork()

            if pid > 0:
                print('PID: %d' % pid)
                sys.exit()

        except OSError as error:
            print('Unable to fork. Error: %d (%s)' % (error.errno, error.strerror))
            sys.exit()

        doTask()

def doTask():
        "new session create"
        os.setsid()

        os.open("/dev/null", os.O_RDWR)
        os.dup(0)
        os.dup(0)

        p_list=[]

        while True:
            list_pid_name_cmdline = []                                     # pid, name, cmdline 요소를 담을 빈 list 생성
            pid_all = []                                                   # 오직 pid만 담겨 있는 빈 list 생성
            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])  # ex: {'cmdline': ['/usr/sbin/sshd'], 'name': 'sshd', 'pid': 874551} -> print(pinfo['cmdline'], pinfo['name'])
                    if (pinfo['name'] == process and '-Dserver=instance01' in pinfo['cmdline']): # pinfo에 담긴 cmdline에 name이 java이고 -Dserver=instance01인 것이 있으면 참이다.
                        pid_all.append(pinfo['pid'])                        # pid_all에 pid를 담는다.
                        if pinfo['pid'] not in p_list:                      # p_list에 타겟 pid가 없는가?
                            list_pid_name_cmdline.append(pinfo)             # pid, name, cmdline 요소를 list_pid_name_cmdline 담는다.
                            msg = title
                            msg += 'Found running -Dserver=instance01 with pid:' + str(pinfo['pid']) + '\n'
                            p_list.append(pinfo['pid'])
                            send(msg)

                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

            for pid in p_list:
                try:
                    if pid not in pid_all:                                     # pid_all 안에 타겟 pid가 없는가?
                        p_list.remove(pid)                                     # 없다면, 타겟 pid를 p_list에서 제거한다.
                        msg = title
                        msg += 'Process Removed / pid:' + str(pid) + '\n'
                        send(msg)

                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

            time.sleep(3)

if __name__ == '__main__':
        daemon()
