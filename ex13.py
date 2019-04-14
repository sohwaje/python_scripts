from sys import argv
#import는 파이썬의 기능에서 스크립트에 필요한 기능을 가져다 쓰는 방법
#argv는 "전달인자"라고 부른다. 스크립트를 실행할 때 전달할 값을 넣어야 한다.
#예를들면 python3.7 ex13.py arg1, arg2
#스크립트, 첫_번째, 두_번째, 세_번째, 네_번째, 다섯_번째 = argv
#아래 전달인자 중에서 "a"는 파일의 이름을 가리킨다. 이것은 약속이다.
a, b, c, d, e = argv

print("스크립트 이름:", a)
print("첫_번째 변수:", b)
print("두_번째 변수:", c)
print("세_번째 변수:", d)
print("네_번째 변수:", e)


print("파일 이름을 무엇으로 바꿀까요?:", end = '')
a = input()
print(f"{a}")
