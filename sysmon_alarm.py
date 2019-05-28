#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telegram
import os
import socket
import string
import sys
import psutil


"""
임계치 설정
"""
cpuLimit = 20
memLimit = 90
loadAverage = 3.0
swapUsage = 10
root_disk = 90
home_disk = 90
#==============================================================================
serverName = 'sigong_messenger_was1(26.145)'
title = '[' + serverName + ' 서버]\n'
msg = title

#Telegram bot 설정
sigong_token = '851723999:AAFUkV3XFAHbujWNbbJO2AXr6dr3SKg8AWA'
sigong = '-1001374734756'
bot = telegram.Bot(token = sigong_token)

"""
텔레그램 메세지 전송
"""
def send(chat):
        bot.sendMessage(sigong, chat, parse_mode='HTML')
"""
LoadAverage
"""
def getLoadAverage():
    return psutil.getloadavg()[0]

"""
cpu 사용률
"""
def getCpuUsage():
    cpu = 0
    for x in range(2):
        cpu += psutil.cpu_percent(interval=1)
        return round(float(cpu)/3,2)

"""
swap 메모리 사용량
"""
def getSwapUsage():
    return round(psutil.swap_memory()[3])
"""
Memory 사용량
"""
def getMemUsage():
    return round(psutil.virtual_memory()[2])

"""
루트 디스크(/) 사용량
"""
def getRootdisk():
    return psutil.disk_usage('/')[3]

"""
/home 디스크 사용량
"""
def getHomedisk():
    return round(psutil.disk_usage('/home')[3])

"""
현재 사용량
"""
loadAvr = getLoadAverage()
avgCpu = getCpuUsage()
memUsage = getMemUsage()
swap = getSwapUsage()
root_Disk = getRootdisk()
home_Disk = getHomedisk()

if loadAvr > loadAverage:
        msg += 'LoadAverage(' + str(loadAverage) + ') 초과\n'
        msg += '현재 LoadAverage : ' + str(loadAvr) + '\n'
        send(msg)

if avgCpu > cpuLimit:
        msg += 'cpu 사용량이 기준값(' + str(cpuLimit) + '%) 초과\n'
        msg += 'cpu usage : ' + str(avgCpu) + '%\n'
        send(msg)

if memUsage > memLimit:
        msg += 'memory 사용량이 기준값(' + str(memLimit) + '%) 초과\n'
        msg += 'memory usage : ' + str(memUsage) + '%\n'
        send(msg)

if swap > swapUsage:
        msg += 'swap 메모리 사용량 기준값(' + str(swapUsage) + '%) 초과\n'
        msg += 'swap 메모리 사용량 : ' + str(swap) + '%\n'
        send(msg)

if root_Disk > root_disk:
        msg += '디스크(/) 사용량 기준값(' + str(root_disk) + '%) 초과\n'
        msg += '현재 루트 디스크 사용량 : ' + str(root_Disk) + '%\n'
        send(msg)

if home_Disk > home_disk:
        msg += '디스크(/home) 사용량 기준값(' + str(home_disk) + '%) 초과\n'
        msg += '현재 (/home) 디스크 사용량 : ' + str(home_Disk) + '%\n'
        send(msg)
