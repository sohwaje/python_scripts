import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import re
import itertools
"""
이 코드는 사이트맵을 제공하는 사이트에서만 유효하다.

"""
def download(url, retries=2, user_agent='wswp', charset='utf-8'):
    print('다운로드:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset() # headers 철자 주의.
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('다운로드 에러:', e.reason)
        html = "알 수 없는 오류가 발생하였습니다." # 또는 html = None
        if retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600: #4xx, 5xx 에러가 발생하면 재귀적 재시도
                return download(url, retries - 1)
    return html

#def crawl_sitemap(url):
    # 사이트 맵 파일을 다운로드 한다.
#    sitemap = download(url)
    # 사이트 맵 링크를 추출한다.(각 사이트 맵 구성마다 다르다.)
#    links = re.findall('<loc>(.*?)</loc>', sitemap) # 다운로드 한 sitemap에서 <loc> </loc> 태그 부분을 정규 표현식을 사용해 포획한다.
    # 각 링크를 다운로드 한다.
#    for link in links:
#        html = download(link)

def crawl_site(url):
    for page in itertools.count(1):         # count 1부터 시작
        pg_url = '{}{}'.format(url, page)   # count 함수에 의해 url/1, url/2....url/n 까지 증가
        html = download(pg_url)
        if html is None:
            num_errors += 1
            if num_errors == max_errors:    # 최대 에러 값에 도달하면 루프를 탈출한다.
                break
        else:
            num_erros = 0
var = "http://example.webscraping.com/places/default/view/"
print(crawl_site(var))

"""출력 결과
다운로드: http://example.webscraping.com/places/default/view/1
다운로드: http://example.webscraping.com/places/default/view/2
다운로드: http://example.webscraping.com/places/default/view/3
다운로드: http://example.webscraping.com/places/default/view/4
다운로드: http://example.webscraping.com/places/default/view/5
다운로드: http://example.webscraping.com/places/default/view/6
다운로드: http://example.webscraping.com/places/default/view/7
다운로드: http://example.webscraping.com/places/default/view/8
다운로드: http://example.webscraping.com/places/default/view/9
다운로드: http://example.webscraping.com/places/default/view/10
다운로드: http://example.webscraping.com/places/default/view/11
다운로드: http://example.webscraping.com/places/default/view/12
"""
