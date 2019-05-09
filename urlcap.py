#!/usr/bin/env python3.7
import requests
from requests.exceptions import Timeout
import re
import datetime
import time
import ssl

"""
url requests 코드 200ok -> url을 텍스트 형식으로 html 변수에 저장.
url requests not 200ok -> 현재 url 상태 코드를 출력하고 스크립트 종료.
"""
def get(url):
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:
        html = resp.text
    else:
        print('%s is Check : Response Status :%d' %(url, resp.status_code))
        exit(0)
    return html

"""
추출 할 문자열의 정규식 패턴을 컴파일
"""
def pattern(x):
    return re.compile(x)

"""
사용자가 입력한 URL에서 정규식 패턴에 일치하는 문자열(full url)을 찾아서 result 변수에 담는다.
"""
def get_parsed_full_url_list():
    URL = input('URL> ')
    html = get(URL)
    p = 'http[s]?://(?:[a-zA-Z]|[0-9][-]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    text = pattern(p)
    result = text.findall(html)
    return result

"""
사용자가 입력한 URL에서 정규식 패턴에 일치하는 문자열(short url)을 찾아서 result 변수에 담는다.
"""
def get_parsed_short_url_list():
    URL = input('URL> ')
    html = get(URL)
    p = '(:?http[s]?://[a-z0-9._\-]+)'
    text = pattern(p)
    result = text.findall(html)
    return result

"""
full url 목록에서 가장 짧은 url에서 가장 긴 url 순서로 정렬한 결과를 반환한다.
"""
def sort_full_url_list():
    result = get_parsed_full_url_list()
    sort = sorted(result, key=len)
    return sort

"""
short url 목록에서 가장 짧은 url에서 가장 긴 url 순서로 정렬한 결과를 반환한다.
"""
def sort_short_url_list():
    result = get_parsed_short_url_list()
    sort = sorted(result, key=len)
    return sort

"""
정렬한 full url 목록을 출력한다.
"""
def full_url():
    sort = sort_full_url_list()
    for url in sort:
        print(url)

"""
정렬한 short url 목록을 출력한다.
"""
def short_url():
    sort = sort_short_url_list()
    for url in sort:
        print(url)

"""
full url 목록에서 각 url의 응답 시간(response time)을 측정한다.
"""
def response_time():
    sort = sort_full_url_list()
    for url in sort:
        try_response(url)

"""
url의 응답 시간을 측정하면서 예외가 발생하면 "Unexpected error"를 출력하고 계속 진행한다.
"""
def try_response(url):
    try:
        rp = requests.get(url)
        print(rp.elapsed, url)
    except:
        print("Unexpected error")
        pass

"""
스크립트 종료 함수
"""
def End_of_script(x):
    print(x, "Good Bye")
    exit(0)

"""
스크립트 시작 함수 : 다자택일
"""
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

"""
스크립트 실행
"""
start()
