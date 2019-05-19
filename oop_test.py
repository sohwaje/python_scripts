import random                      # 난수 발생 모듈
from urllib.request import urlopen # urllib.request의 기능 중 url의 데이터를 읽는 모듈
import sys                         # 파이썬 인터프리터 모듈
from tqdm import tqdm              # for문 상태바 라이브러리
#===============================================================================
"""
[1]word_URL : 요청받을 URL 주소를 생성.
[2]words = [] : URL에서 가져온 단어들을 채울 words[]생성.
[3]sentences : code_pice:sentence(key:value) 형태의 딕셔너리 자료형 데이터 집합 생성.
"""
word_URL = 'http://learncodethehardway.org/words.txt'
words = []
sentences = {
        "class %%%(%%%):":                                                    # code_pice
            "%%% (이)라는 이름의 클래스를 만드는데 %%%의 일종이다.(is-a)",        # sentence
        "class %%%(object):\n\tdef __init__(self, ***)":
            "클래스 %%%은/는 self와 *** 매개변수를 받는 __init__ 을 가졌다.(has-a)",
        "class %%%(object):\n\tdef ***(self, @@@)":
            "클래스 %%%은/는 self와 @@@ 매개변수를 받는 이름이 ***인 함수를 가졌다.(has-a)",
        "*** = %%%()":
            "*** 변수를 %%% 클래스의 인스턴스 하나로 정한다.",
        "***.***(@@@)":
            "*** 변수에서 *** 함수를 받아와 self, @@@ 매개변수를 넣어 호출한다.",
        "***.*** = '***'":
            "*** 변수에서 *** 속성을 받아와 *** (으)로 값을 정한다.",
            }
#===============================================================================
"""
[1] 스크립트를 실행 할 때, sys.argv[0]은 언제나 스크립트 자기 자신을 가리킨다.
인자값을 주지 않고 스크립트만 실행할 때 즉, sys.argv[0]의 개수는 len(sys.argv)=1이다.
스크립트를 실행할 때 다음과 같이 1개의 인자값을 주어보자. 예)>>> ./test.py 인자1
이것은 스크립트 자기 자신(argv[0])과 인자값(argv[1])을 포함하므로 전체 길이는 "len(sys.argv) = 2"가 된다.
[2] len(sys.argv) == 2 and sys.argv[1] == "korean"
스크립트를 실행할 때 인자값이 두 개이면서(즉, 스크립트 자기 자신과 인자값) 주어진 인자값이 "korean"인 경우
파이썬 엔진은 "front_of_sentences = True"에 마크업한다. 그 외에는 모두 False에 마크업 한다.
"""
if len(sys.argv) == 2 and sys.argv[1] == "korean":   # 스크립트 자신을 포함하여 인자가 2개이면서 "korean"을 만족하면 True
    front_of_sentences = True
else:
    front_of_sentences = False                        # 스크립트 단독 실행 또는 인자값이 3개이면 False
#===============================================================================
"""웹 사이트에서 단어를 불러온다
[1] 웹 사이트를 열고 모든 라인을 읽은 다음 각각의 라인을 리스트 자료형으로 리턴한다.
[2] strip(): 단어 사이의 개행(\n)을 벗겨낸다.
[3] str()에 의해 문자열 형태의 객체로 변환되고 'utf-8'로 인코딩 되어 최종적으로 words[] 리스트에 추가(append)한다.
"""
for word in urlopen(word_URL).readlines():
    words.append(str(word.strip(), encoding='utf-8'))
#    print("word 출력:", word)                         # b'design\n'
#    print("word.strip() 출력", word.strip())          # b'design'
#    print("words 리스트 출력:", words)                  # words = ['account', 'achiever', 'actor', ...]

"""
스크립트 실행 블록에서 받은 코드 조각들의 특수문자를 단어로 변환하는 함수
[1] 함수 이름은 convert이고, 2개의 매개 변수를 갖는다. 첫 번째 매개변수는 code_pice이고 두 번째 매개변수는 sentence이다.
[2] 클래스 문자열(%%%) 개수만큼의 단어를 words 리스트에서 무작위로 추출하고 그 단어들의 첫 글자를 대문자로(capitalize) 변경해서 class_name 리스트에 담는다.
[3] 변수 문자열(***)의 개수만큼의 단어를 words 리스트에서 무작위로 추출하고 그 단어들을 other_names 리스트에 담는다.
"""
def convert(code_pice, sentence):   #[1]
    class_names = [w.capitalize() for w in
                        random.sample(words, code_pice.count("%%%"))] #[2]
    # words 리스트에서 "%%%" 개수만큼의 단어를 랜덤하게 추출한다.
    #print("[6]%%%의 개수:", code_pice.count("%%%"))              # "%%%"의 개수를 산정
    #print("code_pice:", code_pice)                                     # "%%%"가 포함된 코드조각 출력
    #print("[7]%%% 이름들:", class_names)                         # class_names 리스트 출력
    other_names = random.sample(words, code_pice.count("***")) #[3]
    #print("[8]***의 개수:", code_pice.count("***"))                # "***"의 개수를 산정
    # words 리스트에서 "***" 개수만큼의 단어를 랜덤하게 추출
    #print("[9]*** 이름들 :", other_names)                           # other_names 리스트 출력

    results = []        # 리스트를 만든다.
    param_names = []

