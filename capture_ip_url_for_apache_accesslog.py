# 아파치 Access_log에서 IP와 URL을 추출한다.
"""사용법
]# python3.7 accesslog.py 아파치엑세스로그파일명
"""
"""
정규식 문자 패턴 분석 : https://regex101.com/r/lIHC9G/1
"""
from sys import argv
import re
script, file_name = argv                        # 스크립트를 실행 할 때 입력 인자 파일(여기서는 아파치 엑세스 로그)을 1개 받는다.

file = open(file_name, 'r')
lines = file.readlines()

#access_log에서 IP와 http[s]를 포함한 URL 경로 추출
m = re.compile('(?:[\d]+[.]\d+[.]\d+[.][\d]+)|(?:\s\/.*?\s)|http[s]?://(?:[a-zA-Z0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
num = 0
for line in lines:
    ip_path = m.findall(line)
    num = num + 1
    print(f"{num}",ip_path)
file.close()

# 정규식 엔진에서 IP만 별도로 추출하거나, GET이나 POST 방식으로 요청된 URL을 출력하고 싶을 때는 아래 스크립트를 이용한다.
#[1] access_log에서 IP만 추출
#for line in lines:
#    m = re.findall('(^\d+[.]+\d+[.]+\d+[.]+[\d])', line)
#    for result in m:
#        print(result)

# r'\bJane\b|\bJanet\b'
#[2] access_log에서 GET 또는 Post 요청 경로만 추출(출력 결과 맨 앞에 GET 또는 POST가 붙는다.)
#m = re.compile('([GET|POST].+)(?:HTTP)')
