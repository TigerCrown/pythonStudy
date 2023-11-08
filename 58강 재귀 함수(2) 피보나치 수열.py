# a_1 = 1
# a_2 = 1
# a_n = a_{n-1} + a_{n-2}
# a_3 = 1 + 1 = 2
# a_4 = a_3 + a_2 = 2 + 1 = 3
# a_5 = a_4 + a_3 = 3 + 2 = 5
# ...

# memo = {}
memo = {1:1, 2:1}
# < 이 코드를 쓰면 아래 코드 조차 필요 없음
# if n == 1:
#     return 1
#     # a_2 = 1
# elif n == 2:
#     return 1

def f(n):
    if n in memo:
        return memo[n]
    # #a_1 = 1
    # if n == 1:
    #     return 1
    # #a_2 = 1
    # elif n == 2:
    #     return 1
    # #a_n = a_{n-1} + a_{n-2}
    else:
        temp = f(n - 1) + f(n - 2)
        memo[n] = temp
        return temp
print(f(3))
print(f(4))
print(f(5))
print(memo)
print(f(50))