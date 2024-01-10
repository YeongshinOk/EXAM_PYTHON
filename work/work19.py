# 연습문제
for i in range(5):
    for j in range(5):
        if i <= j:
            print('*',end='')
        else:
            print(' ',end='')
    print()

for i in range(5):
    for j in range(5):
        if j < i:
            print(' ',end='')
        else:
            print('*',end='')
    print()

# 심사문제
row = int(input())
for i in range(row):
    for j in range(1,2*row):
        if j<row-i or j>row+i:
            print(' ',end='')
        else:
            print('*',end='')
    print()


for i in range(5):
    for j in range(5):
        print('j:',j,sep='',end=' ')
    print('i:',i, '\\n',sep='')
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()
for i in range(3):
    for j in range(7):
        print('*', end='')
    print()
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
    print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
