#a = ['사과', '감', '배']
#a[1] = '수박'
#print(a)


#a = [1,2,3,4,5,6,7,8,1]
#a_set = set(a)
#print(a_set)

a = ['사과', '감', '배', '수박', '딸기']
b = ['배', '사과', '포도', '참외', '수박']

a_set = set(a)
b_set = set(b)

print(a_set & b_set) #교집합
print(a_set | b_set) #합집합
print(a_set - b_set) #차집합