people = [
    {'name': 'A', 'age':78},
    {'name': 'B', 'age':65},
    {'name': 'C', 'age':52},
    {'name': 'D', 'age':80},
    {'name': 'E', },
    {'name': 'F', 'age':47},
]
for person  in people:
    try :
    #print(person)
        if  person ['age'] > 60:
            print(person['name'])
    except:
        print(person['name'], '에러입니다.')