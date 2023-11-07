#break 키워드 : 반복문 전체를 벗어날 때 사용하는 구문
i = 0
while True:
    print(f"{i}번째 반복입니다.")
    i += 1

    a = input(">종료하시겠습니까?(y/n):")
    if  a   in  ["y", "Y"]:
        print("반복문을 종료합니다.")
        break
#continue 키워드 : 현재 반복을 넘어갈 때 사용하는 구분
numbers = [5, 15, 6, 20, 7, 25]
for i in numbers:
    #if i >= 10:
    #   print(i)
    if i < 10:
        continue
# 10이하인 경우에는 continue키워드가 실행되어 현재 반복을 건너띄고 다음 반복으로 넘어가게 된다.
# 그리고 이 경우가 아닌 경우에는 i를 출력하게 만들어 본다면,
    print(i)
#c c+ java와 같은 언어에서는 continue키워드는 사용되지 않지만
# 파이썬에서는 continue 키워드를 쓰면서 들여쓰기를 하나 줄일 수 있다.

#문제1
# 코드가 여러개 나울 수 있는 경우, 가장 간단한 형태를 넣어보라
# 예를들어 range(5) range(0,5) range(0,5,1)은 모두 같은 값을 나타내는데
# 이때는 range(5)로 넣어봐라
#   코드      나타내는 값
# range(5) [0,1,2,3,4]
# range(4,6) [         ]
# range(7, 0, -1) [        ]
# range(3,8) [3,4,5,6,7]
#ex range() [3,6,9]

#답 list(range(4,6)) [4,5]
# list(range(7,0,-1)) [7,6,5,4,3,2,1]
# list(range(3,10,3)) [3,6,9]