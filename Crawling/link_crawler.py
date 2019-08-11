import re
import urllib.request
from urllib.parse import urljoin
from urllib.error import URLError, HTTPError, ContentTooShortError

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

def link_crawler(start_url, link_regex):
    """지정된 시작 start_url에서 link_regex와 일치하는 링크를 크롤링한다.
    """
    crawl_queue = [start_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        if html is not None:
            continue
    # 정규식과 일치하는 링크만 필터링한다.
        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)

def get_links(html):
    """ html에서 링크 목록을 리턴한다."""
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""", re.IGNORECASE) # 웹페이지의 모든 링크를 추출하는 정규식이다.
    #웹페이지의 모든 링크를 리턴한다.
    return webpage_regex.findall(html)

"""start scripts"""
var = "http://example.webscraping.com"
pattern = ('.*/(index|view)/.*')
print(link_crawler(var, pattern))
