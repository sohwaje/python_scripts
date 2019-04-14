# * 바이트 ->decode()-> 문자열
# * 문자열 ->encode()-> 바이트
print("문자열을 바이트로 encode할게요.")
print("문자열을 입력하세요.")
문자열 = input()
바이트 = 문자열.encode()
print(바이트)
