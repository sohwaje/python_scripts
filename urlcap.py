import requests
import re

def get(url):
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:       # if 200 ok -> catch a url and save function
        html = resp.text
    return html

# pattern def function
def pattern(x):
    result = re.compile(x)
    return result

# full url function (URL 전체를 출력)
def full_url():
    URL = input('URL> ')
    html = get(URL)
    p = 'http[s]?://(?:[a-zA-Z]|[0-9][-]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'    # FULL URL 캡쳐 정규식
    text = pattern(p)
    result = text.findall(html)                      # html에서 fullurl을 추출하여 result에 담는다.
    sort = sorted(result, key=len)                   # URL 길이에 따라 정렬
    for url in sort:                                 # URL 리스트에서 URL 출력
        print(url)

# only www function (WWW URL 출력)
def only_www():
    URL = input('URL> ')
    html = get(URL)
    p_1 = '(:?http[s]?://[a-z0-9._\-]+)'                                                        # WWW URL 캡쳐 정규식
    text = pattern(p_1)
    result = text.findall(html)
    sort = sorted(result, key=len)
    for www in sort:
        print(www)

# exit function
def End_of_script(x):
    print(x, "Good Bye")
    exit(0)

# start function
def start():
    print("Capture full url select: 1, ex)http://www.abc.com/abc/&879/778_ga.gif")
    print("Capture www select: 2, ex)http://www.abc.com")

    choice = input("> ")

    if choice == "1":
        full_url()
    elif choice == "2":
        only_www()
    else:
        End_of_script("Thank you")

# start of script
start()
