formatter = "{} {} {} {}" #fomatter 변수에 {} 문자열 4개를 정의한다.

# 1. 1행에서 정의한 formatter 문자열을 가져온다.
# 2. 문자열에서 format이라는 함수를 호출한다. 명렬줄에서 'format'이라는 이름의 명령을 실행하는 것과 비슷하다.
# 3. format()함수 안에 있는 값들이 formatter 변수의 '{}' 4개와 대응한다.
# 4. 즉, {1}, {하나}, {True}, {}{}{}{} 이런 식으로 대응한다.
print(formatter.format(1, 2, 3, 4))
print(formatter.format('하나', "둘", "셋", "넷"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "난 이게 있죠.",
    "지금 막 써 주신 그것.",
    "하지만 '노래'하진 않아요.",
    "그러니까 잘 자요.",
    "싫어요." # 이 문장은 출력되지 않는다. 이 문장을 출력하려면 formatter에 정의된 문자열을 5개로 늘려야 한다.
))
