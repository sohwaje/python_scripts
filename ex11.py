print("사칙연산 연습")
print("첫번째 숫자를 입력하세요", end='')
a = int(input())
print(f"{a}를 입력하셨습니다.")
print("두번째 숫자를 입력하세요", end='')
b = int(input())
print(f"{b}를 입력하셨습니다.")
print("세번째 숫자를 입력하세요", end='')
c = int(input())
print(f"{c}를 입력하셨습니다.")
print("네번째 숫자를 입력하세요", end='')
d = int(input())
print(f"{d}를 입력하셨습니다.")


print(f"{a} + {b} + {c} + {d}는 몇일까요?")
print("값: ", a + b + c + d)
print(f"{a} * {b} / {c} - {d}는 몇일까요?")
print("값: ", round(a * b / c - d))

#print(f"두 숫자의 합: {c}")

#print("몇 살이죠?", end='') #end=''를 넣으면 줄바꿈하지 않는다.
#나이 = input()

#print("키는 몇이죠?", end='')
#키 = input()

#print("몸무게는 얼마죠?", end='')
#몸무게 = input()

#print(f"네, 나이는 {나이}살, 키는 {키}cm, 몸무게는 {몸무게}kg입니다.") #변수가 담긴 문자열을 사용할 때 "f(format)"변수를 사용한다.
