학점 = float(input(">학점 입력: "))
if 학점 == 4.5:
    print("a+")
if 4.2 <= 학점 < 4.5:
    print("great student")
if 3.5 <= 학점 < 4.2:
    print("normal")
if 2.8 <= 학점 < 3.5:
    print("bad student")
if 2.3 <= 학점 < 2.8:
    print("fucking trash")
if 학점 < 2.3:
    print("are u human?")
#여기서 elif 구문을 사용하게 되면 도달하기 위하여 이미 위에 있는 조건들이 거짓이 나와야 한다.
#따라서 nomal을 도달하기 위해서는 4.5점이 아니어야하고 4.2~4.5점이 아니어야 한다.
#따라서 4.2점보다 작다라는 것을 검사할 필요가 없는 거다.
if 학점 == 4.5:
    print("a+")
elif 4.2 <= 학점:
    print("great student")
elif 3.5 <= 학점:
    print("normal")
elif 2.8 <= 학점:
    print("bad student")
elif 2.3 <= 학점:
    print("fucking trash")
else :
    print("are u human?")

x=2
y=10

if x > 4:
    if y > 2:
        print(x * y)
else:
    print(x + y)

#다음 중첩 조건문에 논리 연산자를 적용해 하나의 if 조건문으로 만들어 주세요.
#if x > 10:
    #if x < 20:
        #print("조건에 맞습니다.")
if(x>10) and (x < 20):
    print("조건에 맞습니다.")

#사용자에게 태어난 연도를 입력받아 띠를 출력하는 프로그램을 작성하라.
#작성 시 입력 받은 연도를 12로 나눈 나머지를 사용합니다.
#나머지가 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11일 때 각각 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양띠입니다.
str_input = input("태어난 해를 입력하라")
birth_year = int(str_input)

if birth_year % 12 == 0:
    print("원숭이 띠")
if birth_year % 12 == 1:
    print("닭 띠")
if birth_year % 12 == 2:
    print("개 띠")
if birth_year % 12 == 3:
    print("돼지 띠")
if birth_year % 12 == 4:
    print("쥐 띠")
if birth_year % 12 == 5:
    print("소 띠")
if birth_year % 12 == 6:
    print("범 띠")
if birth_year % 12 == 7:
    print("토끼 띠")
if birth_year % 12 == 8:
    print("용 띠")
if birth_year % 12 == 9:
    print("뱀 띠")
if birth_year % 12 == 10:
    print("말 띠")
if birth_year % 12 == 11:
    print("양 띠")
#if를 elif로 변경해도 가능하다.

#또는 split 코드를 실행해 봐라
print("원숭이,닭,개,돼지,쥐,소,범,토끼,용,뱀,말,양" .split(",")[birth_year % 12], "띠입니다")