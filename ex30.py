사람 = 30
차 = 40
트럭 = 15

if 차 > 사람:
    print("차를 타야 해요.")
elif 차 < 사람:
    print("차를 안 타야 해요.")
else:
    print("결정할 수 없어요.")

if 트럭 > 차:
    print("트럭이 너무 많아요.")
elif 트럭 < 차:
    print("트럭을 탈 수도 있어요")
else:
    print("아직도 결정할 수 없어요.")

if 사람 > 트럭:
    print("좋아요 트럭을 탑시다.")
else:
    print("좋아요 그럼 집에 있죠.")

if 사람 < 트럭 or 트럭 > 차:    #if 문장이 참이면 아래 문장 출력
    print("사람이 트럭보다 많거나 트럭이 차보다 적네요.")
elif 사람 == 트럭 and 트럭 < 차: #if 문장이 거짓이고 elif가 참이면 pass1 출력
    print("pass1")
else:                       #if와 elif 모두 참이 아닐 경우 pass2 출력
    print("pass2")
