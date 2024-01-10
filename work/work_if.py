# 연습문제
x = 5
if not x==10:
    print('ok')

if x!=10:
    print('ok')
# 심사문제
# price = input()
# discount = input().split()
#
# print(f'{price}-')

price=int(input())
coupon=input()

if coupon[4:] == "Cash" :
    print(f'{price}-{int(coupon[4:])}')