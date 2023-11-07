#딕셔너리 키:값 product = {"제품명": "망고", "가격": 4000, "분류": "식품"} //제품명, 가격, 분류는 키 / 망고, 4000, 식품은 값
#즉, "키: 값" 쌍을 여러 개를 붙여서 입력가능, / 키 : 숫자, 문자열, 불, 튜플 / 값 : 모든 값 가능


product = {"name": "7d 건조 망고", "type": "당절임", "test":"delete test"}
#요소의 값을 변경하는 방법
product["name"] = "8d건조망고"
#요소를 추가하는 방법
product["price"] = 5000
#요소를 제거하는 방법
del product["test"]
#키의 존재 확인하는 방법(True or False를 리턴함)과 get()함수
#print("price" in product) 이 코드 아니면
if "origin" in product:
    print(product["origin"])
else:
    print("아직 원산지에 대한 내용이 없습니다.")
#get()함수
print(product.get("name"))
print(product.get("origin")) #get함수의 특징은 존재하지 않는 키를 압력해도 오류발생이 아닌, none을 리턴한다.
# 또는 다른 코드를 사용할 수 있는데,
if product.get("seller") !=None:
    print(product["seller"])
else:
    print("아직 판매자가 없습니다.")
print(product)
#----------------------------------------------------
product = {"제품명": "망고", "가격": 4000, "분류": "식품"}
product["제품명"]
product["가격"]
product["분류"]
#문자열로 만들고 싶다면 반드시 " " 따옴표를 사용하여 감싸줘라.
print(product["제품명"])
print(product["가격"])
print(product["분류"])

#딕셔너리와 반복문
product = {"제품명": "노트북", "가격": 4000, "분류": "전자기기"}
#for 반복변수 in 반복할 수 있는 것(딕셔너리인 product):
    #복합구문
for key in product:
    print(key)
    print(product[key])
    print("-"*20)

#딕셔너리와 중첩 반복문
products = [{"제품명": "노트북", "가격": 4000, "분류": "전자기기"},
{"제품명": "망고", "가격": 4000, "분류": "식품"}]
for product in products:
  for key in product:
    print(key)
    print(product[key])
    print()  # 칸 뛰어 쓰기
  print("-"*40)

#확인문제 1. 다음표에서 dict_a의 결과가 나오도록 빈칸을 채워보라
#dict_a  =   {}
#[][][][][]
#print(dict_a) #{name": "구름"}
dict_a = {}
dict_a["name"] = "구름"
print(dict_a)    #입력한거

dict_a = {"name": "구름"}
del dict_a["name"]
print(dict_a)#제거한거