import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests, sys, time, daemon, os, socket, string, sys
from requests.exceptions import Timeout
from bs4 import BeautifulSoup
from urllib.parse import urljoin


"""
서버 라벨 설정(서버 또는 호스트의 이름)
"""
serverName = 'TEST_SERVER'
title = '[' + serverName + ']\n'

"""
Telegram bot의 token value 설정
"""
my_token = '851723999:AAFUkV3XFAHbujWNbbJO2AXr6dr3SKg8AWA'
my_id = '137532606'

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
# 파싱할 페이지 리스트
"""
http_url_page_list = ['http://websocket.sigongmedia.co.kr:80', 'http://websocket2.sigongmedia.co.kr:80', 'http://www.instance01.com:80']
http_url_page_check_temp = [False, False, False]
http_url_page_check_list = [False, False, False]

"""
데몬 생성 함수
"""
def daemon():
    global http_url_page_check_list
    global http_url_page_check_temp

    try:
        pid = os.fork()
        if pid > 0:
            print('PID: %d' % pid)
            sys.exit()

    except OSError as error:
        print('Unable to fork. Error: %d (%s)' % (error.errno, error.strerror))
        sys.exit()

    while True:
        url_alive_check()
        idx = 0
        message = ""
        for element in http_url_page_list:
            prev = http_url_page_check_list[idx]
            temp = http_url_page_check_temp[idx]
            if ( prev != temp ):
                if temp:
                    message += element + " is UP \r\n"
                else:
                    message += element + " is DOWN \r\n"
            http_url_page_check_list[idx] = http_url_page_check_temp[idx]
            idx = idx + 1

        if len(message) > 0:
            send(message)

        time.sleep(3)


def url_alive_check():
    global http_url_page_check_list
    global http_url_page_check_temp

    idx = 0
    for url_page in http_url_page_list:
        try:
            res = requests.get(url_page, timeout=2)
            if res.status_code == requests.codes.ok:
                http_url_page_check_temp[idx] = True
        except (requests.RequestException, requests.ConnectionError) as e:
            http_url_page_check_temp[idx] = False
        idx = idx + 1

    #print("list -> " + str(http_url_page_check_list[0]) + "/" + str(http_url_page_check_list[1]) + "/" + str(http_url_page_check_list[2]) )
    #print("temp -> " + str(http_url_page_check_temp[0]) + "/" + str(http_url_page_check_temp[1]) + "/" + str(http_url_page_check_temp[2]) )

if __name__ == '__main__':
    daemon()
