#a = 10
# + 연산자 : 피연사자를 바꾸지 않음(비파괴적이다)
#a + 10
#a + 20
#a + 30
#a + a
#a + 10
#a - 10
#a * 10
#a / 10
#a % 10
#a // 10
#a ** 10

# = 연산자 : 피 연산자를 바꿈!
#20이 되기 위해서는 a = a + 10 << 이 코드여야 한다.(파괴적이다)
a = 20
#a = a + 10

#a = 30
#a = a + 10

#a = a + 10
a = a % 10
#a // 10
#a ** 10
print(a)

#대학교 중간고사 시험문제
a = "안 녕 하 세 요"
#a.split()
a = a.split()
print(a)

#upper, lower 함수 << 대문자 소문자가 존재하기 때문에 한글은 적용이 안됨, 모두 비파괴적 함수임 그래서 a = a.upper() 식을 이용해야 함
a = "F u C k i N g 안녕하세요"
#a = a.upper() #소문자를 대문자로 변경
#a.lower() #대문자를 소문자로 변경
print(a)
print(a. upper())
print(a. lower())