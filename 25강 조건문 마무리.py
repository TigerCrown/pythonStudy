#int 다른 자료형을 정수로 변환
#float 다른 자료형을 부동소수점으로 변환
#str 다른 자료형을 문자열로 변환

#bool 다른 자료형을 불로 변환 >> None, 숫자 0, 빈 컨테이너 등 >> False, 숫자 0(0.0), 빈 문자열 > False
#bool 사용자로부터 입력, 입력을 그대로 출력

print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(1))
print(bool(-1))
print(bool("False"))

#사용자가 아무것도 입력하지 않았다면 : "프로그램을 다시 실행해주세요"

i = input("입력하라")
i = i.strip()
#  위와 같은 코드 i = input(">입력해주세요").strip()

#if i == "":
    #프로그램의 보완적인 기능
    #print("프로그램 재시작 요망")
#else:
    #프로그램의 주요 기능
    #print("입력한 내용:", i)
#위 코드를 !=와 if not (i == ""):로 if와 else구문을 변경할 수 있다.
if  i !="":
    #프로그램의 주요기능
    print("입력한 내용:", i)
else:
    # 프로그램의 보완적인 기능
     print("프로그램 재시작 요망")

#또는

if i == "":
    print("프로그램 재시작 요망")
    exit()
print("입력한 내용:", i)

if i:
    #빈 문자열이 아닐떄
    pass
else:
    print("프로그램 재시작 요망")

if i:
    #나중에 작성할 것이다, raise는 강제로 오류를 발생시키는 키워드, Suite(복합구문)
    raise NotImplementedError
else:
    print("프로그램 재시작 요망")

