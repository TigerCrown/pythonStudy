#재귀함수 : 자기자신을 호출하는 함수

#팩토리얼 연산(반복문으로 구현, 재귀함수로 구현)
# n! = n * (n-1) * (n-2) * .... * 1

#반복문 팩토리얼 구현

def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

#재귀함수 팩토리얼 구현(수학의 수열의 점화식 사용 > 이웃한 항의 관계를 통해 수열을 나타 냄)
# 1! = 1
# (n이 2 이상의 수일 때) n! = n * (n-1)!
def factorial(n):
    # 1! = 1
    if n == 1:
        return 1
    #(n이 2 이상의 수일때) n! = n * (n-1)!
    elif n >= 2:
        return n * factorial(n - 1)
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))