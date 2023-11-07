a = "a b c d e f g"

#왼쪽부터 탐색 b는 2번째 자리에 있다.
print(a.find("b"))

#오른쪽부터 탐색 f는 10번째 자리에 있다.
print(a.rfind("f"))

#없는 걸 찾으라 하면 -1 됨
print(a.find("z"))
print(a.rfind("z"))