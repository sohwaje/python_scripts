#kant.txt 파일을 읽어서 출력해보자.
#먼저 이 스크립트가 전달인자를 받는 스크립트 임을 명시하자.
from sys import argv
script, TEXT = argv

#[1]kant.txt를 열고 읽는 함수를 만든다.
def INPUT_TXT(TEXT):
    print(TEXT.read(), end='')
#[2]파일을 0바이트 부분으로 이동시킨다.
def BACKWARD(TEXT):
    TEXT.seek(0)
#[3]파일의 내용을 한 줄씩 읽어들인다.
def READ_LINE(L, TEXT):
    print(LIST, TEXT.readline())

print("파일 전체를 출력합니다.")
OUTPUT_TXT = open(TEXT)
INPUT_TXT(OUTPUT_TXT)

#파일 되감기
print("파일을 되감기 하겠습니다.")
BACKWARD(OUTPUT_TXT)

#====================================================================================
print("파일의 전체 내용을 한 줄 씩 읽어서 출력해볼게요")
f = open(TEXT) #전달받은 스크립트(TXT)를 읽기 모드 읽어들여서 변수(f)에 저장
LINES = f.readlines() #f에 저장된 스크립트의 내용을 \n을 만날 때까지 한 줄 씩 읽어 LINES에 저장한다.
for line in LINES:  #LINES에 저장된 라인 리스트를 변수(line)에 담는다.
    print(line)  #변수에 담긴 라인 리스트를 출력한다. print는 반드시 들여쓰기 한다.
f.close() #변수(f)을 닫는다.
#====================================================================================

# 파일에 저장된 내용을 LIST에 담긴 번호를 붙여 한 줄씩 차례로 출력하다가,
# 중간에 파일을 다시 0바이트 위치로 복귀 시킨 후에 다시 파일을 한 줄씩 출력한다.
print("파일 안에 저장된 내용을 번호를 붙여 출력해볼게요.")
LIST = 0 # 0 바이트에서 \n을 만날 때까지의 내용을 LIST에 저장한다.
READ_LINE(LIST, OUTPUT_TXT)

LIST = LIST + 1 # 0 + 1 바이트에서 \n을 만날 때까지의 내용을 LIST에 저장한다.
READ_LINE(LIST, OUTPUT_TXT)

LIST = LIST + 1 # 0 + 1 + 1 바이트에서 \n을 만날 때까지의 내용을 LIST에 저장한다.
READ_LINE(LIST, OUTPUT_TXT)

# 여기서 파일을 다시 0바이트의 위치로 되돌린다.
print("파일을 다시 되감겠습니다.")
BACKWARD(OUTPUT_TXT) #파일을 0바이트의 위치로 되감는다.

# 파일의 0바이트 부분을 LIST에 저장한다.
LIST = LIST + 0
READ_LINE(LIST, OUTPUT_TXT)

#formatter = "{}" # formatter 문자열 변수에 {} 저장한다.
#LIST = formatter.format("2") #format 안의 문자열 2를 formatter에 전달하고 그 값을 LIST에 저장한다.
#READ_LINE(LIST, OUTPUT_TXT)

#LIST = LIST + "1" #문자열 2 + 문자열 1 = 21
#READ_LINE(LIST, OUTPUT_TXT)

#LIST = LIST + "2" # 문자열 2 + 문자열 1 + 문자열 2 = 212
#READ_LINE(LIST, OUTPUT_TXT)
