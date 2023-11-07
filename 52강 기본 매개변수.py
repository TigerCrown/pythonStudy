#기본 매개변수
def test(a=10, b=20): #b라는 값을 지정하려면 반드시 a의 값을 대입해야하는 상황이 오기 때문에
    # 기본 매개변수는 다른 매개변수보다도 뒤에 와야함
    print(a)
test()
test(20)
test(a = 30)
test()
test(b = 30)

#키워드 매개변수 기본 매개변수
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times(2, "문자열", "안녕하세요")

def print_n_times(*values, n=1):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("문자열", "안녕하세요", n=1)

print("안", "녕", "하", "세", "요", sep="::", end="")

#딕셔너리 매개변수
def 함수(*가변, **딕셔너리):
    print(가변, 딕셔너리)
함수("안", "녕", "하", a=10, b=20, c=30)