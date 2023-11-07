#1. 다음 반복문 내부에 if 조건문의 조건식을 채워서 100 이상의 숫자만 출력하게 만들어 보세요. if조건문과 for 반복문을 조합하는 코드는 굉장히 많이 사용된다.
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers   :
    if  number >= 100:
        print("-100이상의 수:", number)

#다음 빈칸을 채워서 실행 결과에 해당하는 프로그램들을 완성해봐라.
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers :
    if number % 2 == 0:
        print(f"{number}은/는 짝수입니다.")
    else:
        print(f"{number}은/는 홀수입니다.")  #// 홀수 짝수 구분

#자릿수 출력
print(f"{number}은/는 {len(str(number))}자리입니다.")

#다음 코드의 빈칸을 채워서 실행 결과처럼 출력되도록 완성해 봐라.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output  = [[], [], []]

for number in numbers :
    output[number % 3 -1].append(number)
print(output)  #//영상 8분 30초