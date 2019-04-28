#분기와 함수를 사용하는 코드
from sys import exit
#[3]함수 gold_room()
def gold_room():
    print("황금으로 가득 찬 방입니다. 얼마나 가져갈까요?")

    choice = input("> ")
    if "0" in choice or "1" in choice:      # 입력 값이 x0, x0, 1x, x1이면 True
        number = int(choice)                # int()의 동작 방식은?
    else:
        death(" 죽었습니다. 인간이여, 숫자 쓰는 법부터 배우세요.")

    if number < 50:
        print("좋아, 당신이 이겼습니다.")
        exit(0)
    else:
        death("욕심쟁이!!")
#[2]함수 bear_room()
def bear_room():
    print("여기에는 곰이 한 마리 있습니다.")
    print("곰은 꿀을 잔뜩 들고 있습니다.")
    print("뚱뚱한 곰은 다른 쪽 문 앞에 있습니다.")
    print("어떻게 곰을 움직이시겠습니까?")
    bear_move = False

    while True:
        choice = input("> ")
        if choice == "steal":
            death("죽었습니다. 곰이 당신을 쳐다보더니 목이 떨어져라 따귀를 날립니다.")
        elif choice == "laugh" and not bear_move:
            print("곰이 문에서 비켜섰습니다.")
            print("이제 나갈 수 있습니다.")
            bear_move = True

        elif choice == "laugh" and bear_move:
            death("죽었습니다. 곰이 머리 끝까지 열받아 당신의 다리를 씹어먹습니다.")
        elif choice == "open" and bear_move:
            gold_room()                     # ==> [3]함수 gold_room()호출
        else:
            print("무슨 말을 하는 건지 모르겠네요.")

#[3]함수 kant_room()
def kant_room():
    print("여기에서는 칸트를 봅니다.")
    print("그 분이, 그것이, 아니 뭐든 간에 당신을 쳐다보고 당신은 미쳐갑니다.")

    choice = input("> ")

    if "run" in choice:
        start()
    elif "eat" in choice:
        death("죽었습니다. 맛은 좋네요.")
    else:
        kant_room()

def death(reason):
    print(reason, "죽었어요.잘 했어요!")
    exit(0)

#[1] 함수 start()
def start():
    print("어두운 방에 있습니다.")
    print("오른쪽과 왼쪽에는 문이 있습니다.")
    print("어느 쪽을 고를까요?: left, right, nothing")

    choice = input("> ")
#choice "letf" or "right" or "etc"
    if choice == "left":
        bear_room()                         # ==> [2]함수 bear_room() 호출
    elif choice == "right":
        kant_room()                         # ==> [3]함수 kant_root() 호출
    else:
        death("문 주의에서 맴돌기만 하다 굶어 죽었습니다.")
#------------------**이 코드는 start()함수를 호출하면서 시작한다.**----------------------
start()
