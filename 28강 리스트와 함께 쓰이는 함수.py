#파괴적이다. : 연산 후 피연산자가 변형되는 것
# = 할당 연산자
a = 10
print(a)
a = 20
print(a)

#비파괴적이다. : 연산 후에도 피연산자가 변형되지 않는 것
# +=*/ 연산자
a = 10
print(a)
#a + 20 # a의 값을 파괴하지 못함, 이 결과를 저장하고 싶으면 다른 파괴적인 연산자를 조합해서 사용해야 함
b = a +20
print(a)
print(b)


#요소 추가(파괴적 함수) : append(), insert(), extend()
a = [1, 2, 3, 4]
a.append(10) #가장 마지막에 요소를 하나추가
print(a)
a.insert(0, 20) #원하는 위치에 요소를 하나 추가
print(a)
a.extend([5, 6, 7, 8]) #가장 마지막에 요소를 여러 개 추가, +연산자는 비파괴적 연산자임 그래서 extend처럼 사용하고 싶으면 할당연산자(a = a + [5, 6, 7, 8])를 활용해라
print(a)

#요소 제거 : del, pop(), remove(), clear()
a = [1, 2, 3]
del a[0] # 제거하고 싶은 인덱스 입력
print(a)
a.pop(0) # 제거하고 싶은 인덱스 입력(기본값 -1)
print(a)
a.remove(3) # 제거하고 싶은 요소를 입력
print(a)
a.clear() #모든 요소를 제거
print(a)

#요소 정렬 : sort()
a = [52, 273, 1, 7, 9, 103, 58, 201]
a.sort()
print(a)    #오름차 순으로 출력
a.sort(reverse=True)
print(a)    #내림차 순으로 출력

#요소 존재 확인 : in, not in
print(52 in a)
print(0 in a)
print(not (52 in a)) #52가 a에 없냐?
print(52 not in a) #52가 a에 없냐?