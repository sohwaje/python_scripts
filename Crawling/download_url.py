import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
"""
1. 웹페이지 다운로드
2. 다운로드 재처리
3. 사용자 에이전트 설정 : 기본 사용자 에이전트를 wswp(Web Scraping with Python라는 의미)로 설정한다.
"""
"""
hasattr 함수: (e, 'code') 에러에 'code' 변수가 있는지 확인한다.
wswp(Web Scraping with Python)
"""
def download(url, retries=2, user_agent='wswp', charset='utf-8'):
    print('다운로드:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent) # 사용자 에이전트를 추가한다.
    try:
        html = urllib.request.urlopen(request).read() # urlopen 함수는 웹 페이지를 다운로드 하고 html을 리턴한다.
    except (URLError, HTTPError, ContentTooShortError) as e: # 다운로드 또는 url 에러에 대한 예외 처리.
        print('다운로드 에러:', e.reason)
        html = "알 수 없는 오류가 발생하였습니다."
        if retries > 0:
            if hasattr(e, 'code') and 400 <= e.code < 600:
                # 4xx, 5xx 에러가 발생하면 재귀적 재시도
                return download(url, retries - 1)
    return html


var = "http://httpstat.us/500"
print(download(var))

"""결과
다운로드: http://httpstat.us/500
다운로드 에러: Internal Server Error
다운로드: http://httpstat.us/500
다운로드 에러: Internal Server Error
다운로드: http://httpstat.us/500
다운로드 에러: Internal Server Error
알 수 없는 오류가 발생하였습니다.
"""
