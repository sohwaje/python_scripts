#!/usr/bin/env python3.7
import requests
from requests.exceptions import Timeout
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

# 정규식 패턴 컴파일 함수
def pattern(x):
    result = re.compile(x)
    return result

# 전체 url 파싱 함수
def get_parsed_url_list():
    URL = input('URL> ')
    html = get(URL)
    p = 'http[s]?://(?:[a-zA-Z]|[0-9][-]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    text = pattern(p)
    result = text.findall(html)
    sort = sorted(result, key=len)
    return sort

# 짧은 url 파싱 함수
def get_parsed_short_url_list():
    URL = input('URL> ')
    html = get(URL)
    p = '(:?http[s]?://[a-z0-9._\-]+)'
    text = pattern(p)
    result = text.findall(html)
    sort = sorted(result, key=len)
    return sort

# 전체 URL을 출력
def full_url():
    sort = get_parsed_url_list()
    for url in sort:
        print(url)

# 짧은 URL을 출력
def short_url():
    sort = get_parsed_short_url_list()
    for url in sort:
        print(url)

# url 응답 시간 측정을 반복문 수행 및 예외 처리 함수 호출
def response_time():
    sort = get_parsed_url_list()
    for respon in sort:
        try_response(respon)

# 예외 처리 수행 및 url 응답 시간 측정
def try_response(respon):
    try:
        rp = requests.get(respon)
        print(rp.elapsed, respon)
    except:
        print("Unexpected error")
        pass

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
        short_url()
    elif choice =="3":
        response_time()
    else:
        End_of_script("Thank you")

# start of script
start()
