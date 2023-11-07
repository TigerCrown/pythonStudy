#while 반복문 > for 반복문보다 범용적으로 사용할 수 있는 반복문이다
#C, C++, Java 등의 프로그램밍 언어는 for 반복문으로 할 수 있는 일을
#while 반복문으로도 구현할 수 있고 while 반복문으로 할 수 있는 일을 for 반복문으로도
#구현할 수 있다.
#하지만 파이썬은 for 반복문으로 할 수 있는 일을 while 반복문으로도 구현할 수 있지만
#그에 반대는 굉장히 힘들거나 불가능할 수 있다.
#(e.g. 무한 반복문을 for반복문으로 구현하려면 이상한 코드를 사용해야 한다)

#while True:
    #복합구문 / 조건이 참이라면 반복
    #print(".")
# i = 0
# while i < 10:
#     print(f"{i}번째 반복입니다.")
#     i += 1
#
# #while 반복문 : 상태 기반 반복
# for z in range(0,10):
#     print(f"{z}번째 반복입니다.")
    
#for 반복문으로 구현할 수 없는 것들
# 빵 10개를 먹어라라는 것은 for 반복문으로 구현가능하지만,
# 빵이 모두 사라질때까지 먹어라 내일 몇시까지 먹어라와 같은 개수로서 반복문을 돌리는 것이 아니면
# 반복문을 사용할 수 없다.
a = [1, 2, 1, 2]
value = 2

while value in a:
    print(a)
    a.remove(value)
    print(a)

print(a)

#while 반복문 : 시간 기반 반복
#1970년 1월 1일 0시 0분 0초
# import time
# print(time.time())

import time
시작시간 = time.time()
현재시간 = time.time()
while 현재시간 < 시작시간 + 3:
    print(currenttime, 시작시간 + 3)
    currenttime = time.time()