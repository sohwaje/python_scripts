import requests, socket, time, datetime, urllib.request
from requests.exceptions import Timeout

"""
url_list.txt을 생성하고 그 안에 감시해야 할 url을 넣는다. ex) www.googld.com
"""
port = 80
def http_url_list(url):
    f = open(url, 'r')
    data = f.readlines()
    f.close()
    return data

def port_check(url):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # UDP는 socket.SOCK_DGRAM
    try:
        s.connect((url, port))
        #return "Open"
    except socket.error as e:
        pass
        #print(url, " on port: ", str(port))


def webpage_check(url):
    full_url = "http://" + url
    print(full_url)
    try:
        html = urllib.request.urlopen(full_url, timeout=3)
        return "Open" #return True
    except urllib.request.URLError as err:
        return err  #return False
    except:
        return "Some other error"

#if __name__ == '__main__':
url_list = http_url_list("url_list.txt")

for i in url_list:
    url = i.split()
    port_checked = port_check(url[0])
    print("port_checked", port_checked)
    webpage_checked = webpage_check(url[0])
    print("webpage_checked", webpage_checked)
