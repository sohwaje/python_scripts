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
리소스 임계치 설정
"""
normal_cpuLimit = 20
normal_memLimit = 90
normal_loadAverage = 3.0
normal_swapUsage = 10
normal_root_disk = 90
normal_home_disk = 90


serverName = 'TEST'
title = '[' + serverName + ' 서버]\n'


# Telegram bot 설정
sigong_token = '851723999:AAFUkV3XFAHbujWNbbJO2AXr6dr3SKg8AWA'
sigong = '137532606'
bot = telegram.Bot(token = sigong_token)

"""
텔레그램 메세지 전송
"""
def send(chat):
        bot.sendMessage(sigong, chat, parse_mode='HTML')

"""
리소스 사용량 체크
"""
def getLoadAverage():
    return psutil.getloadavg()[0]

def getCpuUsage():
    cpu = 0
    for x in range(2):
        cpu += psutil.cpu_percent(interval=1)
        return round(float(cpu)/3,2)

def getHomedisk():
    return round(psutil.disk_usage('/home')[3])

def getSwapUsage():
    return round(psutil.swap_memory()[3])

def getMemUsage():
    return round(psutil.virtual_memory()[2])

def getRootdisk():
    return psutil.disk_usage('/')[3]

def getHomedisk():
    return round(psutil.disk_usage('/home')[3])

"""
현재 사용량
"""
current_load_Average = getLoadAverage()
current_cpu_Usage = getCpuUsage()
current_swap_Usage = getSwapUsage()
current_mem_Usage = getMemUsage()
current_root_Disk = getRootdisk()
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
리소스 사용량 alert 설정
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
                        msg += '[경고] /home 사용량 : ' + str(current_home_Disk) + '%\n'
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
