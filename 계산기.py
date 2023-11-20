def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("원하는 연산을 선택하세요.")
print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")
print("4. 나눗셈")
print("0. 나가기")

while(True):
  choice = input("선택 (1/2/3/4/0): ")
  if choice == '0':
    print('종료합니다')
    break

  num1 = float(input("첫 번째 숫자를 입력하세요: "))
  num2 = float(input("두 번째 숫자를 입력하세요: "))

  if choice == '1':
      print(num1, "+", num2, "=", add(num1,num2))

  elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1,num2))

  elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1,num2))

  elif choice == '4':
      print(num1, "/", num2, "=", divide(num1,num2))

  else:
      print("잘못된 입력입니다.")
  print()