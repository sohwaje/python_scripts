#www.daum.net에서 http, https 링크를 추출하여 가장 긴 url 길이 순서로 정렬하고, 그 중에서 상위 10개의 url의 응답시간을 출력
import requests
URL = 'http://www.daum.net'
resp = requests.get(URL)
if resp.status_code == requests.codes.ok:
    html = resp.text



import re
target = re.compile('http.*://[^ ]+.')
result = target.findall(html)
print(result)
