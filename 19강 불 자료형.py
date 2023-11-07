#불만들기 : 비교 연산자 6가지

10 == 20 # 두 대상이 같다  =는 할당 연산자이고 == 는 비교 연산자이다
10 != 20 # 두 대상이 다르다
10 < 20
10 <= 20
10 > 20
10 >= 20

print(10 < 20 < 30)
x = 20
print(10 < x < 30)

#불 연산하기 : 논리 연산자
#단항 연산자 not
print(not True) # False
print(not False) # True
print("1020".isalnum())
print(not"1020".isalnum())

#이항 연산자 and << ~이면서
print(True and True)
print(True and False)
print(False and True)
print(False and False)   # 둘다 True일때만 결과가 True로 나온다
#ex) 어린이날 호텔에서 "호텔 멤버쉽 회원"이면서 "12세 이하의 어린이 동반"인 경우 선물을 준다
print("is멤버쉽() and is어린이동반()")
#ex) 배달 음식 어플리케이션에서 "주문한 음식 가격 2만원 이상"이면서 "거리 500m 이하의 경우" 배달무료
print("(가격>=20000) and (거리 <= 500)")
print()

#이항 연산자 or
print(True or True)
print(True or False)
print(False or True)
print(False or False) # 둘 중 하나만 True이면 결과가 True로 나온다

#ex) 쇼핑몰에서 "우리카드"와 "신한카드"를 사용하면 무이자 6개월이다
print("is(우리카드() or is신한카드()")