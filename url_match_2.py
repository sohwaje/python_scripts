import requests
import re

# url의 응답코드가 200ok이면, url을 html이라는 변수에 text로 저장하는 함수
def get(url):
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:
        html = resp.text
    return html

# 패턴 함수
def pattern(p):
    result = re.compile(p)
    return result

# URL 입력을 받음
#URL = 'http://www.naver.com'
URL = input('URL> ')
html = get(URL)

p = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

text = pattern(p)
# html에서 패턴과 일치하는 항목을 찾아 list 형식으로 result에 저장.
result = text.findall(html)

# url의 길이값(length) 순서로 정렬하여 저장
sort = sorted(result, key=len)

#sort 리스트에서 url을 출력한다.
for url in sort:
    print(url)
