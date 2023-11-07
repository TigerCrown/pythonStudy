#다음 중 enumerate()함수와 items()함수의 사용법으로 올바른 것은?
# enumerate()
#
# #items는 딕셔너리에 그냥 나오질 않는다
# a = {}
# a.items()

#2진수, 8진수, 16진수로 변환하는 코드는 많이 사용됩니다. 다음과 같은 형태로 10진수를 변환할 수 있습니다.
#10진수와 2진수 변환(변환시 따옴표로 둘러싸여 있다면 문자열 자료형이다.)
# "{:b}".format(10) = 1010
# int("1010", 2) = 10
f"{10:b}"
print(f"{10:b}")

f"{10:o}"
print(f"{10:o}")

f"{10:x}"
print(f"{10:x}")

int("1010",2)
print(int("1010",2))

int("12",8)
print(int("12",8))

int("a",16)
print(int("a",16))

# 1~100 사이에 있는 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고,
# 그 숫자들의 합을 구하는 코드를 만들어 보아라!!
# 실행 결과 2 : 10, 5 : 101, 6 : 110, 11 : 1011, 62 : 111110, 95 : 1011111 합계:539

#1~100 사이에 있는 숫자를 2진법으로 변환
# 1단계
for i in range(1, 100 + 1):
    print(f"{i:b}")
# 2단계
for i in range(1, 100 + 1):
    변환 = f"{i:b}"
    if 변환.count("0") == 1:
     print(변환)

# 3단계
a = []
for i in range(1, 100 + 1):
    변환 = f"{i:b}"
    if 변환.count("0") == 1:
     print(변환)
     a.append(i)
print(a)
print(sum(a))

# 4단계
a = []
for i in range(1, 100 + 1):
    변환 = f"{i:b}"
    if 변환.count("0") == 1:
     print(i, ":", 변환)
     a.append(i)
print("합계:", sum(a))

#리스트 내포를 사용한 코드입니다.
a = [i for i in range(1,100+1)
     if f"{i:b}".count("0")==1]
for i in a:
    print(i, ":", f"{i:b}")
print("★합계:",sum(a))