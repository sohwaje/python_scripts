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
cpuLimit = 0
memLimit = 10
loadAverage = 0
swapUsage = 2
#==============================================================================
serverName = 'was1'
title = '[' + serverName + ' 서버]\n'
msg = title

#Telegram bot 설정
sigong_token = 'YOUR_TOKEN'
sigong = YOUR_ID
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
    return round(psutil.getloadavg()[0])

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

loadAvr = getLoadAverage()
avgCpu = getCpuUsage()
memUsage = getMemUsage()
swap = getSwapUsage()

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
