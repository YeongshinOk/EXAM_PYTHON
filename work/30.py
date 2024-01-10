#연습문제
korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)

#심사문제
def get_min_max_score(*args):
    return min(args), max(args)

def get_average(*args):
    return sum(args)/len(get_average())

# print(10, 20, 30)

# def print_numbers(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# # print_numbers(10, 20,30)
#
# # x = [10, 20, 30]
# # print_numbers(*x)
#
# print_numbers(*(10, 20, 30))

# def print_numbers(*args):
#     for arg in args:
#         print(arg)
# print_numbers(10, 2,3,4,5,6,7,8,3)
#
# x = [1111, 'asdf']
# print_numbers(*x)
#
# y = [10, 20, 30, 40]
# print_numbers(*y)

# def print_numbers(a, *args):
#     print(a)
#     print(args)
#
# print_numbers(1)
#
# print_numbers(1, 10,20)
#
# print_numbers(*[10, 20,30])

# def personal_info(name, age, address):
#     print('name:',name)
#     print('age:',age)
#     print('address:',address)
#
# # personal_info('Hong-GilDong', 30, 'Seoul')
#
# personal_info(address='Seoul',age = 30,name='Hong-GilDong')
#
# print(10, 20, 30,sep=' : ',end='')

# def personal_info(name, age, address):
#     print('이름: ', name)
#     print('나이: ', age)
#     print('주소: ', address)
#
# x = {'age': 30, 'address': '서울시 용산구 이촌동', 'name': '홍길동'}
# # 딕셔너리 앞에 * 를 하나만 쓰면 키를 가져간다. 값이 아니라. 두개 써야 값을 가져감
# personal_info(*x)
#
# personal_info(**{'age': 30, 'address': '서울시 용산구 이촌동', 'name': '홍길동'})

# def personal_info(**kwargs):
#     for kw, arg in kwargs.items():
#         print(kw,': ', arg, sep='')

# personal_info(name='홍길동')
#
# personal_info(age=30,name='홍길동', address='서울시 용산구 이촌동')

# x = {'name':'홍길동'}
#
# personal_info(**x)
#
# y = {'age':30,'name':'홍길동', 'address':'서울시 용산구 이촌동'}
#
# personal_info(**y)

# def personal_info(**kwargs):
#     if 'name' in kwargs:
#         print('이름: ', kwargs['name'])
#     if 'age' in kwargs:
#         print('나이: ', kwargs['age'])
#     if 'address' in kwargs:
#         print('주소: ', kwargs['address'])
#
#
# x = {'name':'홍길동'}
#
# personal_info(**x)
#
# y = {'age':30,'name':'홍길동', 'address':'서울시 용산구 이촌동'}
#
# personal_info(**y)

# def personal_info(name, **kwargs):
#     print(name)
#     print(kwargs)
#
# personal_info('홍길동')
#
# personal_info('홍길동', address='서울시 용산구 이촌동',age=30)
#
# personal_info(**{'name':'홍길동','age':30,'address':'서울시 용산구 이촌동'})

# def custom_print(*args,**kwargs):
#     print(*args,**kwargs)
#
# custom_print(1,2,3, sep=':', end='')

# def personal_info(name, age, address='비공개'):
#     print('이름: ', name)
#     print('나이: ', age)
#     print('주소: ', address)
#
# # personal_info('홍길동', 30)
#
#
# personal_info('홍길동', 30, '서울시 용산구 이촌동')

# def personal_info(name, address, age):
#     print('이름 :', name)
#     print('나이 :', age)
#     print('주소 :', address)
#
# def personal_info(name='비공개', age=0, address='비공개'):
#     print('이름 :', name)
#     print('나이 :', age)
#     print('주소 :', address)
#
# personal_info()

