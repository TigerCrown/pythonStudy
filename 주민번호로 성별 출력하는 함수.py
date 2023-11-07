def check_gender(pin):
    num = pin.split('-')[1][:1]
    if int(num) % 2 == 0:
        print('여성')
    else :
        print('남성')

check_gender('561651-1646545')
check_gender('561651-2646545')
check_gender('561651-3646545')