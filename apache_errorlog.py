#!/usr/bin/env python3.7

# Grap a IP, PATH and URL in Apache Access_log
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
정규식 컴파일
"""
def regular_expression_compile():
    p = '(?:[\d]+[.]\d+[.]\d+[.][\d]+)|(?:\s\/.*?\s)|http[s]?://(?:[a-zA-Z0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    target_expression = re.compile(p)
    return target_expression

"""
FILE_DOES_NOT_EXIST 로그 찾기
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
CLIENT_DENIED_BY_SERVER_CONFIGURATION 로그 찾기
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
스크립트 종료 함수
"""
def End_of_script(x):
    print(x, "Good Bye")
    ERROR_LOG.close()
    exit(0)

"""
스크립트 시작 함수 : 다자택일
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
