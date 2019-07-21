import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import re
"""이 코드는 사이트맵을 제공하는 사이트에서만 유효하다.
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
            if hasattr(e, 'code') and 400 <= e.code < 600: #4xx, 5xx 에러가 발생하면 재귀적 재시도
                return download(url, retries - 1)
    return html

def crawl_sitemap(url):
    # 사이트 맵 파일을 다운로드 한다.
    sitemap = download(url)
    # 사이트 맵 링크를 추출한다.
    links = re.findall('<loc>(.*?)</loc>', sitemap) # 다운로드 한 sitemap에서 <loc> </loc> 태그 부분을 정규 표현식을 사용해 포획한다.
    # 각 링크를 다운로드 한다.
    for link in links:
        html = download(link)

var = "http://example.webscraping.com/sitemap.xml"
print(crawl_sitemap(var))

"""출력 결과
다운로드: http://example.webscraping.com/sitemap.xml
다운로드: http://example.webscraping.com/places/default/view/Afghanistan-1
다운로드: http://example.webscraping.com/places/default/view/Aland-Islands-2
다운로드: http://example.webscraping.com/places/default/view/Albania-3
다운로드: http://example.webscraping.com/places/default/view/Algeria-4
다운로드: http://example.webscraping.com/places/default/view/American-Samoa-5
다운로드: http://example.webscraping.com/places/default/view/Andorra-6
다운로드: http://example.webscraping.com/places/default/view/Angola-7
다운로드: http://example.webscraping.com/places/default/view/Anguilla-8
다운로드: http://example.webscraping.com/places/default/view/Antarctica-9
"""
