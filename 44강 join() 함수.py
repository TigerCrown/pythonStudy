#구문 내부에 여러 줄 문자열을 사용했을 때 문제점
# 정수 입력 > 10
# 입력한 문자열은 10이다.
# 10은 짝수이다.

number = int(input("정수 입력 > "))
if number % 2 == 0:
    print(f"입력한 문자열은 {number}이다. \n{number}은 짝수이다.")

#줄바꿈과 들여, 띄어쓰기
    print(f"""\
 입력한 문자열은 {number}이다.
 {number}은 짝수이다.""")

#괄호를 사용하여 해결
    print(f"입력한 문자열은 {number}이다.\n"
          f"{number}은 짝수이다.")

else:
     print(f"입력한 문자열은 {number}이다. \n{number}은 홀수이다.")

#join()을 사용하여 해결(굉장히 많이 사용됨)
print(",\n".join(["a", "b", "c"]))
print("\n".join([f"입력한 문자열은 {number}이다."
                 f"\n{number}은 홀수이다."]))

#연습문제
A = [#데카르트 평면 위에서 사각형의 왼쪽아래 좌표(X1, Y1),
#      사각형의 오른쪽 위 좌표(X2, Y2)
#      [X1, Y1, X2, Y2]
      [3, 2, 4, 5],
      [1, 2, 2, 6],
      [-1, -2, 2, 4]
      ]
#join함수를 몰랐을 때는 for문을 쓰지만 알게되면
for a in A:
  print(f"{a[0]},{a[1]},{a[2]},{a[3]}")
for a in A:
    a = [str(요소) for 요소 in a]
    print(",".join(a))
#실행 결과 예
#3,2,4,5
#1,2,2,6
#-1,-2,2,4