a = ['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','india']
b = [i for i in a if len(i) == 5]

print(b)

# 심사문제
num1 = int(input())
num2 = int(input())

power = []

for i in range(num1,num2+1):
    power.append(2**i)
del power[1]
del power[-2]
print(power)