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
m = re.compile('[GE|POS]*T.*(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
for line in lines:
    print(m.findall(line))
