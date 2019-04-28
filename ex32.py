#숫자들 = [1, 2, 3, 4, 5]
#과일들 = ['사과', '귤', '배', '살구']
#잔돈들 = [1, '십원', 2, '백원', 3, '오백원']

#첫 번째 for 순환문은 list를 따라 돕니다.
#for 숫자 in 숫자들:
#    print(f"이 수는 {숫자}")

#for 과일 in 과일들:
#    print(f"과일 종류: {과일}")

#for i in 잔돈들:
#    print(f"받은 잔돈 {i}")

#리스트 만들기
원소들 = []

# for 함수와 range함수의 조합
for i in range(0, 6): # 0, 6 = 5개의 연속된 숫자를 의미한다.
    print(f"list에 {i} 숫자를 더합니다.")
    # append는 list가 인식하는 함수이다.
    원소들.append(i)
print(원소들)

print("range 함수로만 위 로직을 구현하기")
print(list(range(0, 6)))


#for i in 원소들:
#    print(f"원소는 {i}")


#다른 리스트 만들기
#name = []

#for i in range(0, 10):
#    name.append(i)

#for i in name:
#    print(i)

#quiz
#[1] 30행에 for문을 쓰지 않고 리스트에 넣어보자.
#[2] 리스트에서 append말고 다른 연산을 할 수 있는지 찾아보자.
