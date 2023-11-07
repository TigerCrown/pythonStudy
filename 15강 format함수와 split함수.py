#format 함수 개요 : 복잡한 코드를 줄이고 간단하게 코딩가능하도록 하는 것. "{}" << format함수의 틀
a = 52
b = 273

#52 + 273 = {더한값}
#print(a, "+", b, "=", a + b) << 뛰어쓰기 있음
print("{} + {} = {}".format(a, b, a+b))
#52+273={더한값}

#a + "+" + b + "=" + (a + b)
#c = str(a) + "+" + str(b) + "=" + str(a + b)
#print(c)    << 뛰어쓰기 없음
print("{}+{}={}".format(a, b, a+b))

print("{}".format(10)) #format함수는 자동적으로 괄호안의 내용을 문자열로 변환한 뒤에 틀 안에 집어 넣는다.
print("{}년 {}월 {}일".format(2023, 7, 15))

#TEST 1
print("#테스트1")
print("{}".format(10, 20, 30))    #<<<<앞의 format함수 틀은 1개이고 숫자는 여러개더라도 실행 됨
#TEST 2
print("#테스트2")
print("{} {}".format(10))  #<<<< 실행 안됨