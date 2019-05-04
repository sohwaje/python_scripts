n = "one two three four five six"

print("아직 목록에 10개가 들어있지 않으니 한 번 고쳐봅시다.")

thing = n.split(' ')                            # n 리스트의 요소들을 ''로 구분
other_thing = ["seven", "eight", "nine", "ten",
                        "eleven", "twelve", "thirteen"]

while len(thing) !=10:                          # thing의 개수가 10개가 될 때까지 while문은 반복된다.
    next_one = other_thing.pop()                # other_thing에서 1개의 요소를 잘라낸다.
    print("추가: ", next_one)                    # 잘라낸 요소를 출력한다.
    thing.append(next_one)                      # 잘래낸 1개의 요소를 thing 리스트에 추가한다.
    print(f"이제 {len(thing)} 항목이 있습니다.")     # 요소가 추가된 thing의 전체 개수를 출력한다.


print(thing)                                    # thing 리스트 전체를 출력한다.
print(thing[1])                                 # thing 리스트의 1번째 요소를 출력한다.
print(thing[-1])                                # thing 리스트의 맨 마지막 요소를 출력한다.
print(thing.pop())                              # pop()은 thing 리스트의 맨 마지막 요소를 뺀 나머지를 출력한다.
print('|'.join(thing))                          # thing 리스트의 각각의 문자열 사이에 공백(|)을 삽입한다.
print('#'.join(thing[3:5]))                     # thing 리스트에서 3번째에서 4번째 요소 사이에 #를 삽입한다.
