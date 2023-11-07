#a의 100번째 항
n = 100
a_n = 2 * n-1
print(a_n)

for n in  range(1, 10 +1):
    a_n = 2 * n -1
print(a_n)

# 1번째 항에서 10번째 항의 리스트
a = [None]
for n in range(1, 10 + 1):
    a_n = 2 * n - 1
    a.append(a_n)
#print(a)

#점화식 : 이전 항을 기반으로 다음 항을 만드는 방법
# an = an -1 + 2이다. / a1 = 1
a = [None]
for n in range(1, 10 +1):
    if  n == 1:
        a_n = 1
    else:
        a_n= a[n-1] + 2
    a.append(a_n)
print(a)
#위 리스트에서 특정 길이의 리스트를 만들때는, 구현해야 하는 항이 많을때는
#파이썬의 append함수로 리스트를 늘리는 것은 많이 느려서 처음부터 큰 리스트를 만들면 된다.

#리스트 반복 연사자로 큰 리스트 구현하기
N = 10
a = [None] * (N + 1)
for n in range(1, N + 1):
    if n == 1:
        a[1] = 1
    else:
        a[n] = a[n-1] + 2
print(a)

#동적계획법 : 반복문으로 이전 항의 값을 기반으로 다음 항의 값을 구해내는 방법
N = 10
a = [None] * (N + 1)
for n in range(1, N + 1):
    if n == 1 or n == 2:
        a[n] = 1
    else:
        a[n] = a[n-1] + a[n-2]
print(a)