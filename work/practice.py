print(f'0 = {bin(0)[2:]}')
print(f'1 = {bin(1)[2:]}')
print(f'2 = {bin(2)[2:]}')
print(f'3 = {bin(3)[2:]}')
print(f'4 = {bin(4)[2:]}')
print(f'5 = {bin(5)[2:]}')
print(f'6 = {bin(6)[2:]}')
print(f'7 = {bin(7)[2:]}')
print(f'8 = {bin(8)[2:]}')
print(f'9 = {bin(9)[2:]}')
print(f'10 = {bin(10)[2:]}')

a, b = input("Enter two numbers : ").split()
print(int(a)+int(b))

a, b = map(int, input('숫자 두 개를 입력하세요: ').split(','))

print(a + b)