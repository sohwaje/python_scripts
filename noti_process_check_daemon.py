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
감시 대상 프로세스
"""
process = "java"

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
            listOfProcessObjects = []
            p_all = []
            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
                    if (pinfo['name'] == 'java' and '-Dserver=instance01' in pinfo['cmdline']):
                        p_all.append(pinfo['pid'])
                        if pinfo['pid'] not in p_list:
                            listOfProcessObjects.append(pinfo)
                            msg = title
                            msg += 'Found running -Dserver=instance01 with pid:' + str(pinfo['pid']) + '\n'
                            p_list.append(pinfo['pid'])
                            send(msg)

                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

            for pid in p_list:
                try:
                    if pid not in p_all:
                        p_list.remove(pid)
                        msg = title
                        msg += 'Process Removed / pid:' + str(pid) + '\n'
                        send(msg)

                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

            time.sleep(3)

if __name__ == '__main__':
        daemon()
