"""
라이브러리 불러오기
[1] import random : 난수 발생 모듈을 불러온다.
[2] from urllib.request : 웹 작업을 수행(urllib)하는 모듈의 기능 중 HTTP 요청을 담담을 하는 모듈(request)을 불러온다.
[3] import urlopen : urllib.request의 기능 중 url에서 데이터를 읽어 들이는 모듈(urlopen)을 불러온다.
[4] import sys : 파이썬 인터프리터와 관련된 정보와 기능을 제공하는 모듈을 불러온다.
"""
import random
from urllib.request import urlopen
import sys
#===============================================================================
"""
[1]word_URL : 요청받을 URL 주소를 생성한다.
[2]words = [] : URL에서 가져온 단어들을 리스트 자료형으로 채울 수 있는 빈 words리스트를 생성한다.
[3]sentences : "키":"값"이 들어 있는 딕셔너리 자료형 데이터를 생성한다.
"""
word_URL = 'http://learncodethehardway.org/words.txt'
words = []
sentences = {
        "class %%%(%%%):":                                       # code_pices[0]
            "%%% (이)라는 이름의 클래스를 만드는데 %%%의 일종이다.(is-a)",
        "class %%%(object):\n\tdef __init__(self, ***)":         # code_pices[1]
            "클래스 %%%은/는 self와 *** 매개변수를 받는 __init__ 을 가졌다.(has-a)",
        "class %%%(object):\n\tdef ***(self, @@@)":              # code_pices[2]
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
if len(sys.argv) == 2 and sys.argv[1] == "korean":  #인자값 1개(즉, 인자가 2개)이면서 "korean"을 만족할 때.
    front_of_sentences = True
else:
    front_of_sentences = False
#===============================================================================
"""웹 사이트에서 단어를 불러온다
[1] 웹 사이트를 열고 모든 라인을 읽은 다음 각각의 라인을 리스트 자료형으로 리턴하여 word 변수에 담는다.
# word = b'design\n'
[2] strip() 함수에 의해 단어 사이의 개행이 벗겨진다.
# word.strip() = b'design'
[3]단어들은 str()에 의해 문자열 형태의 객체로 변환되고 'utf-8'로 인코딩 되어 최종적으로 words[] 리스트에 추가(append)된다.
# ['account', 'achiever', 'actor', ...]
"""
for word in urlopen(word_URL).readlines():
    words.append(str(word.strip(), encoding='utf-8'))
#    print("word 출력:", word)                         # 출력 예: b'design\n'
#    print("word.strip() 출력", word.strip())          # 출력 예: b'design' -> strip()은 \n를 벗겨낸다.
#    print("words 리스트 출력:", words)                  # 출력 예 : ['account', 'achiever', 'actor', ...]

#===============================================================================
#=============================== 함수 정의 =======================================
"""
변환 함수 생성 : convert(code_pice, sentence)
[1] 코드조각(code_pice)와 문장(sentence)을 매개 변수로 갖는 변환 함수(convert())를 생성한다.
[2] 코드조각에서 "%%%"의 개수를 구한다. -> words[리스트]에서 "%%%"의 개수만큼의 단어를 랜덤하게 추출하여 for문 변수 w에 담는다.
-> 변수 w에 담긴 word의 첫 글자를 대문자로(capitalize()) 바꿔서 class_names=[리스트]를 만든다.
[3] 코드조각에서"***"의 개수를 구한다. -> 그 개수만큼 words[리스트]에서 word를 랜덤하게 추출한다.
-> other_names=[리스트]를 만든다.
[4]0부터 "@@@"의 개수 사이의 요소 1개를 for문 변수 i에 담는다.
[5]randpint(1,2,3)에서 임의의 수 1개를 매개변수_수(param_num)에 담는다.
[6]words[리스트]에서 randpoint에 의해 정해진 매개변수_수(param_num)만큼 무작위로 단어를 추출한다.
[7]추출한 단어들을 (','.join)으로 구분하여 매개변수_이름들(param_names[리스트])에 추가(append)한다.
"""
def convert(code_pice, sentence):
    class_names = [w.capitalize() for w in
                        random.sample(words, code_pice.count("%%%"))]
#    print("class_names 출력:", class_names)             # 출력 : ['Condition']
    other_names = random.sample(words, code_pice.count("***"))
#    print("other_names 출력:", other_names)             # 출력 : ['blade']

    results = []                         # 빈 결과들 리스트를 만든다.
    param_names = []                     # 빈 파라미터 이름 리스트를 만든다.

    for i in range(0, code_pice.count("@@@")):      # range(시작, 끝)
        param_num = random.randint(1, 3)            # 1, 2, 3 중 무작위로 하나
        param_names.append(', '.join(               # param_names = [이름, 이름2, 이름3...]
            random.sample(words, param_num)))       # 단어들에서 매개변수 수만큼 무작위로 추출

    for sentence in code_pice, sentence:            # 코드조각과 문장의 요소를 sentence 변수에 담고, 이를 result 변수에 담는다.
        result = sentence                           # class %%%(%%%):
                                                    # %%% (이)라는 이름의 클래스를 만드는데 %%%의 일종이다.(is-a)
        # 가짜 클래스 이름
        for word in class_names:                    # "%%%"를 word로
            result = result.replace("%%%", word, 1) # result.replace(old, new[, count]) -> str

        # 가짜 나머지 이름
        for word in other_names:
            result = result.replace("***", word, 1)

        # 가짜 매개변수 이름
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results
#================================ 함수 정의 끝 ====================================
# CTRL -D를 누를 때까지 계속한다.
"""
[1] code_pices = list(sentences.keys()): 문장들(sentences)에서 key에 해당하는 코드_조각(code_pices)을 리스트에 담는다.
# 6개의 code_pice가 리스트에 담긴다.
[2] random.shuffle(code_pices) : 코드_조각들[code_pices] 리스트 안의 요소들을 랜덤하게 섞는다.
[3] for code_pice in code_pices: 코드_조각들 리스트에서 코드_조각을 꺼낸다.
[4] sentence = sentences[code_pice] : 문장들(sentences) 사전에서 [code_pice]를 꺼내서 sentence에 담는다.
# 출력 : sentence: *** 변수를 %%% 클래스의 인스턴스 하나로 정한다. / code_pice: *** = %%%()
"""
try:
    while True:
        code_pices = list(sentences.keys())
        #print("code_pices:", code_pices)
        random.shuffle(code_pices)
        #print("shuffle_code_pices", code_pices)
        for code_pice in code_pices:
            sentence = sentences[code_pice]     # key:value -> 사전{sentences}에서 sentences[code_pice]에 해당하는 문장을 찾는다.
            #print("sentence:", sentence, "code_pice:", code_pice)
            question, answer = convert(code_pice, sentence)
            if front_of_sentences:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"answer: {answer}\n\n")
except EOFError:
    print("\nEND")
