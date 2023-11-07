#리스트 내포(List Comprehension)
#반복 가능한 것을 기반으로 새로운 리스트를 만들어 내는 문법
# An = 2n + 1 (0 <== n < 10)
# A = {1, 3, 5, 7, 9, ...., 19}
A = []
for i in range(0, 10):
    A.append(2 * i + 1)
print(A)
#리스트 내포
#[표현식 for 반복문]
A = [2 * i + 1 for i in range(0, 10)]
print(A)
#----------------
달러 = [155.43, 302.71, 22.00]
원화 = []
for dollar in 달러:
    원화.append(dollar * 1340)
print(원화)

원화 = [dollar * 1340 for dollar in 달러]
print(원화)

A = [2 * i + 1              #표현식
     for i in range(0,10)   #반복문
     if i % 2 == 0          #조건문
]
print(A)

A = [2 * i + 1 for i in range(0,10)]
A = [2 * i + 1 for i in range(0,10) if i % 2 == 0]
print(A)