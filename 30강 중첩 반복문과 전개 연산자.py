#2차원 리스트
a = [[1,2,3], [4,5,6], [7,8,9]]
print(a[0])

for i in a:
    print(i)
    for j in i:
        print(j)

#3차원 리스트
a = [[[1],[2], [3]],
    [[4],[5], [6], [7]],
    [[8], [9]]]
for i in a:
    print(i)
    for j in i:
        print(j)

for i in a:
    print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)
            
#전개 연산자 : *리스트 요소를 하나하나 분리하게 됨
            #리스트의 내부와 함수의 매개변수 위치에서 사용된다.
#(1) 리스트 내부
a = [1, 2, 3]
b = [*a, *a]
print(b)

a = [4,5,6]
a.append(7)
print(a)
a = [4, 5, 6]
b = [*a, 7]
print("a:", a)
print("b:", b)

#함수의 매개변수 위치
date = [2023, 8, 10, 9, 00]
#print("{}년 {}월 {}일 {}시 {}분".format(date[0], date[1], date[2], date[3], date[4]))  << 첫번째 방법
print("{}년 {}월 {}일 {}시 {}분".format(*date))