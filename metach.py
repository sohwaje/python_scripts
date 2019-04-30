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

print("=====^c================================================================")
text = "http://www.naver.com https://www.daum.net/"
p = re.compile('http.+?')
print(p.findall(text))

text = "cat caaaat ct"
p = re.compile('^..+?')
print(p.findall(text))
