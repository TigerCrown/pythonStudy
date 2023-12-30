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

#간단한 외관
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