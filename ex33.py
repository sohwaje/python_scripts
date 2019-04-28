"""
while boolean이 True인 동안 그 아래의 코드 블록을 계속 실행한다.
*TIP
1. while문을 지양하고 for문을 쓰자.
2. while 블록을 검토하자. 언제 False를 만나는지 꼭 확인하자.
3. 필요할 때 while문의 코드 블록이 어떻게 순환되고 있는지 검사 변수를 출력하여 검토하자.
"""
#--코드시작--#
i = 0
숫자들 = []

while i < 6:                    # i = 0~5까지
    print(f"꼭대기에서 i는 {i}")
    숫자들.append(i)             #숫자 리스트 안에 0부터 5까지 넣는다. [0, 1, 2, 3, 4, 5]

    i = i + 1
    print("숫자는 이제: ", 숫자들)  #append가 리스트 안에 숫자를 하나씩 넣는다.
    print(f"바닥에서 i는 {i}")    # i = 1 + 1

print("숫자: ")

for 숫자 in 숫자들:               #숫자들 리스트에 있는 숫자를 차례로 출력
    print(숫자)
#--코드 끝--#

#--코드 시작--#
# while문을 함수로 만들어 사용.
print(" ")
def while_test(a, b, c, d):          # 매개변수 4개를 갖는 while_test함수
    if a < b:
        print("스크립트 실행")
    else:
        print("매개변수가 잘못되었습니다. 스크립트를 종료합니다.")
    while a < b:                     # a < b True이면 아래 블록을 실행
        print(f"꼭대기에서는 {a}")
        c.append(a)                  # 매개변수 a가 append에 의해 리스트 c에 저장.
        a = a + d                    # a = a + d 매개변수 만큼 값을 늘리고 while문을 다시 호출.
        print(c)
a = 1                                #매개 변수 시작 값
b = 7                                #매개 변수 마지막 값
c = []                               #매개 변수가 담길 리스트
d = 1                                #매개 변수 a에 1만큼 늘린다.

while_test(a, b, c, d)
#--코드 끝--#

#--코드 시작--#
print(" ")
print("while문 대신 for문으로 바꿔보자.")
result = []
for i in range(0, 6):
    print(f"하나씩 {i}")
    result.append(i)
print(result)

#--코드 시작--#
print(" ")
print("for문 없이 ragne 함수로 리스트에 저장")
print(list(range(100, 105)))        #내장 list함수로 range 범위의 값들을 리스트로 출력
#--코드 끝--#
