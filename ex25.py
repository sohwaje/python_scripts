#=================================함수 정의==================================
#[1]
def 단어_쪼개기(값):
    """문자열을 단어 단위로 쪼개줍니다"""
    단어들 = 값.split(' ')
    return 단어들
#[2]
def 단어_정렬(단어들):
    """단어를 정렬합니다."""
    return sorted(단어들)
#[3]
def 첫_단어_출력(단어들):
    """첫 단어를 꺼내고 출력합니다."""
    단어 = 단어들.pop(0)
    print(단어)
#[4]
def 마지막_단어_출력(단어들):
    """마지막 단어를 꺼내고 출력합니다."""
    단어 = 단어들.pop(-1)
    print(단어)
#[5]
def 문장_정렬(문장):
    """한 문장을 통째로 받아 정렬된 단어를 반환합니다."""
    단어들 = 단어_쪼개기(문장) #단어_쪼개기 함수를 호출하여 return값을 단어들에 담는다.
    return 단어_정렬(단어들) #단어_정렬 함수를 이용하여 정렬된 단어를 반환한다.
#[6]
def 처음과_마지막_단어_출력(문장):
    """문장의 처음과 마지막 단어를 출력합니다."""
    단어들 = 단어_쪼개기(문장) #단어_쪼개기 함수가 문장을 단어 단위로 분리하여 단어들 변수에 담는다.
    첫_단어_출력(단어들) #첫_단어_출력 함수가 단어들에서 첫 단어를 반환한다.
    마지막_단어_출력(단어들) #마지막_단어_출력 함수가 단어들에서 마지막 단어를 반환한다.
#[7]
def 정렬_후_처음과_마지막_단어_출력(문장):
    """단어를 정렬하고 처음과 마지막 단어를 출력합니다."""
    단어들 = 문장_정렬(문장)
    첫_단어_출력(단어들)
    마지막_단어_출력(단어들)
#================================함수 정의 끝======================================
문장 = "기다리는 자에게 복이 온다."
#===============================================================================
#[1]단어_쪼개기 함수로 문장을 단어 단위로 분리한다.
print("단어들 출력")
단어들 = 단어_쪼개기(문장)
print(단어들)
#===============================================================================
#[2]분리된 단어들이 단어_정렬 함수에 의해 정렬(sorted)된다.
print("단어들에서 정렬한 단어들")
단어들에서_정렬한_단어들 = 단어_정렬(단어들)
print(단어들에서_정렬한_단어들)
#===============================================================================
#[3]정렬된 단어들에서 첫 단어를 출력한다. 단어들.pop(0)
print("정렬한 단어들에서 첫 단어 출력")
첫_단어 = 첫_단어_출력(단어들)
print("정렬한 단어들에서 마지막 단어 출력")
#===============================================================================
#[4]정렬된 단어들에서 마지막 단어를 출력한다. 단어들.pop(-1)
마지막_단어 = 마지막_단어_출력(단어들)
print("첫 단어와 마지막 단어를 뺀 단어들 출력")
print(단어들) #첫_단어와 마지막_단어를 뺀 단어들을 출력한다.
#===============================================================================
#[5]
#단어_쪼개기 함수를 호출 -> 문장을 단어 단위로 분리하여 "단어들" 변수에 담는다.
#"단어들" 변수를 "단어_정렬" 함수로 넘기고 그 값을 반환(return)한다.
print("문장에서 정렬한 단어들 출력")
문장에서_정렬한_단어들 = 문장_정렬(문장)
print(문장에서_정렬한_단어들)
#===============================================================================
#[6]
print("문장에서 처음과 마지막 단어 출력")
처음과마지막_단어 = 처음과_마지막_단어_출력(문장)
#===============================================================================
#[7]
print("정렬한 문장에서 처음과 마지막 단어 출력")
정렬후_처음과마지막_단어 = 정렬_후_처음과_마지막_단어_출력(문장)
#===============================================================================
