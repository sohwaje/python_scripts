import sys
스크립트, 입력_인코딩, error = sys.argv

#함수 이름은 main, 3개의 인자값을 받는다.
#언어_파일에서 바이트를 하나씩 읽다가 \n 문자를 만나면 멈춘다. 그리고 다음 줄의 첫바이트를 읽는다.
def main(언어_파일, 인코딩, errors):
    줄 = 언어_파일.readline()

#줄을 만나면, 3개의 인자값을 받는 줄_출력이라는 함수를 만든다.
    if 줄:
        줄_출력(줄, 인코딩, errors)
        return main(언어_파일, 인코딩, errors)

#함수 이름은 줄_출력이고 3개의 인자값을 받는다.
def 줄_출력(줄, 인코딩, errors):
    다음_언어 = 줄.strip() #줄에서 양쪽 공백을 지운다.
    생_바이트열 = 다음_언어.encode(인코딩, errors=errors)
    요리한_문자열 = 생_바이트열.decode(인코딩, errors=errors)

    print(생_바이트열, "<===>", 요리한_문자열)


언어들 = open("languages.txt", encoding='utf-8')

main(언어들, 입력_인코딩, error)
