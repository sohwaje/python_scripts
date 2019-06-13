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
sigong_token = 'YOUR_TOKEN'
sigong = 'YOUR_CHAT_ID'
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
normal_root_disk = 90
normal_home_disk = 4
normal_loadAverage_first = 3.0
normal_loadAverage_second = 5.0
normal_loadAverage_third = 10.0
normal_swapUsage = 10
normal_cpuLimit_first = 20
normal_cpuLimit_second = 50
normal_cpuLimit_third = 70
normal_cpuLimit_fourth = 80
normal_cpuLimit_fifth = 90
normal_memLimit_first = 60
normal_memLimit_second = 80
normal_memLimit_third = 90

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
        root_alert = True
        load_alert_first = True
        load_alert_second = True
        load_alert_third = True
        cpu_first_alert = True
        cpu_second_alert = True
        cpu_third_alert = True
        cpu_fourth_alert = True
        cpu_fifth_alert = True
        swap_alert = True
        mem_first_alert = True
        mem_second_alert = True
        mem_third_alert = True


        while True:
            msg = title
            try:
                current_home_Disk = getHomedisk()
                if normal_home_disk < current_home_Disk:
                    if home_alert == True:
                        home_alert = False
                        msg += '/home 임계치:  ' + str(normal_home_disk) + '%\n'
                        msg += '[경고] /home 사용량 : ' + str(current_home_Disk) + '%\n'
                        send(msg)
                elif normal_home_disk >= current_home_Disk:
                    if home_alert == False:
                        home_alert = True
                        msg += '[복구] 현재 /home 사용량 : ' + str(current_home_Disk) + '%\n'
                        send(msg)
            except:
                pass

            try:            # / 디스크 경고 block
                current_root_Disk = getRootdisk()
                if normal_root_disk < current_root_Disk:
                    if root_alert == True:
                        root_alert = False
                        msg += ' / 임계치:  ' + str(normal_root_disk) + '%\n'
                        msg += '[경고] / 사용량 : ' + str(current_root_Disk) + '%\n'
                        send(msg)
                elif normal_root_disk >= current_root_Disk:
                    if root_alert == False:
                        root_alert = True
                        msg += '[복구] 현재 / 사용량 : ' + str(current_root_Disk) + '%\n'
                        send(msg)
            except:
                pass

            try:            # first LoadAverage alert block
                current_load_Average = getLoadAverage()
                if normal_loadAverage_first < current_load_Average:
                    if load_alert_first == True:
                        load_alert_first = False
                        msg += 'LoadAverage 임계치:  ' + str(normal_loadAverage_first) + '\n'
                        msg += '[경고] LoadAverage : ' + str(current_load_Average) + '\n'
                        send(msg)
                elif normal_loadAverage_first >= current_load_Average:
                    if load_alert_first == False:
                        load_alert_first = True
                        msg += '[복구] 현재 LoadAverage : ' + str(current_load_Average) + '\n'
                        send(msg)
            except:
                pass

            try:            # second LoadAverage alert block
                current_load_Average = getLoadAverage()
                if normal_loadAverage_second < current_load_Average:
                    if load_alert_second == True:
                        load_alert_second = False
                        msg += 'LoadAverage 임계치:  ' + str(normal_loadAverage_second) + '\n'
                        msg += '[경고] LoadAverage : ' + str(current_load_Average) + '\n'
                        send(msg)
                elif normal_loadAverage_second >= current_load_Average:
                    if load_alert_second == False:
                        load_alert_second = True
            except:
                pass

            try:            # third LoadAverage alert block
                current_load_Average = getLoadAverage()
                if normal_loadAverage_third < current_load_Average:
                    if load_alert_third == True:
                        load_alert_third = False
                        msg += 'LoadAverage 임계치:  ' + str(normal_loadAverage_third) + '\n'
                        msg += '[경고] LoadAverage : ' + str(current_load_Average) + '\n'
                        send(msg)
                elif normal_loadAverage_third >= current_load_Average:
                    if load_alert_third == False:
                        load_alert_third = True
            except:
                pass

            try:            # swap 경고 block
                current_swap_Usage = getSwapUsage()
                if normal_swapUsage < current_swap_Usage:
                    if swap_alert == True:
                        swal_alert = False
                        msg += 'SWAP 임계치:  ' + str(swap_alert_list) + '%\n'
                        msg += '[경고] SWAP 사용량 : ' + str(current_swap_Usage) + '%\n'
                        send(msg)
                elif normal_swapUsage >= current_swap_Usage:
                    if swap_alert == False:
                        swap_alert = True
                        msg += '[복구] 현재 SWAP 사용량 : ' + str(current_swap_Usage) + '%\n'
                        send(msg)
            except:
                pass

            try:            # first CPU 경고 block
                current_cpu_Usage = getCpuUsage()
                if normal_cpuLimit_first < current_cpu_Usage:
                    if cpu_first_alert == True:
                        cpu_first_alert = False
                        msg += 'CPU 임계치:  ' + str(normal_cpuLimit_first) + '%\n'
                        msg += '[경고] CPU 사용량 : ' + str(current_cpu_Usage) + '%\n'
                        send(msg)
                elif normal_cpuLimit_first >= current_cpu_Usage:
                    if cpu_first_alert == False:
                        cpu_first_alert = True
                        msg += '[복구] 현재 CPU 사용량 : ' + str(current_cpu_Usage) + '%\n'
                        send(msg)
            except:
                pass

            try:            # second CPU 경고 block
                current_cpu_Usage = getCpuUsage()
                if normal_cpuLimit_second < current_cpu_Usage:
                    if cpu_second_alert == True:
                        cpu_second_alert = False
                        msg += 'CPU 임계치:  ' + str(normal_cpuLimit_second) + '%\n'
                        msg += '[경고] CPU 사용량 : ' + str(current_cpu_Usage) + '%\n'
                        send(msg)
                elif normal_cpuLimit_second >= current_cpu_Usage:
                    if cpu_second_alert == False:
                        cpu_second_alert = True
            except:
                pass

            try:            # third CPU 경고 block
                current_cpu_Usage = getCpuUsage()
                if normal_cpuLimit_third < current_cpu_Usage:
                    if cpu_third_alert == True:
                        cpu_third_alert = False
                        msg += 'CPU 임계치:  ' + str(normal_cpuLimit_third) + '%\n'
                        msg += '[경고] CPU 사용량 : ' + str(current_cpu_Usage) + '%\n'
                        send(msg)
                elif normal_cpuLimit_third >= current_cpu_Usage:
                    if cpu_third_alert == False:
                        cpu_third_alert = True
            except:
                pass

            try:            # fourth CPU 경고 block
                current_cpu_Usage = getCpuUsage()
                if normal_cpuLimit_fourth < current_cpu_Usage:
                    if cpu_fourth_alert == True:
                        cpu_fourth_alert = False
                        msg += 'CPU 임계치:  ' + str(normal_cpuLimit_fourth) + '%\n'
                        msg += '[경고] CPU 사용량 : ' + str(current_cpu_Usage) + '%\n'
                        send(msg)
                elif normal_cpuLimit_fourth >= current_cpu_Usage:
                    if cpu_fourth_alert == False:
                        cpu_fourth_alert = True
            except:
                pass

            try:            # fifth CPU 경고 block
                current_cpu_Usage = getCpuUsage()
                if normal_cpuLimit_fifth < current_cpu_Usage:
                    if cpu_fifth_alert == True:
                        cpu_fifth_alert = False
                        msg += 'CPU 임계치:  ' + str(normal_cpuLimit_fifth) + '%\n'
                        msg += '[경고] CPU 사용량 : ' + str(current_cpu_Usage) + '%\n'
                        send(msg)
                elif normal_cpuLimit_fifth >= current_cpu_Usage:
                    if cpu_fifth_alert == False:
                        cpu_fifth_alert = True
            except:
                pass

            try:            # first memory rate alert block
                current_mem_Usage = getMemUsage()
                if normal_memLimit_first < current_mem_Usage:
                    if mem_first_alert == True:
                        mem_first_alert = False
                        msg += 'Memory 임계치:  ' + str(normal_memLimit_first) + '%\n'
                        msg += '[경고] Memory 사용량 : ' + str(current_mem_Usage) + '%\n'
                        send(msg)
                elif normal_memLimit_first >= current_mem_Usage:
                    if mem_first_alert == False:
                        mem_first_alert = True
                        msg += '[복구] 현재 Memory 사용량 : ' + str(current_mem_Usage) + '%\n'
                        send(msg)
            except:
                pass

            try:            # second memory rate alert block
                current_mem_Usage = getMemUsage()
                if normal_memLimit_second < current_mem_Usage:
                    if mem_second_alert == True:
                        mem_second_alert = False
                        msg += 'Memory 임계치:  ' + str(normal_memLimit_second) + '%\n'
                        msg += '[경고] Memory 사용량 : ' + str(current_mem_Usage) + '%\n'
                        send(msg)
                elif normal_memLimit_second >= current_mem_Usage:
                    if mem_second_alert == False:
                        mem_second_alert = True
            except:
                pass

            try:            # third memory rate alert block
                current_mem_Usage = getMemUsage()
                if normal_memLimit_third < current_mem_Usage:
                    if mem_third_alert == True:
                        mem_third_alert = False
                        msg += 'Memory 임계치:  ' + str(normal_memLimit_third) + '%\n'
                        msg += '[경고] Memory 사용량 : ' + str(current_mem_Usage) + '%\n'
                        send(msg)
                elif normal_memLimit_third >= current_mem_Usage:
                    if mem_third_alert == False:
                        mem_third_alert = True
            except:
                pass

            time.sleep(3)

if __name__ == '__main__':
        daemon()
