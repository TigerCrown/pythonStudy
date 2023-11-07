print('hello sparta')
print('Good Afternoon')
print('1+2+3')
print(1+2+3)
print('1'+'2'+'3')
print('1','2','3')


a = 9
b = 5

print(a**b)
print(a%b)

a = 3
b = 'woozoo'
print(a, b)

a = (2 == 2)
print(a)

first_name = 'Gae'
last_name = 'sibal'

print(first_name+last_name)

a = '2'
b = str(5)
print(a, b)

text = 'fuck suck'
result = text[0:9]
# result = text[:]
# result = text[:3]
# result = text[3:]
# result = len(text)
print(result)

myemail = 'suck@naver.com'
result = myemail
print(result)

myemail = 'suck@naver.com'
result = myemail.split('@')
print(result)

myemail = 'suck@naver.com'
z1 = myemail.split('@')[1]
print(z1)

z2 = z1.split('.')
print(z2)

z3 = z2[0]
print(z3)
# result = myemail.split('@')[1].split('.')[0]
# print(z)
# print(result)

a_list = ['사과', '배']
print(a_list[0])

a_list = ['2', '배', False, ['사과', '감']]
print(a_list[3])
print(a_list[3][1])

a_list = [1,5,6,3,2]
a_list.append(18)
print(a_list)

a_list = [1,5,6,3,2]
result = a_list[-1]
print(result)

a_list = [1,5,6,3,2]
result = len(a_list)
print(result)

a_list = [1,5,6,3,2]
a_list.sort()
print(a_list)

a_list = [1,5,6,3,2]
a_list.sort(reverse=True)
print(a_list)

a_list = [1,5,6,3,2]
result = (5 in a_list)
print(result)

#dict
a_dict = {'name':'bob','age':27}
result = a_dict['age']
print(result)

a_dict = {'friend':['영희', '철수']}
result = a_dict['friend'][1]
print(result)

a_dict = {'friend':['영희', '철수']}
a_dict['height'] = 180
print(a_dict)

a_dict = {'friend':['영희', '철수']}
a_dict['height'] = 180
result = ('height' in a_dict)
print(result)

#people
people = [
    {'name':'bob', 'age':27},
    {'name':'john', 'age':30}
]
print(people)

people = [
    {'name':'bob', 'age':27},
    {'name':'john', 'age':30}
]
print(people[1]['age'])

#if else
money = 5000
if money > 3800:
    print('택시를 탐')
else:
    print('택시를 못탐')
    print('택시 대신 뭐?') # 둘 중에 하나가 선택됨

money = 1000
if money > 3800:
    print('택시를 탐')
elif money > 1200:
    print('버스를 타자')
else:
    print('걸어가자')

#반복문
fruits = ['사과', '배', '감', '수박', '딸기']

for A in fruits:
    print(A)

people = [
    {'name' : 'A', 'age': 20},
    {'name' : 'B', 'age': 30},
    {'name' : 'C', 'age': 40},
    {'name' : 'D', 'age': 50},
    {'name' : 'E', 'age': 60}
]
for person in people:
    print(person)

people = [
        {'name': 'A', 'age': 20},
        {'name': 'B', 'age': 30},
        {'name': 'C', 'age': 40},
        {'name': 'D', 'age': 50},
        {'name': 'E', 'age': 60}
    ]
for person in people:
    name = person['name']
    age = person['age']
    print(name, age)

people = [
        {'name': 'A', 'age': 20},
        {'name': 'B', 'age': 30},
        {'name': 'C', 'age': 40},
        {'name': 'D', 'age': 50},
        {'name': 'E', 'age': 60}
    ]
for person in people:
    name = person['name']
    age = person['age']
    if age > 50:
        print(name, age)

people = [
        {'name': 'A', 'age': 20},
        {'name': 'B', 'age': 30},
        {'name': 'C', 'age': 40},
        {'name': 'D', 'age': 50},
        {'name': 'E', 'age': 60}
    ]
for i, person in enumerate(people):
    name = person['name']
    age = person['age']
    print(i, name, age)
    if i > 30:
        break