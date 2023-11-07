#범위는 특정한 범위 내부의 정수들을 나열하는 자료형

#(1) range(A), 0부터 A까지의 정수를 범위로 나열, A는 포함하지 않음
print(range(5))
print(list(range(5)))
print(list(range(6)))
#(2) range(A, B) A부터 B까지의 정수를 범위로 나열, B는 포함하지 않음
print(list(range(10, 15)))
print(list(range(10, 20)))
#(3) range(A, B, C) A부터 B까지의 정수를 범위로 나열, B는 포함하지 않음, C만큼씩 건너뛰면서 범위 생성
print(list(range(0, 10, 2)))
print(list(range(0, 10, 3)))

#범위로 반복문을 사용한때
for i   in range(10):
    print(f"{i}번째입니다!")

for i in range(0, 11 + 1):
    print(f"{i}번째입니다!")
    
#범위 반복문 구분
#1개 넣는 경우, 특정 횟수만큼 반복
for i in  range(5):
    print("반복테스트")
#2개 넣는 경우, 반복 변수를 사용
for i in  range(0, 3):
    print(f"{i}번째입니다!!")
#3개 넣는 경우, 반대로 반복하는 경우
for i in  range(10, -1, -1):
    print(f"{i}번째입니다!!")

#반복 변수 _ 식별자
for _ in  range(3):
    print("식별자테스트")