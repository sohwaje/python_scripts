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

process = "java"
instances =['-Dserver=instance01', '-Dserver=instance02']

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
            list_pid_name_cmdline = []
            pid_all = []

            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
                    pid_all.append(pinfo['pid'])
                    list_pid_name_cmdline.append(pinfo)
                    for instance in instances:
                        if (pinfo['name'] == process and instance in pinfo['cmdline']):
                            if pinfo['pid'] not in p_list:
                                msg = title
                                msg += 'process UP: ' + str(instance) + 'pid: ' + str(pinfo['pid']) + '\n'
                                p_list.append(pinfo['pid'])
                                print("추가:",p_list)# 2개 추가(ex: [668422, 670117])
                                send(msg)
                                break
                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

            for pid in p_list:
                try:
                    if pid not in pid_all:
                        p_list.remove(pid)
                        msg = title
                        msg += 'Process DOWN: ' + str(instance) + 'pid : ' + str(pid) + '\n'
                        send(msg)

                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

            time.sleep(3)

if __name__ == '__main__':
        daemon()
