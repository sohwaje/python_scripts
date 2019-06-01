#!/opt/python3/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time, psutil, signal, telegram, string, socket
serverName = 'was1'
title = '[' + serverName + ']\n'
msg = title
sigong_token = '851723999:AAFUkV3XFAHbujWNbbJO2AXr6dr3SKg8AWA'
sigong = '137532606'
bot = telegram.Bot(token = sigong_token)

def send(chat):
    bot.sendMessage(sigong, chat, parse_mode='HTML')

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

        while True:
            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
                    if (pinfo['name'] == 'java' and '-Dserver=instance01' in pinfo['cmdline']):
                        msg += 'Found running cassandra process with pid:' + str(pinfo['pid']) + '%\n'
                        send(msg)
                    else:
                        msg += 'Not Found'
                        pass

if __name__ == '__main__':
        daemon()