#매개 변수 이름 호출
    for i in range(0, code_pice.count("@@@")):                  #  for문 반복 횟수 : range(0, 2)이므로  for문은 1회 반복.
        param_num = random.randint(1, 3)                        # 1, 2, 3 중 무작위로 하나를 추출하여 param_num에 담는다.
        #print("for문의 매개변수(@@@)의 수:", param_num)          # 매개변수의 수가 3이면, param_name리스트에 담기는 단어는 3개가 된다.
        param_names.append(', '.join(
            random.sample(words, param_num)))                   # param_num의 개수만큼 매개변수 단어들을 무작위로 추출

        print("매개변수(param_names) 이름:", param_names)   # param_names = [매개변수1, 매개변수2...]

# 두 번째 for문 : code_pice가 for문을 만나서 맨 마지막 results 리스트에 담기고, 그 다음 sentence가 for문을 만나서 results 리스트에 담긴다.
# code_pice의 results를 먼저 리턴하고 다시 for문을 돌아 sentence의 results를 리턴한다. for문을 돌면서 특수문자는 단어로 치환된다.
    for codepic_sentence in code_pice, sentence:
        #print("두 번째 for문의 코드조각:", code_pice, "두 번째 for문의 문장:", sentence)
        result = codepic_sentence
        #print("두 번째 for문의 결과(codepic_sentence):", result)

        # 가짜 클래스 이름
        for word in class_names:                    # 반복문을 통해 가짜 클래스(%%%)를 단어로 바꾼다.
            result = result.replace("%%%", word, 1) # (result.replace(old, new, 바꿀횟수) -> str)
            #print("가짜 클래스(%%%):", result)       # %%% -> 단어

        # 가짜 변수 나머지 이름
        for word in other_names:                     # 반복문을 통해 가짜 변수(***)를 단어로 바꾼다.
            result = result.replace("***", word, 1)
            #print("가짜 변수(***):", result)          # ex) *** -> 단어

        # 가짜 매개변수 이름
        for word in param_names:                      # 반복문을 통해 가짜 매개변수를(@@@)를 단어로 바꾼다.
            result = result.replace("@@@", word, 1)
            #print("가짜 매개변수(@@@):", result)       # ex) @@@ -> 단어

        results.append(result)
        #print("결과들:", results)
    return results

#================================ 함수 정의 끝 ====================================
# CTRL -D를 누를 때까지 계속한다.
"""
[1] 문장들(sentences) 사전에서 key에 해당하는 코드_조각(code_pice)을 code_pices 리스트에 담는다.
# 6개의 code_pice가 리스트에 담긴다.
[2] 문장들(sentences) 사전에서 [code_pice]를 꺼내서 문장(sentence)에 담는다.
# 예) sentence: *** 변수를 %%% 클래스의 인스턴스 하나로 정한다. / code_pice: *** = %%%()
[3] 위에서 얻은 sentence와 code_pice에서 특수문자를 단어로 변경하기 위한 convert 함수를 호출한다.
"""
## 스크립트 실행 블록
try:
    while True:
        code_pices = list(sentences.keys())             #[1]
        #print("[1] code_pice가 들어간 code_pices 리스트 생성:", code_pices)
        random.shuffle(code_pices)                      # code_pices 리스트에 담긴 요소들을 랜덤하게 섞는다.
        #print("[2] code_pices 리스트 섞기", code_pices)
        for code_pice in code_pices:                    # code_pices 리스트에서 요소 1개를 꺼내 code_pice 변수에 담는다.
            #print("[3] code_pices에서 꺼낸 code_pice:", code_pice)
            sentence = sentences[code_pice]             # 위의 code_pice를 값으로 하는 문장을 sentences 사전에서 찾아 sentence에 담는다.
            #print("[4] sentences 사전에서", code_pice, "에 대응하는 sentence:", sentence)
            #print("[5]특수문자 변환 함수 호출-> convert(code_pice, sentence)")
            question, answer = convert(code_pice, sentence)  # 코드조각과 문장을 매개변수로 채우고 특수문자 변환 함수(def convert)를 호출한다.
            #print("Question:", question)
            #print("Answer:", answer)
            if front_of_sentences:                       # front_of_sentences = True이면 실행할 부분
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"answer: {answer}\n\n")
except EOFError:
    print("\nEND")
