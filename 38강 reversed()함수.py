#reversed()함수란 매개변수로 반복 가능한 것을 넣으면
#그것을 뒤집어서 리턴 값이 결과(이터레이터)로 나온다.

#리스트
print(list(reversed([1, 2, 3, 4, 5])))

#범위
print(list(reversed(range(0, 5))))

for i in reversed(range(0, 10)):
    print(i)

#1. 문자열 반복 연산자
height  =   5
for i in range(1, height + 1):
    print("*" * i)

#2. 문자열 반복 연산자 x
N  =  5
for i in range(N):
    #N개의 별을 가로 방향으로 출력하는 반복문
    print("★", end="")
N  =  5
result = ""
for i in range(N):
    #N개의 별을 가로 방향으로 출력하는 반복문
    result += "☆"
    print(result)

#위 1.2번 코드를 합치게 되면 아래 두개의 코드로 만들 수가 있다.
height = 5
for i in range(1, height + 1):
    N = i
    result = ""
    for j in range(N):
        result += "♥"
    print(result)

height = 5
for i in range(1, height + 1):
    result = ""
    for j in range(i):
        result += "♡"
    print(result)

#별로 피라미드 만들기 2가지 공식
height = 5
for i in range(1, height + 1):
    result = ""
    #print("띄어쓰기:", height - i)
    result += " " * (height - i)
    #print("별:", 2 * i -1)
    result += "*" * (2 * i -1)
    #print()
    print(result)

height = 5
for i in range(1, height + 1):
    result = ""
    #result += " " * (height - i)
    for j in range(height - i):
        result += " "
        #result += "*" * (2 * i -1)
    for j in range(2 * i - 1):
      result += "*"
    print(result)