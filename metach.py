import re
"""
[1]메타 문자

[ ]	    : [abc]라면 이 표현식의 의미는 "a, b, c 중 한 개의 문자와 매치"
.	    : \n을 제외한 모든 문자와 매치 (점 하나는 글자 하나를 의미)
*	    : 0회 이상 반복 (없어도 상관 없음)
+	    : 1회 이상 반복 (무조건 한번 이상 등장해야 함)
{m, n}	: m회 이상 n회 이하
l	    :or 조건식을 의미
^	    :문자열의 시작 의미
$	    :문자열의 끝을 의미
?	    :0회 이상 1회 이하
\	    :이스케이프, 또는 메타 문자를 일반 문자로 인식하게 한다
( )	    :그룹핑, 추출할 패턴을 지정한다.
"""
"""
[2] 정규식을 이용한 문자열 검색
match()	문자열의 처음부터 정규식과 매치되는지 조사한다.
search()	문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
findall()	정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다
finditer()	정규식과 매치되는 모든 문자열(substring)을 iterator 객체로 리턴한다
"""

text = "cat caaaat ct"

print("====[c*t]==============================================================")
p = re.compile('[c*t]')
print(p.findall(text))
# ['c', 't', 'c', 't', 'c', 't']

print("====[ca*t]=============================================================")
p = re.compile('[ca*t]')
print(p.findall(text)) # => ['c', 'a', 't', 'c', 'a', 'a', 'a', 'a', 't', 'c', 't']

print("====ca+t===============================================================")
p = re.compile('ca+t')
print(p.findall(text))
# ['cat', 'caaaat']

print("====[ca+t]=============================================================")
p = re.compile('[ca+t]')
print(p.findall(text))  # => ['c', 'a', 't', 'c', 'a', 'a', 'a', 'a', 't', 'c', 't']

print("====ca{3,}t===========================================================")
p = re.compile('ca{3,}t')
print(p.findall(text))
# ['caaaat']

print("====[0-9a-zA-Z]========================================================")
p = re.compile('[0-9a-zA-Z]')
print(p.findall(text))
# ['c', 'a', 't', 'c', 'a', 'a', 'a', 'a', 't', 'c', 't']

print("====c|a|t==============================================================")
#p = re.compile('c|a|t')
p = re.compile('[c|a|t]')
print(p.findall(text))
# ['c', 'a', 't', 'c', 'a', 'a', 'a', 'a', 't', 'c', 't']

print("=====http 또는 https로 시작하는 url 찾기====================================")
text = "http://www.naver.com https://www.daum.net/"
p = re.compile('http[s]://.+')
"""
정규식 엔진을 만족하는 문자열은 "http"로 시작한다.
정규식 엔진이 "[]"를 만났을 때 그 안에 문자(s)가 있으면 일치시키고, 없으면 불일치시킨다.
그런데 "?"를 만나면서 []안에 문자가 없는 것도 일치시킨다. 그러다 문자열 "://"와 일치시키고
"."를 만난다. "."는 문자열 1개와 일치한다.
일치되는 문자(여기서는".")가 1개 이상 반복할 때 "+"를 만나면 정규식 엔진은 최대 일치를 시도한다.
"""
print(p.findall(text))

print("================cat만 일치시키기===========================================")
text = "cat caaaat ct"
p = re.compile('^.+?t')
print(p.findall(text))
"""
정규식 엔진을 만족하는 첫 문자는 반드시 "."로 시작(^)해야 한다.
"."가 1개 이상이고 "+"가 나오면 정규식 엔진은 "."가 나오는만큼 최대 일치를 시도한다.
그러다 정규식 엔진이 "?"를 만나면 최대 일치를 취소하고 최소 일치를 시도한다.
"t"까지 일치하면 엔진이 종료된다.
"""
text="<p>The very <em>first</em> task is to find the beginning of a paragraph.</p> <p>Then you have to find the end of the paragraph </p>="
p = re.compile('<p>.*?</p>')
print(p.findall(text))

text = "Her name is Janet."
print(re.findall(r'\bJanet?\b', text))   # t{0, 1}
#['Janet']
print(re.findall(r'\bJane\b|\bJanet\b', text))  #\b는 파이썬에서는 백스페이스(Back Space)를 의미하므로 raw string임을 알려주는 기호 r을 반드시 붙여준다.
#['Janet']
text = "Her name isJanetss."
print(re.findall(r'\BJane\B|\BJanet\B', text))