#리스트 반대로 돌리기
print("abcde")

#print("abcde"[start:end:step])  #시작부분에 [:end:step]라고 하면 가장 앞위치가 들어감, end부분을 없애면 가장 끝부분이 들어간다
print("abcde"[::-1])

#리스트
#print([1, 2, 3, 4, 5])[::-1]

#중첩 리스트
a = [1, 2, 3, 4, 5]
b=[a, a, a]
print(b)
print(b[0])
print(b[0][0])