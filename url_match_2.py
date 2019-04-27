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
URL = 'http://www.naver.com'
#URL = input('URL> ')
html = get(URL)

#[s]? = ?앞에 있는 문자 s가 있거나 없거나 모두 매치된다.
# | = "or"의 의미와 동일하다. A|B는 A또는 B이다. "|"을 findall 함수와 같이 쓰면 A와B를 모두 찾는다.
# +, * = 반복을 나타내는 메타문자. *은 0번 반복해도 참, +는 최소 1번 반복해야 참.
# . = 모든 문자와 매치된다.
# ^ 또는 $ 문자를 메타문자가 아닌 문자 그 자체로 매치하고 싶은 경우에는 [^], [$] 처럼 사용하거나 \^, \$ 로 사용
p = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

text = pattern(p)
# html에서 패턴과 일치하는 항목을 찾아 list 형식으로 result에 저장.
result = text.findall(html)

# url의 길이값(length) 순서로 정렬하여 저장
sort = sorted(result, key=len)

#sort 리스트에서 url을 출력한다.
for url in sort:
    print(url)
    #print(k.replace("'","")) #정규식 표현에서 "와'를 제거하였으므로 필요 없음.
