import re

def reg(p):
    m = re.compile(p)
    return m
#[예제1]
text = "a before dude"
p = reg('[abc]')
print(p.findall(text))
#결과 : ['a', 'b']
#findall 함수는 결과를 리스트로 출력한다.['값1', '값2'....'값n']
# "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
# "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
# "dude"는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음

#문자 클래스[] : 문자 클래스는 안에 나열된 문자들 중 한 문자와 일치된다. 문자클래스가 반복되어 있을 때 각 클래스는 서로 독립적이다.
text = "123aff456b6c7dDefgh"
p = reg('[0-9]|[a-z]|[A-Z]')
p1 = reg('[0-9a-zA-Z]')
p3 = reg('[^0-9][a-zA-Z]')
p4 = reg('[a-zA-Z]')
p5 = reg('[^a-zA-Z]')
p6 = reg('[0-9][^a-zA-Z]')
p7 = reg('([0-9])[^a-zA-Z]')
print(p.findall(text))
print(p1.findall(text))
print(p3.findall(text))
print(p4.findall(text))
print(p5.findall(text))
print(p6.findall(text))
print(p7.findall(text))
#['1', '2', '3', 'a', 'f', 'f', '4', '5', '6', 'b', '6', 'c', '7', 'd', 'D', 'e', 'f', 'g', 'h']
#['1', '2', '3', 'a', 'f', 'f', '4', '5', '6', 'b', '6', 'c', '7', 'd', 'D', 'e', 'f', 'g', 'h']
#['af', 'dD', 'ef', 'gh']
#['a', 'f', 'f', 'b', 'c', 'd', 'D', 'e', 'f', 'g', 'h']
#['1', '2', '3', '4', '5', '6', '6', '7']
#['1', '4']
text = "aab a0b abc"
p = reg('a.b')
print(p.findall(text))
#['aab', 'a0b']
#abc는 a와 b사이에 아무 것도 없기 때문에 패턴과 일치하지 않는다.

text = "calendar"
p = reg('c[ae]l[ae]nd[ae]r')
p1 = reg('[a-fA-F0-9]')
p2 = reg('[^a-fA-F0-9]')
print(p.findall(text))
print(p1.findall(text))
print(p2.findall(text))
#['calendar']
#['c', 'a', 'e', 'd', 'a']
#['l', 'n', 'r']


print("개행문자를 제외한 따옴표 사이의 모든 단일문자와 일치되는 정규식")
text = "http://search.naver.com/search.naver?where=nexearch&query=%EB%82%98%EC%9D%B4%ED%82%A4+%EC%97%90%EC%96%B4%EB%A7%A5%EC%8A%A4+95&sm=top_lve&ie=utf8"
lines = re.split("\r?\n", text);
p = re.compile('.')
for line in lines[:]:
    if p.search(line):
        print("line: ", line)
    else:
        print(none)

print("개행문자를 포함한 모든 문자와 완전히 일치되는 정규식")
p = re.compile('[/s/S]')
m = p.findall(text)
print(m)
