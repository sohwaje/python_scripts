#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telegram
import os
import socket
import string
import sys
import psutil
import time


"""
임계치 설정
"""
normal_home_disk = 4
#==============================================================================
serverName = 'TEST'
title = '[' + serverName + ' 서버]\n'

#Telegram bot 설정
sigong_token = '851723999:AAFUkV3XFAHbujWNbbJO2AXr6dr3SKg8AWA'
sigong = '137532606'
bot = telegram.Bot(token = sigong_token)

"""
텔레그램 메세지 전송
"""
def send(chat):
        bot.sendMessage(sigong, chat, parse_mode='HTML')

"""
/home 디스크 사용량
"""
def getHomedisk():
    return round(psutil.disk_usage('/home')[3])

"""
#현재 사용량
"""
current_home_Disk = getHomedisk()

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

        sys_chk()
"""
시스템 상태 체크
"""
def sys_chk():
        "new session create"
        os.setsid()
        os.open("/dev/null", os.O_RDWR)
        os.dup(0)
        os.dup(0)
        home_alert_list = [0]

        while True:
            msg = title
            try:
                current_home_Disk = getHomedisk()
                if normal_home_disk < current_home_Disk:
                    if 1 not in home_alert_list:
                        home_alert_list.remove(0)
                        home_alert_list.append(1)
                        msg += '/home 임계치:  ' + str(normal_home_disk) + '%\n'
                        msg += '/home 사용량 : ' + str(current_home_Disk) + '%\n'
                        send(msg)
            except:
                pass

            try:
                if normal_home_disk >= current_home_Disk:
                    if 0 not in home_alert_list:
                        home_alert_list.remove(1)
                        home_alert_list.append(0)
                        msg += '[복구] 현재 /home 사용량 : ' + str(current_home_Disk) + '%\n'
                        send(msg)
            except:
                pass
            time.sleep(3)

if __name__ == '__main__':
        daemon()
