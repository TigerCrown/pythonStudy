#다음 빈칸을 채워, numbers 내부에 들어있는 숫자가 몇 번 등장하는지 출력하는 코드를 작성하라.
# 숫자는 무작위로 입력해도 상관 없다.
numbers = {1, 2, 6, 8, 4, 3, 2, 1, 9, 5}
counter = {}
#(1) 요소의 출현을 확인하는 코드 : 요소를 초기화
#for number in numbers:
    #counter[number] = 0
#pass

#(2) 해당 요소의 빈도를 확인하는 코드
#for number in numbers:
    #counter[number] += 1

# 위 식의 합친 식이
for number in numbers:
    if  number  not in  counter:
        counter[number] = 0
    counter[number] += 1
#최종출력
print(counter)
#실행 결과, 1: 3, 2: 4, 6: 1, 8: 2, 4: 3, 3: 3, 9: 3, 5: 2, 7: 2,
#------------------------------------------------------------------
#파이썬은 다음과 같은 방법으로 특정 값이 어떤 자료형인지 확인할 수 있다.
#type("문자열") is str > 문자열인지 확인
#type([]) is list > 리스트인지 확인
#type([{}) is dict > 딕셔너리인지 확인
#이를 활용해 다음 빈칸을 채워 실행 결과와 같이 출력되게 만들어 보라.
character = { "name": "데스페라도", "level": 61, "items": {"gun": "하운드 크레커", "armor": "까먹음"},
              "skill": ["윈드밀", "바베큐", "난사", "스커드 제노사이드"]}
#for key in character:
    #print(f"{key} : {character[key]}")
for key in character:
    print(f"{key} : {character[key]}")
    if type(character[key]) is dict:
        #print(character[key])
        for 키 in character[key]:
            print(f"{키} : {character[key][키]}")
    elif type(character[key]) is list:
        #print(character[key])
        for 요소 in character[key]:
            print(f"스킬 : {요소}")
    else :
        print(f"{key} : {character[key]}")