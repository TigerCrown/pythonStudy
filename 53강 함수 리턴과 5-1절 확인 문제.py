#서브루틴, 프로시저, 함수 > 수학에서 빌려온 용어
def f(x):
    return x + 1 # return을 쓴 이유는 x = 1 / x + 1이라는 값이 들어오면 값을 들고 돌아가라!
#return을 만난 후 자신의 위치로 돌아와서 값을 대치하게 된다.
#return 뒤에 x+1 같은 것이 없으면 return none이 된다.
# def f(x):
#     return
print(f(1))
print(f(2))
# f(x) = x + 1
# f(1) = 2
# f(2) = 3



def 함수(매개변수):
    변수 = "초기화"
    # 여러가지 처리
    # 여러가지 처리
    # 여러가지 처리
    return 변수

print(함수(1)) # 함수(1) = 변수
def sum_all(start, end):
    # 항등원으로 초기화
    output=0
    for i in range(start, end + 1):
        output += i    # output = output + i
    return output
print(sum_all(1, 10))
print(sum_all(1, 100))

def sum_all(start, end):
    # 항등원으로 초기화
    output=0
    for i in range(start, end + 2):
        output += i    # output = output + i
    print(output)
sum_all(1, 10)
sum_all(1, 100)
#return output과 print(sum~ 이 아니라 sum_all(1, 10)으로 해도 실행은 된다.
#sum_all() 함수일 때와 값을 계산하는 부분 + 출력하는 부분인 경우
#파일에 결과를 출력하고 네트워크 통신으로 결과를 전송하는 경우
#값을 계산하는 부분만 따로 쓰여지는 것이 훨씬 더 간편하게 사용할 수 있다.
#활용범위(return)와 출력(print의 차이가 있을 뿐이다.

#확인문제 1번
# 1. 다음과 같이 방정식을 파이썬 함수로 만들어 보라
# ex) f(x)=x
def f(x):
    return x
print(f(10))
# ①f(x) = 2x + 1
def f(x):
    return 2 * x + 1
print(f(10))

# ②g(x) = x^2 + 2x + 1
def g(x):
    return x ** 2 + 2 * x + 1
print(f(10))

#확인문제 2
#다음 빈칸을 채워 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수를 만들어 봐라
def mul(*values):
      output = 1  #곱셈의 항등원은 1
      for i in values:
          output *= i
      return output
#함수를 호출합니다. 실행결과 3150
print(mul(5, 7, 9, 10))

#확인문제3
#다음 중 오류가 발생하는 코드를 고르세요.
#답 1.
def function(*values, valueA, valueB):
    pass
function(1, 2, 3, 4, 5)
# 답 : function(1, 2, 3, 4, 5, valueA=10, valueB=20)

#2.
def function(*values, valueA=10, valueB=20):
    pass
function(1, 2, 3, 4, 5)

#3.
def function(valueA, valueB, *values):
    pass
function(1, 2, 3, 4, 5)