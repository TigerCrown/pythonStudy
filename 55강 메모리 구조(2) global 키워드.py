# global 함수는 외부에 있는 함수를 쓰고 싶을때 쓰임.
# global 키워드를 사용하면, 함수 스택의 새로운 변수를 만들지 않는다!

#외부 위치에서 a,b라는 변수를 생성
a=10
b=[1,2,3,4]
#파이썬에서 변수를 잠조할 땐
#자신과 가까운 스택부터 위로 올라가면서 참조
def function():
    global a, b
    a=20
    b=[5, 6, 7, 8]
    print(a)
    print(b)
function()
print(a)
print(b)


#<오류코드>
# a=10
# b=[1,2,3,4]
# def function():
#     # 함수는 실행되기 전에, 내부에서 생성되는 모든 변수에 대한 정보를 미리 파악
#     # "a, b"는 함수 스택 내부에 있을 것이다!
#     print(a)
#     print(b)
#     # 함수 스택 내부에 새로운 변수를 만들겠구나! 생각하겠지만 오류가 생성 된다.
#     a=20
#     b=[5, 6, 7, 8]
# function()
# print(a)
# print(b)

#<수정코드>
a=10
b=[1,2,3,4]
def function():
    global a, b
    print(a)
    print(b)
    a=20
    b=[5, 6, 7, 8]
function()
print(a)
print(b)

a=10
b=[1,2,3,4]
def function():
    a = 20
    b = [5,6,7,8] #함수 스택에 새로운 변수를 만듬
    b.extend([5,6,7,8]) #외부 a,b에 영향을 준다.
    print(a)
    print(b)
function()
print(a)
print(b)