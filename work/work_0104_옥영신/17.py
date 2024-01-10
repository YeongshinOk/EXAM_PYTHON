#연습문제
i = 2
j = 5
while i <=32: #or j >= 1:
    print(f'{i:2} {j:2}')
    # print('%2i %2i' %(i, j))
    i *= 2
    j -= 1
#심사문제
balance = int(input())
while balance > 0:
    balance -= 1350
    if balance > 0:
        print(balance)
i = 0
while i < 100:
     print('Hello, world!',i)
     i += 1

i = 1
while i <= 100:
     print('Hello, world!' , i)
     i += 1

i = 100
# # # # while i > 0:
# # # #     print('Hello, world!', i)
# # # #     i -= 1
# # #
# # # count = int(input('반복할 횟수를 입력하세요. : '))
# # # i = 0
# # # while i < count:
# # #     print('Hello, world!',i)
# # #     i += 1
# # #
# # count = int(input('반복할 횟수를 입력하세요. : '))
# #
# # while count > 0:
# #     print('Hello, world!', count)
# #     count -= 1
# # import random
# # # print(random.random())
# # print(random.randint(1,6))
# import random
#
# i = 0
# while i != 3:
#     i = random.randint(1,6)
#     print(i)
# print(f"{i}이 나왔다")