#연습문제
for i in range(1,101):
    if i % 22 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 ==0:
        print('Buzz')
    else:
        print(i)
#심사문제

while True:
    i, j = map(int, input().split())
    if i >= j:
        continue
    if not 10 <= j <= 1000:
        continue
    if i < 1:
        continue
    for i in range(i,j+1):
        if i % 35 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Fizz')
        elif i % 7 == 0:
            print('Buzz')
        else:
            print(i)







#
#
# for i in range(1,101):
#     if i % 15 == 0: # 3과 5의 최소공배수
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)
#
# for i in range(1,100):
#     print('Fizz'*(i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)