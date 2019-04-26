import requests
import re

# url의 응답코드가 200ok이면, url을 html이라는 변수에 text로 저장하는 함수
def get(url):
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:
        html = resp.text
    return html

# 패턴 함수
def p(pattern):
    result = re.compile(pattern)
    return result


# URL 입력을 받음
URL = 'http://www.daum.net'
html = get(URL)

# 변수 = 정규식 표현으로 패턴을 만듦
pattern = 'http.*://[^"\']+'
text = p(pattern)

# html에서 패턴과 일치하는 항목을 찾아 result에 저장.
result = text.findall(html)

# url의 길이값(length) 순서로 정렬하여 저장
sort = sorted(result, key=len)

#url에 붙어 있는 "를 제거
for k in sort:
    print(k)
    #print(k.replace("'","")) #정규식 표현에서 "와'를 제거하였으므로 필요 없음.
