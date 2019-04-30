# 아파치 Access_log에서 IP를 추출한다.
# 아파치 Access_log에서 GET과 POST 방식으로 요청된 경로를 추출한다.
from sys import argv
import re
script, file_name = argv

file = open(file_name, 'r')
lines = file.readlines()
#[1] access_log에서 IP 추출
#for line in lines:
#    m = re.findall('[0-9]+[.]+[0-9]+[.]+[0-9]+[.]+[0-9]+', line) # 리스트 형식['IP']으로 저장
#    for result in m:                                             # 리스트에서 IP만 추출
#        print(result)
#file.close()

#[2] access_log에서 GET 또는 Post 경로 추출
m = re.compile('([GET|POST].+)(?:HTTP)')
for line in lines:
    path = m.findall(line)
    for result in path:
        print(result)
"""
정규식 엔진은 []안의 문자열 "GET"과 "POST"의 일치를 시도한다.
그 뒤의 문자(".")가 하나 이상 일치하므로 +는 최대 일치를 시도한다.
정규식 엔진이 최대 일치를 끝낸 시점에서 (?:HTTP) 즉, HTTP가 들어간 그룹은 출력에서 제외한다.
"""
