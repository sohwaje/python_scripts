import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
# 로그인 정보
INFO = {
    'j_username': '아이디',
    'j_password': '패스워드'
}
# 세션 시작
session = requests.session()

# 로그인
url_login = "로그인URL"
res = session.post(url_login, data=INFO)
res.raise_for_status()  #예외 발생 시

# 파싱할 페이지 접근
page = "파싱할 페이지"
res = session.get(page)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
p = soup.select("Copy selector 파싱 영역 지정") #ex : '#div_content > div.post-title > div.title-subject > div'
print(p)
