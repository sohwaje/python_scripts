import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests, sys, time, daemon, os, socket, string, sys
import json, urllib.request, urllib.parse
from requests.exceptions import Timeout
from urllib.parse import urljoin
from urllib.error import URLError, HTTPError, ContentTooShortError
"""
서버 라벨 설정(서버 또는 호스트의 이름)
"""
serverName = 'TEST 서버'
title = '[' + serverName + ']\n'

"""
Telegram bot의 token value 설정
"""
my_token = 'TOKEN'
my_id = 'CHAT_ID'

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
url_1 = "http://www.example.com/GetLatestVersion.json"
url_2 = "http://upload.example.com/GetLatestVersion.json"

"""
json 구조를 dictionary 자료형으로 변환하는 함수
"""
#def json_to_dictionary(url):
#    try:
#        text_data = urllib.request.urlopen(url).read().decode('utf-8')
#        dict_ = json.loads(text_data)
#    except (URLError, HTTPError, ContentTooShortError) as e:
#        dict_ = False
#    return dict_

def json_to_dictionary(url, num_retries=3):     #예외 발생시 3번 재시도
    try:
        text_data = urllib.request.urlopen(url).read().decode('utf-8')
        dict_ = json.loads(text_data)
    except (URLError, HTTPError, ContentTooShortError) as e:
        dict_ = None
        if num_retries > 0:                     #예외 발생시 3번 재시도
            return json_to_dictionary(url, num_retries - 1)
    return dict_
"""
변환된 dictionary 자료형에서 특정 자료형에 해당하는 값이 'OK'인지 검증하는 함수
여기서 'result', 'code', 'OK'는 예제이다. 실제 json 코드는 개발한 페이지마다 다르다.
json 페이지를 파싱하면 {"result":{"msg":"최신버전입니다.","code":"OK"}} 이런 결과 값이 나온다는 가정을 전제한 것.
"""
def url_status_chk(url):
    try:
        result = json_to_dictionary(url)
        if result['result']['code'] == 'OK':
            return True
    except:
        return False

"""
현재 URL 서비스 상태 저장
"""
current_url_1_status = url_status_chk(url_1)
current_url_2_status = url_status_chk(url_2)

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


def GET_URL_STATUS_CHK():
        os.setsid()
        os.open("/dev/null", os.O_RDWR)
        os.dup(0)
        os.dup(0)

        status_of_url1 = True       # URL 상태 기본 값 = True
        status_of_url2 = True

        while True:
            try:
                msg = title
                current_url_1_status = url_status_chk(url_1)
                print(current_url_1_status)
                if current_url_1_status == True:
                    if status_of_url1 == True:
                        status_of_url1 = False
                        msg += url_1 + " 텔레그램 봇이 전달할 텍스트 메시지.\r\n"
                        send(msg)
                elif current_url_1_status == False:
                    if status_of_url1 == False:
                        status_of_url1 = True
                        msg += url_1 + " [치명]텔레그램 봇이 전달할 텍스트 메시지.\r\n"
                        send(msg)
            except:
                pass

            try:
                msg = title
                current_url_2_status = url_status_chk(url_2)
                if current_url_2_status == True:
                    if status_of_url2 == True:
                        status_of_url2 = False
                        msg += url_2 + " 텔레그램 봇이 전달할 텍스트 메시지.\r\n"
                        send(msg)
                elif current_url_2_status == False:
                    if status_of_url2 == False:
                        status_of_url2 = True
                        msg += url_2 + " [치명]텔레그램 봇이 전달할 텍스트 메시지.\r\n"
                        send(msg)
            except:
                pass
            time.sleep(3)

if __name__ == '__main__':
    daemon()
