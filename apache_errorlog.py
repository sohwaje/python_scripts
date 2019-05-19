#!/usr/bin/env python3.7

# 아파치 에러로그의 특정 에러 메시지가 포함된 문자열을 IP와 URL 또는 Path로 구분하여 출력한다.
"""usage
]> python3.7 script_name apache_error.log
"""
"""
start of script
"""
from sys import argv
import re

script, file_name = argv

ERROR_LOG = open(file_name, 'r')

"""
찾을 문자열 패턴을 컴파일
"""
def regular_expression_compile():
    p = '(?:[\d]+[.]\d+[.]\d+[.][\d]+)|(?:\s\/.*?\s)|http[s]?://(?:[a-zA-Z0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    target_expression = re.compile(p)
    return target_expression

"""
[1]FILE_DOES_NOT_EXIST 로그 찾기
"""
def FILE_DOES_NOT_EXIST():
    num = 0
    for line in ERROR_LOG.readlines():
        if line.find("File does not exist") > 0:
            target = regular_expression_compile()
            ip_path = target.findall(line)
            num = num + 1
            for result in ip_path:
                print(f"{num}", "IP:",ip_path[0],"PATH:",ip_path[1],"URL:",ip_path[-1])
        else:
            pass

"""
[2]CLIENT_DENIED_BY_SERVER_CONFIGURATION 로그 찾기
"""
def CLIENT_DENIED_BY_SERVER_CONFIGURATION():
    num = 0
    for line in ERROR_LOG.readlines():
        if line.find("client denied by server configuration") > 0:
            target = regular_expression_compile()
            ip_path = target.findall(line)
            num = num + 1
            print(f"{num}", "IP:",ip_path[0], "URL or PATH:",ip_path[1])
        else:
            pass


"""
스크립트 종료
"""
def End_of_script(x):
    print(x, "Good Bye")
    ERROR_LOG.close()
    exit(0)

"""
스크립트 시작
"""
def start():
    print("FILE_DOES_NOT_EXIST                    : 1")
    print("CLIENT_DENIED_BY_SERVER_CONFIGURATION  : 2")

    choice = input("> ")

    if choice == "1":
        FILE_DOES_NOT_EXIST()
    elif choice == "2":
        CLIENT_DENIED_BY_SERVER_CONFIGURATION()
    else:
        End_of_script("Thank you")

"""
스크립트 실행
"""
start()
