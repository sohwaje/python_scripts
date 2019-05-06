import requests
import re
# if 200 ok -> catch a url and save
def get(url):
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:
        html = resp.text
    return html

# pattern def
def pattern(x):
    result = re.compile(x)
    return result


# input a URL
URL = input('URL> ')
html = get(URL)

# full url
p = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
text = pattern(p)
result = text.findall(html)         # html에서 fullurl을 추출하여 result에 담는다.
sort = sorted(result, key=len)      # sorted key len
for url in sort:                    # print url in list
    print(url)

# only www
p_1 = '(:?http[s]?://[a-z0-9._]+)'
text = pattern(p_1)
result = text.findall(html)
sort = sorted(result, key=len)
for www in sort:
    print(www)
