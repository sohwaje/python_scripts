# 아파치 Access_log에서 IP와 URL을 추출한다.
"""사용법
]# python3.7 accesslog.py 아파치엑세스로그파일명
"""
"""
[1]문자열("([\d]+[.]+\d+[.]+\d+[.]+[\d])")은 IP와 일치를 시도하는 정규식 표현이다.
[2]정규식 엔진은 그 다음 한 번 이상 반복되는 모든 문자열(.+)에 대해 최대 일치를 시도하는 시점에서 비캡쳐 문자열(?:)을 만난다.
[3]그리고 다시 그룹핑된 (.*)에 의해 모든 문자열에 대해서 최대 일치+를 시도하고, 다시 비캡쳐 문자열을 만난다.
*** 비캡쳐 문자열을 만나면 정규식 엔진은 해당 문자열을 캡쳐는 하지만, 출력은 하지 않는다.

**마지막 print(result[0]+result[1])은 출력되는 리스트 자료형[ 'x', 'x1']에서 0번째와 1번째의 문자열을 더해서 출력한다.
이렇게 하는 이유는 리스트 자료형의 구조에서 싱글쿼터와 쉼표를 제외하고 IP와 URL만 출력할 수 있기 때문이다.
"""
from sys import argv
import re
script, file_name = argv                        # 스크립트를 실행 할 때 입력 인자 파일(여기서는 아파치 엑세스 로그)을 1개 받는다.

file = open(file_name, 'r')
lines = file.readlines()

#access_log에서 IP와 URL 경로 추출
m = re.compile('([\d]+[.]+\d+[.]+\d+[.]+[\d]).+(?:GET|POST)(.*?)(?:HTTP)', re.IGNORECASE)
for line in lines:
    ip_path = m.findall(line)
    for result in ip_path:
        print(result[0]+result[1])   #['IP', 'URL']에서 0번째가 IP, 1번째가 URL이 된다.
file.close()

# 정규식 엔진에서 IP만 별도로 추출하거나, GET이나 POST 방식으로 요청된 URL을 출력하고 싶을 때는 아래 스크립트를 이용한다.
#[1] access_log에서 IP만 추출
#for line in lines:
#    m = re.findall('(^\d+[.]+\d+[.]+\d+[.]+[\d])', line)
#    for result in m:
#        print(result)


#[2] access_log에서 GET 또는 Post 요청 경로만 추출(출력 결과 맨 앞에 GET 또는 POST가 붙는다.)
#m = re.compile('([GET|POST].+)(?:HTTP)')
