memo = {1: 1, 2: 1}
# 코드의 작성 방법은 당연한 것이 아니라 하나의 유행일 뿐이다. 새로운 유행에 갈아타라.
# 방법 1
def f(n):
    if n in memo:
        return memo[n]
    else:
        temp = f(n - 1) + f(n - 2)
        memo[n] = temp
        return temp
print(f(50))

# 방법 2
def f(n):
    if n in memo:
        return memo[n]
    temp = f(n - 1) + f(n - 2)
    memo[n] = temp
    return temp
print(f(50))

# 방법 3
def f(n):
    if n in memo:
       return memo[n] # (1)
    else:
       temp = f(n - 1) + f(n - 2)
       memo[n] = temp
       return temp # (2)
print(f(50))

#문제 리스트 평탄화하는 재귀 함수 만들기
#리스트 평탄화는 중첩된 리스트가 있을 때 중첩을 모두 제거하고 풀어서 1차원 리스트로 만드는 것을 의미한다.
#그런데 다음과 같이 세번 중첩된 리스트를 평탄화하려면 어떻게 해야 하나?
def flatten(data):
    output = []
    for item in data:
        if type(item) == list: #다른 처리
            pass # or output.extend(flatten(item))
        else:
            output.append(item)#코드 작성
    return output
data = [[1,2,3], [4,[5,6]], 7, [8,9]]
print(flatten(data)) #[1,2,3,4,5,6,7,8,9]
#일반적으로 2차원 리스트 평탄화까지는 쉽지만, 몇 차원까지 중첩될지 정해지지 않은 리스트를 평탄화하는
#문제는 조금 어렵다. 우선 리스트 하나를 입력 받아 이를 평탄화해서 리턴하는 함수를 만들자.