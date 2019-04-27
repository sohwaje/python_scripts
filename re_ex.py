import re

text = """
tomato','potato','aaabc','iiibc','aiabc','aaibc','iiabc
"""
p = re.compile('[tom|pot]*ato')
m = p.findall(text)
for i in m:
    print(i)

p = re.compile('[a-z]*bc', re.VERBOSE)
m = p.findall(text)
for i in m:
    print(i)

text = """
/""
'

/
"""
p = re.compile('[\W]')
m = p.findall(text)
print(m)

#m = re.compile('(tom|pot)ato')
#print(m.findall(text))

data = """
park 800905-1049118
kim  700905-1059119
"""
p = re.compile("(\d{6}[-]\d{7})")
m = p.findall(data)
for i in m:
    print(i)



#메타문자 해설
#[ ] : 문자 부류를 지정한다. 즉, 일치시키고자 하  문자 집합을 지정한다. 이 안에서는 메타 문자도 문자 부류로 인식된다.(단, 여집합 기호^는 제외한다.)
# \ : 역사선이다. 메타 문자의 속성을 없앤다. 즉 "\("는 문자열 "("것과 일치한다.
# \(\) -> 소괄호 ()를 문자열로 인식한다.
#
