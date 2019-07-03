import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests, sys, time, daemon, os, socket, string, sys
from requests.exceptions import Timeout

"""
서버 라벨 설정(서버 또는 호스트의 이름)
"""
serverName = 'service Port'
title = '[' + serverName + ']\n'

"""
Telegram bot의 token value 설정
"""
sigong_token = 'Your_token'
sigong = 'Your Chat ID'
#sigong = '-1001473364013'
bot = telegram.Bot(token = sigong_token)

"""
메시지 전송 설정
"""
def send(chat):
    bot.sendMessage(sigong, chat, parse_mode='HTML')

"""
감시 대상 URL, port
"""
host = ['10.10.10.10','10.10.10.11','10.10.10.12','10.10.10.13','10.10.10.14','10.10.10.15','10.10.10.16','10.10.10.17','10.10.10.18','10.10.10.19']
port = 80

"""
소켓을 생성하고 주어진 host/port로 연결을 연결을 시도한다.
연결에 성공하면 True, 실패하면 False
"""
def Creat_Socket_Connect_Host_Port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5);
        s.connect((host, port))
        return True
    except (socket.gaierror, socket.error, socket.timeout) as e:
        return False

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

    GET_URL_STATUS_CHK()

"""
URL 상태 체크 함수
"""
def GET_URL_STATUS_CHK():
        os.setsid()
        os.open("/dev/null", os.O_RDWR)
        os.dup(0)
        os.dup(0)

        status_of_url1 = True       # 소켓 상태 기본 값 = True
        status_of_url2 = True
        status_of_url3 = True
        status_of_url4 = True
        status_of_url5 = True
        status_of_url6 = True
        status_of_url7 = True
        status_of_url8 = True
        status_of_url9 = True
        status_of_url10 = True

        while True:
            try:
                msg = title
                current_url_1_status = Creat_Socket_Connect_Host_Port(host[0], port)
                if current_url_1_status == True:
                    if status_of_url1 == True:
                        status_of_url1 = False
                        msg += host[0] + ": Jeus Service is available at %d port\r\n" % port
                        send(msg)
                elif current_url_1_status == False:
                    if status_of_url1 == False:
                        status_of_url1 = True
                        msg += host[0] + " Jeus socket timeout at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_2_status = Creat_Socket_Connect_Host_Port(host[1], port)
                if current_url_2_status == True:
                    if status_of_url2 == True:
                        status_of_url2 = False
                        msg += host[1] + ": Jeus Service is available at %d port\r\n" % port
                        send(msg)
                elif current_url_2_status == False:
                    if status_of_url2 == False:
                        status_of_url2 = True
                        msg += host[1] + " Jeus socket timeout at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_3_status = Creat_Socket_Connect_Host_Port(host[2], port)
                if current_url_3_status == True:
                    if status_of_url3 == True:
                        status_of_url3 = False
                        msg += host[2] + ": Jeus Service is available at %d port\r\n" % port
                        send(msg)
                elif current_url_3_status == False:
                    if status_of_url3 == False:
                        status_of_url3 = True
                        msg += host[2] + " Jeus socket timeout at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_4_status = Creat_Socket_Connect_Host_Port(host[3], port)
                if current_url_4_status == True:
                    if status_of_url4 == True:
                        status_of_url4 = False
                        msg += host[3] + ": Jeus Service is available at %d port\r\n" % port
                        send(msg)
                elif current_url_4_status == False:
                    if status_of_url4 == False:
                        status_of_url4 = True
                        msg += host[3] + " Jeus socket timeout at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_5_status = Creat_Socket_Connect_Host_Port(host[4], port)
                if current_url_5_status == True:
                    if status_of_url5 == True:
                        status_of_url5 = False
                        msg += host[4] + ": Jeus Service is available at %d port\r\n" % port
                        send(msg)
                elif current_url_5_status == False:
                    if status_of_url5 == False:
                        status_of_url5 = True
                        msg += host[4] + " Jeus socket timeout at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_6_status = Creat_Socket_Connect_Host_Port(host[5], port)
                if current_url_6_status == True:
                    if status_of_url6 == True:
                        status_of_url6 = False
                        msg += host[5] + ": Jeus Service is available at %d port\r\n" % port
                        send(msg)
                elif current_url_6_status == False:
                    if status_of_url6 == False:
                        status_of_url6 = True
                        msg += host[5] + " Jeus socket timeout at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_7_status = Creat_Socket_Connect_Host_Port(host[6], port)
                if current_url_7_status == True:
                    if status_of_url7 == True:
                        status_of_url7 = False
                        msg += host[6] + ": Jeus Service is available at %d port\r\n" % port
                        send(msg)
                elif current_url_7_status == False:
                    if status_of_url7 == False:
                        status_of_url7 = True
                        msg += host[6] + " Jeus socket timeout at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_8_status = Creat_Socket_Connect_Host_Port(host[7], port)
                if current_url_8_status == True:
                    if status_of_url8 == True:
                        status_of_url8 = False
                        msg += host[7] + ": Jeus Service is available at %d port\r\n" % port
                        send(msg)
                elif current_url_8_status == False:
                    if status_of_url8 == False:
                        status_of_url8 = True
                        msg += host[7] + " Jeus socket timeout at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_9_status = Creat_Socket_Connect_Host_Port(host[8], port)
                if current_url_9_status == True:
                    if status_of_url9 == True:
                        status_of_url9 = False
                        msg += host[8] + ": Jeus Service is available at %d port\r\n" % port
                        send(msg)
                elif current_url_9_status == False:
                    if status_of_url9 == False:
                        status_of_url9 = True
                        msg += host[8] + " Jeus socket timeout at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_10_status = Creat_Socket_Connect_Host_Port(host[9], port)
                if current_url_10_status == True:
                    if status_of_url10 == True:
                        status_of_url10 = False
                        msg += host[9] + ": Jeus Service is available at %d port\r\n" % port
                        send(msg)
                elif current_url_10_status == False:
                    if status_of_url10 == False:
                        status_of_url10 = True
                        msg += host[9] + " Jeus socket timeout at %d port\r\n" % port
                        send(msg)
            except:
                pass

            time.sleep(5)

if __name__ == '__main__':
    daemon()
