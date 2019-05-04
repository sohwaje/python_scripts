# 아파치 Access_log에서 IP와 URL을 추출한다.
"""사용법
]# python3.7 accesslog.py 아파치엑세스로그파일명
"""
"""
정규식 문자 패턴 분석 : https://regex101.com/r/lIHC9G/1
"""
from sys import argv
import re
script, file_name = argv                        # 스크립트를 실행 할 때 입력 파일(여기서는 아파치 엑세스 로그)을 1개 받는다.

file = open(file_name, 'r')
lines = file.readlines()

#access_log에서 IP와 http[s]를 포함한 URL 경로 추출
m = re.compile('(?:^[\d]+[.]\d+[.]\d+[.][\d]+)|(?:\s\/.*?\s)|http[s]?://(?:[a-zA-Z0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
num = 0
for line in lines:
    ip_path = m.findall(line)
    num = num + 1
    print(f"{num}",ip_path)
file.close()
"""
end of script
"""
