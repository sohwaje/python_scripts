import requests
import re
# if 200 ok -> catch a url and save
def get(url):
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:
        html = resp.text
    return html

# pattern def
def pattern(p):
    result = re.compile(p)
    return result

# input a URL
#URL = 'http://www.naver.com'
URL = input('URL> ')
html = get(URL)

p = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
text = pattern(p)
# html에서 패턴과 일치하는 항목을 찾아 list 형식으로 result에 저장.
result = text.findall(html)

# sorted key len
sort = sorted(result, key=len)

#print url in list
for url in sort:
    print(url)
