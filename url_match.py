import requests
import re
URL = 'http://www.daum.net'
resp = requests.get(URL)
if resp.status_code == requests.codes.ok:
    html = resp.text
target = re.compile('http.*://[^""]+')
result = target.findall(html)
for k in result:
    print(k.replace("'",""))


#def get(url):
#    resp = requests.get(url)
#    if resp.status_code == requests.codes.ok:
#        html = resp.text
#    return html

#def select(string):
#    target = re.compile(string)
#    return target

#테스트 해야 함.
#def url(sort):
#    sorted_string = sorted(sort)
#    sorted_string.reverse()
#    return ''.join(sorted_string)

#URL = input("input URL> ")
#html = get(URL)
#string = 'http.*://[^"]+'
#target = select(string)
#target = re.compile('http.*://[^"]+')
#result = target.findall(html)
#for k in result:
#    print(k.replace("'",""))
