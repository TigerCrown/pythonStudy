#공식
#input()
#input()
#N = 10
#for n in range(N):
    #input()

#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. a+b - 3
#첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#각 테스트 케이스는 한 줄로 이루어져 있으먀, 각 줄에 A와 B가 주어진다(0<A, B<10)
#각 테스트 케이스마다 A+B를 출력한다.
T = int(input())

for n in range(T):
    # ["1", "1"]
    a = input().split()
    a_0 = int(a[0])
    a_1 = int(a[1])
    print(a_0 + a_1)