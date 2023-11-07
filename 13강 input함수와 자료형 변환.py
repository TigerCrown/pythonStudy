#input("문자열") 함수
##input()함수의 흐름은 첫째, 프롬프트(입력을 요청하는 문자열)를 출력
###둘째, 사용자로부터 입력을 받을 수 있게 일시 정지
####셋째, 입력을 받으면 계속 진행
#####input()함수 : 입력을 받음 / int() : 정수로 변환 / float()함수 : 부동소수점으로 변환 / str()함수 : 문자열로 변환


#input("입력해주세요: ")
#input(">>>")

#print(input("입력해주세요: "))
#a = input(">>>> ")
#print(a)

#a = input(">>>")
#print(a)
#print(type(a))

#문자열 >> 숫자변환
int("52") #정수로 변환할 수 있게 해줌   ex) int("hello") = X
float("52.273") #부동소수점으로 변환할 수 있게 해줌
#a = input("숫자1: ")
#b = input("숫자2: ")
#print(a + b)

a = int("52")
b = int("10")
print(a + b)

#숫자 > 문자열변환
c = str(a)

print(a+b)
print(c, type(c))