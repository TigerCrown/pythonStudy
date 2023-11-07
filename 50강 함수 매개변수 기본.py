#어떤 코드를 하나로 묶어서 변수에 저장하고 싶다면,
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
print_3_times()

#매개변수 : 함수의 괄호 안에 넣는 변수
#parameter : 함수 정의 떄 넣은 변수, 아래의 문자열
#argument : 함수 호출 때 넣은 값, 아래의 "안녕"
def print_3_times(문자열):
    print(문자열)
    print(문자열)
    print(문자열)
print_3_times("안녕")

def print_3_times(문자열, 횟수):
    for i in range(횟수):
        print(문자열)


print_3_times("안녕","하루")
# print_3_times("안녕",3)
print_3_times("하세요",3)

#매개변수와 관련된 오류(1) : parameter가 2개인데 argument를 3개를 넣었을때의 오류
#매개변수와 관련된 오류(2) : argument의 횟수부분에 문자열을 넣었을때의 오류

#함수는 설계하는 사람과 사용하는 사람이 있다. 설계하는 사람은 함수의 설명서(문서)와 예외처리를 잘 해야한다.
def print_3_times(문자열, 횟수):
    if type(문자열) != str:
        print("첫 번째 매개변수는 문자열을 입력해야 합니다!")
    if type(횟수) != int:
        print("두 번째 매개변수는 정수를 입력해야 합니다!")
        for i in range(횟수):
         print(문자열)
print_3_times("안녕", 3)
print_3_times("안녕", "하루")