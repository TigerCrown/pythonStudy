# 1. 빈칸을 채워 키와 값으로 이루어진 각 리스트를 조합하여 하나의 딕셔너리를 만들어 보라
# 숫자는 무작위로 입력해도 상관 없다.
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]

character = {}
# character[key_list[0]] = value_list[0]
# character[key_list[1]] = value_list[1]
# character[key_list[2]] = value_list[2]
# character[key_list[3]] = value_list[3]
# 밑에 for 구문과 같은 값이 나온다.
for i in range(0, 4):
    character[key_list[i]] = value_list[i]
print(character)

# 2. 1부터 숫자를 하나씩 증가시키면서 더하는 경우를 생각해 보면, 몇을 더할때 1000을 넘는지 구해보자.
# 그리고 그떄의 값도 출력해 보자. 다음은 10000이 넘는 경우를 구한 예이다.
#1, 1+2 =3, 1+2+3 = 6, 1+2+3+4 = 10 ...
limit = 10000
i = 1
sum_value = 0
while sum_value <= limit:
    sum_value += i
    i += 1
print(f"{i-1}를 더할때 {limit}을 넘으면 그때의 값은 {sum_value}입니다.")
#sum은 파이썬 내부에서 사용하는 식별자이므로 sum_value라는 변수의 이름을 사용한다

# 3. 최대값 구하기
a = [27,53,103,273,32]

현재최대값 = a[0]
for i in a:
  if 현재최대값 < i:
      현재최대값 = i

print(현재최대값)
#응용 예시
a = []
for i in range(1, 99+1):
    j = 100 -i
    a.append(i * j)

현재최대값 = a[0]
for i in a:
  if 현재최대값 < i:
      현재최대값 = i
print(현재최대값)
#-----------------------
a = []
for i in range(1, 99+1):
    j = 100 -i
    a.append([i, j, i * j])
print(a)
#-----------------------
최대리스트 = a[0]
현재최대값 = 최대리스트[2]
for i in a:
  if 현재최대값 < i[2]:
      최대리스트 = i
      현재최대값 = 최대리스트[2]
print(최대리스트)
#-----------------------
현재최대값 = 0
a = 0
b = 0
for i in range(1, 99 + 1):
    j = 100 - i
    if 현재최대값 < i * j:
      # 어떤것을 곱한것인지 알고 싶을때는 a = i / b = j 입력
      a = i
      b = j
      현재최대값 = i * j
#어떤것을 곱한것인지 알고 싶을때는
print(a)
print(b)
print(현재최대값)
print("최대가 되는 경우: {} * {} = {}".format(a, b, 현재최대값))


# 최소값 구하기
a = [27,53,103,273,32]

현재최대값 = a[0]
for i in a:
  if 현재최대값 > i:
      현재최대값 = i

print(현재최대값)