A = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
# 어떠한 요소가 몇번 사용되었는지 확인하기 위해서는 일반적으로 딕셔너리를 활용한다.
카운터 = {}

for a in A:
    카운터[a] = 0
for a in A:
    카운터[a] += 1

for a in A:
    if a not in 카운터:
        카운터[a] = 0
    카운터[a] += 1
print(카운터)
print(len(카운터))
print(f"사용된 숫자의 종류는 {len(카운터)}개 입니다.")

A = "abcdefghijklmnopqrstuvwxyz"

카운터 = {}
for i in range(0, len(A), 3):
    print(i, i+3, A[i:i+3])
for i in range(0, len(A), 3):
    a = A[i:i+3]
    if len(a) !=3: #a라는 문자열의 길이가 3개가 아닐 경우, continue를 사용하여 반복을 생략 건너띄어라
        continue
    if a not in 카운터:
        카운터[a] = 0
    카운터[a] += 1
print(카운터)
print(f"사용된 숫자의 종류는 {len(카운터)}개입니다.")