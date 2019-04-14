# add_mul이라는 함수를 만들고 2개의 인자값을 받는다.
# 이때 *args는 한꺼번에 여러개의 인자값을 모아서 받을 수 있게 한다.
# 첫번째 인자값이 "add"일 경우 result = 0으로 설정한다.
# *args로 받은 인자값 중 첫번째 것을 result=0에 더하고 이 값을 다시 result에 저장한다.
# 저장된 result 값에 *args로 받은 인자값 중 두번째 것을 더하고 이 값을 다시 result에 저장한다.
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
# 16 + 6 = 21  <==리턴 값 
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


result = add_mul("add", 1, 2, 3, 4, 5, 6)
print(result)
result = add_mul("mul", 1, 2, 3, 4, 5, 6)
print(result)
