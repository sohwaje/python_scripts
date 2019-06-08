import telegram, os, socket, string, sys, psutil, daemon, time
"""
usage : python3.6 server_process_alive_check.py
"""

"""
서버 라벨 설정(서버 또는 호스트의 이름)
"""
serverName = 'TEST_SERVER'
title = '[' + serverName + ']\n'

"""
Telegram bot의 token value 설정
"""
my_token = 'YOUR_TOKEN'
my_id = 'YOUR_TELEGRAM_CHAT_ID'

"""
봇에 메시지를 전달하는 설정
"""
bot = telegram.Bot(token = my_token)

"""
감시 대상 프로세스 및 인스턴스 변수 설정(감시 대상 프로세스 : java, 프로세스의 인스턴스 이름: -Dserver=instnace01)
"""
process = "java"
instances =['-Dserver=instance01', '-Dserver=instance02', '-Dserver=instance03']

"""
메시지 전송 설정
"""
def send(chat):
    bot.sendMessage(my_id, chat, parse_mode='HTML')

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

        process_chk()
"""
프로세스 상태 체크 함수
"""
def process_chk():
        "new session create"
        os.setsid()
        os.open("/dev/null", os.O_RDWR)
        os.dup(0)
        os.dup(0)

        instance_list=[]

        while True:
            instance_all = []       # 모든 인스턴스를 담는다.

            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
                    for instance in instances:
                        if (pinfo['name'] == process and instance in pinfo['cmdline']): # 1st conditional statements
                            instance_all.append(instance)
                            if instance not in instance_list:
                                instance_list.append(instance)
                                msg = title
                                msg += 'process UP: ' + str(instance) + ' pid: ' + str(pinfo['pid']) + '\n'
                                send(msg)
                                break
                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

            for instance in instance_list:
                try:
                    if instance not in instance_all:
                        instance_list.remove(instance)
                        msg = title
                        msg += 'Process DOWN: ' + str(instance) + '\n'
                        send(msg)
                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

            time.sleep(3)

if __name__ == '__main__':
        daemon()
