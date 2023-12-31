#튜플 = () 튜플은 외관이 간단하고 요소를 변경할 수 없는 장점이 있다. / 리스트 = []
a = (1,2,3)
print(a)
# 요소의 접근
print(a[0])
print(a[1])
print(a[2])

a = (1,2,3)
b = (1,)
print(b, type(b))

#튜플의 괄호 생략
a = 1,2,3
b = 1,
print(a)
print(b)

#튜플과 리스트의 차이
a = [1,2,3]
a[1] = 5
print(a)   #<<<< 리스트

# a = (1,2,3)
# a[1] = 5
# print(a)   #<<<< 튜플

#1. 간단한 외관
#(1)
[a, b] = [10, 20]
(a, b) = (10, 20) #or
(a, b) = 10, 20
print(a, b)

#(2)
def a():
    return (100, 200, 300)
(b,c,d) = a()
# (b,c,d) = (10, 20, 30)
print(b,c,d)

#(3)
#튜플과 함수 리턴 예시 : enumerate
A = ["바나나", "사과", "고구마", "감자"]

i = 0
for item in A:
    print(i, item)
    i += 1

for item in enumerate(A):
    print(item)

for i, item in enumerate(A):
    print(i,item)

#(4)
#튜플과 함수 리턴 예시(1) : item()
B = {"이름": "별",
     "생일": (2024, 1, 1)}
for key in B.items():
    print(key)
for key, value in B.items():
    print(key)

#2. 변경할 수 없는 요소
#뮤터블과 이뮤터블

#(1)뮤터블 : 변수에 넣었을 때 스택에 있는 값을 변경하지 않아도 값을 변경할 수 있는 자료
#           ex) 리스트, 딕셔너리
#(2)이뮤터블 : 변수에 넣었을 때 스택에 있는 값을 변경해야만 값을 변경할 수 있는 자료
a = 10
a = 20 # 숫자들은 이뮤터블
b = True
b = False #불
c = "안녕하세요" #문자열도 이뮤터블
c = "안녕히가세요"
a = {(10, 20): 10,
     (2023, 12, 25): "크리스마스",
     (2024, 1, 1): "새해"}
print(a) #튜플(튜플은 이뮤터블임)과 딕셔너리