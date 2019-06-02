#!/opt/python3/bin/python3
# -*- coding: utf-8 -*-
import telegram, os, socket, string, sys, psutil, daemon
serverName = 'TEST_SERVER'
title = '[' + serverName + ' 서버]\n'
msg = title

#Telegram bot 설정
sigong_token = '851723999:AAFUkV3XFAHbujWNbbJO2AXr6dr3SKg8AWA'
sigong = '137532606'
bot = telegram.Bot(token = sigong_token)

#find_process
process = "java"


def send(chat):
    bot.sendMessage(sigong, chat, parse_mode='HTML')

def checkIfProcessRunning(process):
    listOfProcessObjects = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
            if (pinfo['name'] == 'java' and '-Dserver=instance01' in pinfo['cmdline']):
                listOfProcessObjects.append(pinfo)
                global msg
                msg += 'Found running -Dserver=instance01 with pid:' + str(pinfo['pid']) + '\n'
                send(msg)
        except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
            pass
    return listOfProcessObjects;

checkIfProcessRunning(process)
