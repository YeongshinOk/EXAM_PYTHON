#연습문제
x = 10
y = 3

# def div(x, y):
#     a = x // y
#     b = x % y
#     return a, b
# print(div(x,y))

def get_quotient_remainder(a, b):
    return a // b, a % b

quotient, remainder = get_quotient_remainder(x,y)
print('몫: {}, 나머지: {}'.format(quotient,remainder))

#심화문제
x, y = map(int, input().split())

def calc(x, y):
    return x + y, x - y, x * y, x / y


a, s, m, d = calc(x, y)
print('덧셈: {}, 뺄셈: {}, 곱셉: {}, 나눗셈: {}'.format(a, s, m, d))
# # def add(a,b):
# #     """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
# #     return a + b
# #
# # x = add(10, 20)
# # print(x)
# #
# # print(add.__doc__)
# # help(add)
# #
# # def add(a,b):
# #     return a + b
# #
# # x = add(10,20)
# # print(x)
# # print(add(11,22))
#
# def mul(a, b):
#     c = a * b
#     return c
#
# def add(a, b):
#     c = a + b
#     print(c)
#     d = mul(a, b)
#     print(d)
#
# x=10
# y=20
# add(x,y)
#
# def hello():
#     return (1,2,3)
# print(hello())