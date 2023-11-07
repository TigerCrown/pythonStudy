def hello():
    print('안녕')
    print('디지몬')

hello()
hello()


def sum(a,b):
    print('더하기 했네') #<< 단독으로 print(' ')해도 됨
    return a+b

result = sum(1,2)
print(result)

def bus_rate(age):
    if age > 65:
        print('무료입니다')
    elif  age > 20:
        print('성인입니다')
    else :
        print('청소년입니다')
bus_rate(35)

def bus_rate(age):
    if  age > 65:
        return 0
    elif age > 20:
        return 1200
    else:
        return 750
myrate = bus_rate(60)
print(myrate)