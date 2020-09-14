import telegram, os, string, sys, psutil, daemon, time
import logging

mylogger = logging.getLogger("python-daemon")
mylogger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('/var/log/python2.log')
file_handler.setFormatter(formatter)
mylogger.addHandler(file_handler)
"""
서버 라벨 설정
"""
serverName = '222.231.26.208'
title = '[' + serverName + ']\n'

"""
Telegram bot 설정
"""
sigong_token = '851723999:AAFUkV3XFAHbujWNbbJO2AXr6dr3SKg8AWA'
sigong = '-1001473364013'
bot = telegram.Bot(token = sigong_token)

"""
감시 대상 프로세스 및 인스턴스
"""
process = "java"
instances =['-Dtkbell', '-Daspen', '-Dthce']

"""
메시지 전송 설정
"""
def send(chat):
    try:
        bot.sendMessage(sigong, chat, parse_mode='HTML')
    except BadRequest as e:
        bot.sendMessage(sigong, chat, parse_mode='HTML')
    except RetryAfter as e:
        sleep(240)
        bot.sendMessage(sigong, chat, parse_mode='HTML')
    except TimedOut as e:
        sleep(60)
        bot.sendMessage(sigong, chat, parse_mode='HTML')
    except Unauthorized as e:
        sleep(0.25)
        bot.sendMessage(sigong, chat, parse_mode='HTML')
    except NetworkError as e:
        sleep(30)
        bot.sendMessage(sigong, chat, parse_mode='HTML')
    except Exception as e:
        sleep(1)
        bot.sendMessage(sigong, chat, parse_mode='HTML')


"""
데몬 생성 함수
"""
def daemon():
        try:
            pid = os.fork()
            if pid > 0:
                print('PID: %d' % pid)
                mylogger.info("=========PID=========")
                mylogger.info(pid)
                mylogger.info("=====================")
                sys.exit(0)

        except OSError as error:
            print('Unable to fork. Error: %d (%s)' % (error.errno, error.strerror))
            mylogger.info("=========OSError=========")
            mylogger.info("error:" + error)
            mylogger.info("=======OSError END=======")
            sys.exit(1)

        process_chk()
        mylogger.info("process_chk:" + process_chk())
"""
프로세스 상태 체크 함수
"""
def process_chk():
#        mylogger.info("new session create")
        os.setsid()

        os.open("/dev/null", os.O_RDWR)
        os.dup(0)
        os.dup(0)

        instance_list=[]
        try:
            while True:
                instance_all = []       # 모든 인스턴스를 담는다.

                for proc in psutil.process_iter():
                    try:
                        pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
                        for instance in instances:
                            if (pinfo['name'] == process and instance in pinfo['cmdline']):
                                instance_all.append(instance)
                                if instance not in instance_list:
                                    instance_list.append(instance)
                                    msg = title
                                    msg += 'process UP: ' + str(instance) + ' pid: ' + str(pinfo['pid']) + '\n'
                                    send(msg)
                                    mylogger.info("======UP instance====")
                                    mylogger.info("instance:" + instance)
                                    mylogger.info("=====================")
                                    break

                    except (psutil.Error, psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess, psutil.TimeoutExpired) as e:
                        mylogger.exception("mgs1 = "+ msg +" errorLog " + e)

                for instance in instance_list:
                    try:
                        if instance not in instance_all:
                            instance_list.remove(instance)
                            msg = title
                            msg += 'Process DOWN: ' + str(instance) + '\n'
                            send(msg)
                            mylogger.warning("=====================")
                            mylogger.warning("====Down process=====")
                            mylogger.warning("instance:" + instance)
                            mylogger.warning("=====================")

                    except (psutil.Error, psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess, psutil.TimeoutExpired) as e:
                        mylogger.exception("mgs2 = "+ msg +" errorLog " + e)


                time.sleep(3)
        except Exception as e:
            mylogger.exception(e)
if __name__ == '__main__':
    daemon()
