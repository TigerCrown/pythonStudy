# 1. 리스트에 적용할 수 있는 함수 max()함수와 min()함수
a = [52, 273, 32, 103, 57]
print(max(a))
print(min(a))
print(max(52, 273, 32, 103, 57))
print(min(52, 273, 32, 103, 57))

print(max(*a))
print(min(*a))
print(sum(a))

# 2. reversed()함수(함수형 프로그래밍 이념에 따라 탄생됨)
# for i in reversed(range(0, 10)):
#     print(i)
# 위와 같은 값이 나오는 다른 방식임
# a = range(0, 10)
# for i in reversed(a):
#     print(i)

# reversed()함수의 결과는 한번만 사용 가능!!
a = reversed(range(0, 10))
for i in a:
    print(i)
for i in a:
    print(i)

# 3. enumerate함수
fruits = ["바나나", "사과", "포도"]
for fruit in fruits:
    print(fruit)
#리스트의 몇번째 요소인지 함께 출력하고 싶다면 3가지 방식이 있다
fruits = ["바나나", "사과", "포도"]
i = 0
for fruit in fruits:
    print(f"{i}: {fruit}")
    i += 1
#아래의 구문도 reversed함수처럼 일회용임-------------
a = enumerate(fruits)
print(list(a))
#-------------
for fruit in  enumerate(fruits):
    print(fruit[0], fruit[1])
for i, fruit in  enumerate(fruits):
    print(i, fruit)

# 4. items()함수(객체 지향 프로그래밍 이념에 따라 탄생)
a = {"이름": "바나나",
     "가격": 1500,
     "원산지": "말레이시아"}
print(a.items())
for 반복변수 in a.items():
    print(반복변수[0], 반복변수[1])
for 키, 값 in a.items():
        print(키, 값)