#변수 : 값에 붙이는 이름

##변수를 만드는 방법 : 식별자 = 값 ex) pi = 3.141592

###변수를 사용하는 방법 : print(파이)

pi =  3.141592
print(pi)
print(pi+10)

####변수와 관련된 용어 : 정의(defined)(선언) : 변수를 만드는 행위
#                      할당(assign) : 변수에 값을 넣는 행위
#                      참조(reference) : 변수 안에 있는 값을 사용하는 행위

#####정의와 할당

pi = 3.14159265
r = 10
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2*pi*r)
print("원의 넓이 =", pi*r*r)

#####복합 대입 연산자
#pi = 3.141592
#식별자 = 값[리터럴]
#pi = pi / #pi = pi + 1
a = 0
print(a)
a += 1 #a = a + 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)   # 계속 이렇게 쓰기 귀찮으니 복합대입 연산자를 만듬
#-----------------------------------------
a = 0
print(a)
a += 1
print(a)
a -= 1
print(a)
a += 1
print(a)
a -= 1
print(a)

string = "안녕하세요"
string += "!"
string += "!S"
print(string)
#####형태
#[변수] [연산자] = [값]  : 변수에 값을 연산자해서 다시 변수에 넣은다