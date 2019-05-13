import random                      # 난수 발생 모듈
from urllib.request import urlopen # urllib.request의 기능 중 url의 데이터를 읽는 모듈
import sys                         # 파이썬 인터프리터 모듈
from tqdm import tqdm              # for문 상태바 라이브러리
#===============================================================================
"""
[1]word_URL : 요청받을 URL 주소를 생성한다.
[2]words = [] : URL에서 가져온 단어들을 리스트 자료형으로 채울 수 있는 빈 words리스트를 생성한다.
[3]sentences : "키":"값"이 들어 있는 딕셔너리 자료형 데이터를 생성한다.
"""
word_URL = 'http://learncodethehardway.org/words.txt'
words = []
sentences = {
        "class %%%(%%%):":                                       # code_pices[0], code_pice.count(%%%) = 2
            "%%% (이)라는 이름의 클래스를 만드는데 %%%의 일종이다.(is-a)",
        "class %%%(object):\n\tdef __init__(self, ***)":         # code_pices[1], code_pice.count(%%%) = 1, code_pice.count(***) = 1
            "클래스 %%%은/는 self와 *** 매개변수를 받는 __init__ 을 가졌다.(has-a)",
        "class %%%(object):\n\tdef ***(self, @@@)":              # code_pices[2], code_pice.count(%%%) = 1, code_pice.count(***) = 1
            "클래스 %%%은/는 self와 @@@ 매개변수를 받는 이름이 ***인 함수를 가졌다.(has-a)",
        "*** = %%%()":                                           # code_pices[3]
            "*** 변수를 %%% 클래스의 인스턴스 하나로 정한다.",
        "***.***(@@@)":                                          # code_pices[4]
            "*** 변수에서 *** 함수를 받아와 self, @@@ 매개변수를 넣어 호출한다.",
        "***.*** = '***'":                                       # code_pices[5]
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
즉, 이 코드가 True가 되려면 반드시 인자값의 이름은 "korean"이어야 한다.
"""
if len(sys.argv) == 2 and sys.argv[1] == "korean":   # 스크립트 자신을 포함하여 인자가 2개이면서 "korean"을 만족히먄 True
    front_of_sentences = True
else:
    front_of_sentences = False                        # 스크립트 단독 실행 또는 인자값이 3개이면 False
#===============================================================================
"""웹 사이트에서 단어를 불러온다
[1] 웹 사이트를 열고 모든 라인을 읽은 다음 각각의 라인을 리스트 자료형으로 리턴하여 word 변수에 담는다.
# b'design\n'
[2] strip(): 단어 사이의 개행을 벗겨낸다.
# b'design'
[3] str()에 의해 문자열 형태의 객체로 변환되고 'utf-8'로 인코딩 되어 최종적으로 words[] 리스트에 추가(append)한다.
# ['account', 'achiever', 'actor', ...]
"""
for word in urlopen(word_URL).readlines():
    words.append(str(word.strip(), encoding='utf-8'))
#    print("word 출력:", word)                         # b'design\n'
#    print("word.strip() 출력", word.strip())          # b'design'
#    print("words 리스트 출력:", words)                  # words = ['account', 'achiever', 'actor', ...]

"""
변환 함수 생성 : convert(code_pice, sentence)
[1] 함수 이름은 convert이고, 2개의 매개 변수를 갖는다.
[2] "%%%"의 개수만큼의 단어를 words 리스트에서 랜덤하게 추출하고 첫 글자를 대문자로(capitalize()) 바꾼다음 class_name 리스트에 담는다.
[3] owords 리스트에서 *** 개수만큼의 단어를 랜덤하게 추출하고 other_names 리스트에 담는다.
"""
def convert(code_pice, sentence):   #[1]
    class_names = [w.capitalize() for w in
                        random.sample(words, code_pice.count("%%%"))] #[2]
    # words 리스트에서 "%%%" 개수만큼의 단어를 랜덤하게 추출한다.
    print("클래스(%%%)의 개수:", code_pice.count("%%%"))              # "%%%"의 개수를 산정
    #print("code_pice:", code_pice)                         # "%%%"가 포함된 코드조각 출력
    print("클래스(%%%) 이름들:", class_names)                  # class_names 리스트에 들어간 단어 출력(ex: class_names : ['Cry'])
    other_names = random.sample(words, code_pice.count("***")) #[3]
    print("변수(***)의 개수:", code_pice.count("***"))              # "***"의 개수를 산정
    # words 리스트에서 "***" 개수만큼의 단어를 랜덤하게 추출
    print("변수(***)이름들 :", other_names)              # other_names 리스트에 들어간 단어 출력

    results = []        # 리스트를 만든다.
    param_names = []

#첫 번째 for문
    for i in range(0, code_pice.count("@@@")):                 # 0부터 code_pice("@@@")의 개수를 하나씩 i에 대입
        param_num = random.randint(1, 3)                        # 1, 2, 3 중 무작위로 하나를 추출하여 param_num에 담는다.
        print("첫 번째 for문의 매개변수(@@@)의 수:", param_num)
        param_names.append(', '.join(
            random.sample(words, param_num)))                   # 단어들에서 매개변수 수만큼 무작위로 추출
        print("첫 번째 for문의 매개변수(param_names) 이름:", param_names)   # param_names = [이름, 이름2, 이름3...]

#두 번째 for문
    for sentence in code_pice, sentence:
        print("두 번째 for문의 코드조각:", code_pice, "두 번째 for문의 문장:", sentence)           # ex) ***.***(@@@)
        result = sentence
        print("두 번째 for문의 결과(result):", result)          # ex) ***.***(@@@)

        # 가짜 클래스 이름 (클래스가 없으면 이 부분의 결과는 나오지 않는다.)
        for word in class_names:                    # 가짜 class_names "%%%"를  word() 바꾼다.
            result = result.replace("%%%", word, 1) # (result.replace(old, new, 바꿀횟수) -> str)
            print("가짜 클래스(%%%) 이름:", result)

        # 가짜 변수 나머지 이름(변수가 없으면 이 부분의 result는 나오지 않는다.)
        for word in other_names:                     # 가짜 가짜변수(other_names) "***"를 word로 1회 바꾼다.
            result = result.replace("***", word, 1)  # 가짜 변수가 2개("***", "***")면 2회 바꾼다.
            print("가짜 변수(***) 이름:", result)        # ex) 단어.***(@@@) -> 단어.단어(@@@)

        # 가짜 매개변수 이름
        for word in param_names:                      # 가짜 param_names "@@@"를 word로 바꾼다.
            result = result.replace("@@@", word, 1)
            print("가짜 매개변수(@@@) 이름:", result)      # ex) 단어.단어(매개변수 단어)

        results.append(result)                        # result를 results 리스트에 추가한다.
        print("결과들:", results)        # ex) ['단어.단어[매개변수, 매개변수']
    return results

#================================ 함수 정의 끝 ====================================
# CTRL -D를 누를 때까지 계속한다.
"""
[1] code_pices = list(sentences.keys()): 문장들(sentences)에서 key에 해당하는 코드_조각을 코드_조각들(code_pices)을 리스트에 담는다.
# 6개의 code_pice가 리스트에 담긴다.
[2] sentence = sentences[code_pice] : 문장들(sentences) 사전에서 [code_pice]를 꺼내서 sentence에 담는다.
# 출력 : sentence: *** 변수를 %%% 클래스의 인스턴스 하나로 정한다. / code_pice: *** = %%%()
[3] question, answer = convert(code_pice, sentence) # 주어진 code_pice와 sentence를 변환하여 question, answer에 각각 담는다.
# 왼쪽 출력 : question / answer : "butto = Balance()" / "butto 변수를 Balance 클래스의 인스턴스 하나로 정한다."
# 오른쪽 출력 : code_pice / sentence : "*** = %%%()" / "클래스 %%%은/는 self와 *** 매개변수를 받는 __init__ 을 가졌다.(has-a)"
"""
## 코드 실행 부분
try:
    while True:
        code_pices = list(sentences.keys())             #[1]
        #print("while문 code_pices:", code_pices)
        random.shuffle(code_pices)                      # code_pices 리스트를 랜덤하게 섞는다.
        #print("while문 shuffle_code_pices", code_pices)
        for code_pice in code_pices:                    # 코드_조각들 리스트에서 코드_조각을 꺼낸다.
            sentence = sentences[code_pice]             # key:value -> 사전{sentences}에서 sentences[code_pice]에 해당하는 문장을 찾는다.
            #print("sentence:", sentence, "code_pice:", code_pice)
            question, answer = convert(code_pice, sentence)  # def convert 함수를 호출한다.
            #print("question:", question, "answer:", answer)
            #print("sentence:", sentence)
            if front_of_sentences:                       # front_of_sentences = True이면 실행할 부분
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"answer: {answer}\n\n")
except EOFError:
    print("\nEND")
