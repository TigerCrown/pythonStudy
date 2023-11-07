#if 주건문
## 조건이 True일 때만 들여쓰기 안쪽의 문장을 실행
if True : print("트루입니다.")

if False : print("펄스입니다.")

#사용자가 입력한 숫자가 양수 음수 0인지 판별하는 프로그램
raw_input = input("정수를 입력해주세요.")
raw_input = int(raw_input)

if raw_input > 0:
    print("양수")
if raw_input < 0:
    print("음수")
if raw_input == 0:
    print("0입니다")

#오전 오후 구분하는 프로그램
from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))
print(f"{today.hour}시 입니다.ㄴ")
if today.hour < 12:
    print("오전")
if today.hour >= 12:
    print("오후")

#계절을 구분하는 프로그램
from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))
m = today.month

if 3 <= m <= 5:
    print("봄")
if 6 <= m <= 8:
    print("여름")
if 9 <= m <= 11:
    print("가을")
if (11 <= m <= 12) or (m == 1):
    print("겨울")