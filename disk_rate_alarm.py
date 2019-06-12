#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telegram, os, socket, string, sys, psutil, time

"""
[1]감시 대상 서버 라벨 설정
"""
serverName = 'TEST'
title = '[' + serverName + ' 서버]\n'

"""
[2]Telegram bot token value
"""
sigong_token = '851723999:AAFUkV3XFAHbujWNbbJO2AXr6dr3SKg8AWA'
sigong = '137532606'
bot = telegram.Bot(token = sigong_token)

"""
[3]텔레그램 메세지 전송
"""
def send(chat):
        bot.sendMessage(sigong, chat, parse_mode='HTML')

"""
[4]리소스 사용량 체크
"""
def getLoadAverage():                               # LoadAverage 측정
    return psutil.getloadavg()[0]

def getCpuUsage():                                  # CPU 사용률 측정
    cpu = 0
    for x in range(4):
        cpu = psutil.cpu_percent(interval=1, percpu=False)
        return cpu

def getSwapUsage():                                 # swap 메모리 측정
    return round(psutil.swap_memory()[3])

def getMemUsage():                                  # 메모리 사용률 측정
    return round(psutil.virtual_memory()[2])

def getRootdisk():                                  # 최상위 디렉토리(/) 사용량 측정
    return psutil.disk_usage('/')[3]

def getHomedisk():                                  # home 디렉토리 사용량 측정
    return round(psutil.disk_usage('/home')[3])

"""
[5]각 함수를 호출하여 현재 리소스 사용량을 가져온다.
"""
current_load_Average = getLoadAverage()
current_cpu_Usage = getCpuUsage()
current_swap_Usage = getSwapUsage()
current_mem_Usage = getMemUsage()
current_root_Disk = getRootdisk()
current_home_Disk = getHomedisk()

"""
[6]리소스 임계치
"""
normal_loadAverage = 3.0
normal_cpuLimit_first = 20
normal_cpuLimit_second = 50
normal_cpuLimit_third = 70
normal_cpuLimit_fourth = 80
normal_cpuLimit_fifth = 90
normal_swapUsage = 10
normal_memLimit = 90
normal_root_disk = 90
normal_home_disk = 4

"""
[7]데몬 생성 함수
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
[8]리소스 사용량이 정의된 임계치보다 높으면 "[경고]" 메시지를 전송하고, 임계치 이하면 "[복구]" 메시지를 전송한다.
"""
def sys_chk():
        "new session create"
        os.setsid()
        os.open("/dev/null", os.O_RDWR)
        os.dup(0)
        os.dup(0)

        home_alert = True

        while True:
            msg = title
            try:            # home disk 경고 block
                current_home_Disk = getHomedisk()
                if normal_home_disk < current_home_Disk:
                    if home_alert == True:
                        home_alert = False
                        msg += '/home 임계치:  ' + str(normal_home_disk) + '%\n'
                        msg += '[경고] /home 사용량 : ' + str(current_home_Disk) + '%\n'
                        send(msg)
            except:
                pass

            try:            # home disk 복구 block
                if normal_home_disk >= current_home_Disk:
                    if home_alert == False:
                        home_alert = True
                        msg += '[복구] 현재 /home 사용량 : ' + str(current_home_Disk) + '%\n'
                        send(msg)
            except:
                pass


            time.sleep(3)

if __name__ == '__main__':
        daemon()
