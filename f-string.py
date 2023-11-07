scores = [
    {'name': 'A', 'score':78},
    {'name': 'B', 'score':65},
    {'name': 'C', 'score':52},
    {'name': 'D', 'score':80},
    {'name': 'E', 'score':91},
    {'name': 'F', 'score':47},
]
for s in scores:
    #print(s)
    n = s['name']
    s = s['score']
    #print(name, scores)
    #print(name + '의 점수는 ' + str(scores) + ' 점 입니다.')
    print(f'{n}의 점수는 {s}점입니다.')