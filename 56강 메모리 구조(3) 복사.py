# 변수를 변수에 할당하면[복사하면]
# 스택에 있는 것이 할당[복사]되는 것이다!
a = 10
b = a

a = 20

print(a)
print(b)

#주소를 스택에 저장
a = [1, 2, 3, 4]
b = a
a = [5, 6, 7, 8]
print(a)
print(b)

a = [1, 2, 3, 4]
b = a
a.append(5)
print(a)
print(b)

#매개변수 복사
a = 10
b = [1, 2, 3, 4]
print(a, b)
def function_a(c, d):
    c = 20
    d = [5, 6, 7, 8]
function_a(a, b)
print(a, b)
def function_b(c,d):
    c = 30
    d.extend([9, 10])
function_b(a, b)
print(a, b)