import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests, sys, time, daemon, os, socket, string, sys
from requests.exceptions import Timeout
from bs4 import BeautifulSoup
from urllib.parse import urljoin

"""
서버 라벨 설정(서버 또는 호스트의 이름)
"""
serverName = 'WEBSOCKET'
title = '[' + serverName + ']\n'

"""
Telegram bot의 token value 설정
"""
my_token = 'YOUR_TOKEN'
my_id = 'YOUR_CHATID'

"""
봇에 메시지를 전달하는 설정
"""
bot = telegram.Bot(token = my_token)

"""
메시지 전송 설정
"""
def send(chat):
    bot.sendMessage(my_id, chat, parse_mode='HTML')

"""
감시 대상 URL:port
"""
url_1 = 'http://www.sample1.com:80'
url_2 = 'http://www.sample2.com:80'
url_3 = 'http://www.sample3.com:80'
url_4 = 'http://10.10.10.10:28080'
url_5 = 'http://10.10.10.11:28080'
url_6 = 'http://10.10.10.12:28080'

"""
URL Alive 체크 함수
"""
def GET_URL_ALIVE_CHECK(url):
        try:
            res = requests.get(url, timeout=2)
            if res.status_code == requests.codes.ok:
                return True
        except (requests.RequestException, requests.ConnectionError) as e:
            return False

"""
현재 URL 서비스 상태 저장
"""
current_url_1_status = GET_URL_ALIVE_CHECK(url_1)
current_url_2_status = GET_URL_ALIVE_CHECK(url_2)
current_url_3_status = GET_URL_ALIVE_CHECK(url_3)
current_url_4_status = GET_URL_ALIVE_CHECK(url_4)
current_url_5_status = GET_URL_ALIVE_CHECK(url_5)
current_url_6_status = GET_URL_ALIVE_CHECK(url_6)

"""
포트 지정 변수
"""
port = 80
port_1 = 28080

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

        status_of_url1 = True       # URL 상태 기본 값 = True
        status_of_url2 = True
        status_of_url3 = True
        status_of_url4 = True
        status_of_url5 = True
        status_of_url6 = True


        while True:
            try:
                msg = title
                current_url_1_status = GET_URL_ALIVE_CHECK(url_1)
                if current_url_1_status == True:
                    if status_of_url1 == True:
                        status_of_url1 = False
                        msg += url_1 + " is available at %d port\r\n" % port
                        send(msg)
                elif current_url_1_status == False:
                    if status_of_url1 == False:
                        status_of_url1 = True
                        msg += url_1 + " is not available at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_2_status = GET_URL_ALIVE_CHECK(url_2)
                if current_url_2_status == True:
                    if status_of_url2 == True:
                        status_of_url2 = False
                        msg += url_2 + " is available at %d port\r\n" % port
                        send(msg)
                elif current_url_2_status == False:
                    if status_of_url2 == False:
                        status_of_url2 = True
                        msg += url_2 + " is not available at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_3_status = GET_URL_ALIVE_CHECK(url_3)
                if current_url_3_status == True:
                    if status_of_url3 == True:
                        status_of_url3 = False
                        msg += url_3 + " is available at %d port\r\n" % port
                        send(msg)
                elif current_url_3_status == False:
                    if status_of_url3 == False:
                        status_of_url3 = True
                        msg += url_3 + " is not available at %d port\r\n" % port
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_4_status = GET_URL_ALIVE_CHECK(url_4)
                if current_url_4_status == True:
                    if status_of_url4 == True:
                        status_of_url4 = False
                        msg += url_4 + " is available at %d port\r\n" % port_1
                        send(msg)
                elif current_url_4_status == False:
                    if status_of_url4 == False:
                        status_of_url4 = True
                        msg += url_4 + " is not available at %d port\r\n" % port_1
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_5_status = GET_URL_ALIVE_CHECK(url_5)
                if current_url_5_status == True:
                    if status_of_url5 == True:
                        status_of_url5 = False
                        msg += url_5 + " is available at %d port\r\n" % port_1
                        send(msg)
                elif current_url_5_status == False:
                    if status_of_url5 == False:
                        status_of_url5 = True
                        msg += url_5 + " is not available at %d port\r\n" % port_1
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_6_status = GET_URL_ALIVE_CHECK(url_6)
                if current_url_6_status == True:
                    if status_of_url6 == True:
                        status_of_url6 = False
                        msg += url_6 + " is available at %d port\r\n" % port_1
                        send(msg)
                elif current_url_6_status == False:
                    if status_of_url6 == False:
                        status_of_url6 = True
                        msg += url_6 + " is not available at %d port\r\n" % port_1
                        send(msg)
            except:
                pass
            time.sleep(3)

if __name__ == '__main__':
    daemon()
