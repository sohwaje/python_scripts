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

"""
메세지 송신 함수
"""
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
            process = "java"
            instance = "-Dserver=instance01"

            list_pid_name_cmdline = []
            pid_all = []

            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])          # ex: {'cmdline': ['/usr/sbin/sshd'], 'name': 'sshd', 'pid': 874551} -> print(pinfo['cmdline'], pinfo['name'])
                    pid_all.append(pinfo['pid'])                                    # 모든 pinfo의 모든 pid를 pid_all에 담는다.
                    list_pid_name_cmdline.append(pinfo)                             # pinfo의 모든 요소들이 list_pid_name_cmdline에 담는다. 리스트 안에 딕셔너리 자료형 형태로 저장

                    if (pinfo['name'] == process and instance in pinfo['cmdline']): # pinfo에 담긴 cmdline에 name이 java이고 -Dserver=instance01인 것이 있으면 참이다.
                        if pinfo['pid'] not in p_list:                              # p_list에는 아무 것도 담겨 있지 않으므로 True -> msg 코드 실행
                            # 메세지 전송 코드 블록
                            msg = title
                            msg += 'process UP: ' + str(instance) + 'pid : ' + str(pinfo['pid']) + '\n'
                            p_list.append(pinfo['pid'])                             # 출력한 pid를 p_list에 담는다.
                            send(msg)
                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

            for pid in p_list:
                try:
                    if pid not in pid_all:                                          # pid_all 안에 타겟 pid가 없는가?  -> pid가 있다면 이 구문은 실행되지 않는다.
                        p_list.remove(pid)                                          # 없다면, 타겟 pid를 p_list에서 제거하고 p_list를 비운다.
                        msg = title
                        msg += 'Process DOWN: ' + str(instance) + 'pid : ' + str(pid) + '\n'
                        send(msg)

                except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                    pass

            time.sleep(3)

if __name__ == '__main__':
        daemon()
