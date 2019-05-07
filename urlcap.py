#!/usr/bin/env python3.7
import requests
import re
import datetime
import time
import ssl

# 사이트 유효성 검사 및 사이트 내용 저장
def get(url):
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:       # if 200 ok -> catch a url and save function
        html = resp.text
    else:
        print('%s is Check : Response Status :%d' %(url, resp.status_code))
        exit(0)
    return html

# pattern 정규식 컴파일 함수
def pattern(x):
    result = re.compile(x)
    return result

# full url function (URL 전체를 출력)
def full_url():
    URL = input('URL> ')
    html = get(URL)
    p = 'http[s]?://(?:[a-zA-Z]|[0-9][-]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'    # FULL URL 캡쳐 정규식
    text = pattern(p)
    result = text.findall(html)
    sort = sorted(result, key=len)
    for url in sort:
        print(url)

# only www function (WWW URL 출력)
def only_www():
    URL = input('URL> ')
    html = get(URL)
    p_1 = '(:?http[s]?://[a-z0-9._\-]+)'                                                        # WWW URL 캡쳐 정규식
    text = pattern(p_1)
    result = text.findall(html)
    sort = sorted(result, key=len)
    for www in sort:
        print(www)

def respones_time():
    URL = input('URL> ')
    html = get(URL)
    p = 'http[s]?://(?:[a-zA-Z]|[0-9][-]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'    # FULL URL 캡쳐 정규식
    text = pattern(p)
    result = text.findall(html)
    sort = sorted(result, key=len)
    for respon in result:
        rp = requests.get(respon)
        print(rp.elapsed, respon)

# exit function
def End_of_script(x):
    print(x, "Good Bye")
    exit(0)

# start function
def start():
    print("Capture full url     : 1,  ex)http://www.abc.com/abc/&879/778_ga.gif")
    print("Capture short url    : 2,  ex)http://www.abc.com")
    print("Capture url and response time : 3 ")

    choice = input("> ")

    if choice == "1":
        full_url()
    elif choice == "2":
        only_www()
    elif choice =="3":
        respones_time()
    else:
        End_of_script("Thank you")

# start of script
start()
