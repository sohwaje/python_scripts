import requests
import re
#URL = 'http://www.daum.net'
#resp = requests.get(URL)
#if resp.status_code == requests.codes.ok:
#    html = resp.text
#target = re.compile('http.*://[^"]+')
#result = target.findall(html)
#for k in result:
#    print(k.replace("'",""))


def get(url):
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:
        html = resp.text
    return html

def p(pattern):
    result = re.compile(pattern)
    return result


#URL 입력을 받음
URL = input("input URL> ")
html = get(URL)

#찾을 패턴
pattern = 'http.*://[^"]+'
text = p(pattern)

result = text.findall(html)
sort = sorted(result, key=len)
for k in sort:
    print(k.replace("'",""))
