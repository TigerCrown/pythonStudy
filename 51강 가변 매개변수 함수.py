#매개변수가 가변적으로 변하는 함수를 가변 매개변수 함수라 칭한다.
#가변매개변수는 이렇게 만들어진걸 써야하는 상황이 많기때문에 배운다.
print("안")
print("안","녕")
print("안","녕","하")

#리스트를 받는 형태로 구현하기
#print_n_times(횟수, 출력대상, 출력대상.....)
#print_n_times(횟수, [리스트])
def print_n_times(횟수, 리스트):
    print(리스트)
    for i in range(횟수):
        for 요소 in 리스트:
            print(요소)
print_n_times(2, ["안녕", "하세요"])

#가변 매개 변수
def print_n_times(횟수, *리스트):
    print(리스트)
    for i in range(횟수):
        for 요소 in 리스트:
            print(요소)
print_n_times(2, "그래", "안녕")
print_n_times(2, ["그래", "안녕"])

#전개 연산자와 조합하기
a = ["문자열", "목록"]
print_n_times(2, *a)

#주의 사항
def print_n_times(*리스트, 횟수):
    for i in range(횟수):
       for 요소 in 리스트:
            print(요소)
# print_n_times("주의", "사항", 2) #2 횟수까지 리스트로 잡아버림 이럴 땐, 횟수를 따로 잡아줘야함
print_n_times("주의", "사항", 횟수=2)

#정리하자면, 가변 매개 변수를 만들때는 *연산자를 사용한다.