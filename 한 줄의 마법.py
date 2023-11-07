num = 3
# if num % 2 == 0:
#     #print('짝수')
#     result = '짝수'
# else:
#     #print('홀수')
#     result = '홀수'
result = '짝수' if num % 2 == 0 else '홀수'
#result = ('짝수' if num % 2 == 0 else '홀수')
print(f'{num}은 {result}입니다.')


a_list = [1,3,2,5,1,2]
b_list = []
# for a in a_list:
#     b_list.append(a*2)#첨부하다, 덧붙이다.
b_list = [a*2 for a in a_list]
print(b_list)