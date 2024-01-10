#연습문제
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break

    print(i, end=' ')
    i += 1

#심사문제
start, stop = map(int, input().split())

i = start

while True:
    if i >= stop:
        break
    if not 10 < stop < 200:
        break
    if i % 10 == 3:
        i += 1
        continue

    print(i, end=' ')
    i += 1



# i=0
# while True:
#     print(i)
#     i += 1
#     if i == 100:
#         break
#
# for i in range(10000):
#     print(i)
#     if i == 100:
#         break

# for i in range(100):
#     if i % 2 == 0:
#         continue
#     print(i)

# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)

# count = int(input('반복할 횟수를 입력하세요: '))
#
# i = 0
# while True: #무한루프
#     print(i)
#     i += 1
#     if i == count: #i가 입력 받은 값과 같을 때
#         break       #반복문을 끝냄
#
# cnt = int(input('반복할 횟수 입력! :'))
# i = 0
# while i < cnt:
#     print(i)
#     i += 1

