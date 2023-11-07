#입력
raw = input("정수 입력")
l = raw[-1]
#짝수 또는 홀수
#if l == "0" or l == "2" or l == "4" or l == "6" or l == "8":
    #print("짝수")
if l in "02468":
    print("짝수입니다")
#짝수 : 02468 홀수 : 13579
#if l == "1" or l == "3" or l == "5" or l == "7" or l == "9":
    #print("홀수")
if l in "13579":
    print("홀수입니다")

#자주하는 실수
#if l == "0" or "2" or "4" or "6" or "8":
    #print("짝수")   << 이런 코드는 안된다

#짝수 홀수 구분(2) : 컴퓨터 기준
raw = input("정수 입력")
raw = int(raw)
if raw % 2 == 0:
    print("짝수")
if raw % 2 == 1:
    print("홀수")