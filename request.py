import requests
URL = 'http://www.daum.net'
resp = requests.get(URL)
if resp.status_code == requests.codes.ok:
    html = resp.text
    print(html)
