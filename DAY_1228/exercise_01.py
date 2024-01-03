# 실습 1
# num1, num2 =input().split("d")
# print(num1)
# print(num2)
num1 = float(input("첫번째 숫자를 입력하세요 : "))
num2 = float(input("두번째 숫자를 입력하세요 : "))

print(f'{num1} + {num2} = {num1+num2}')
print(f'{num1} - {num2} = {num1-num2}')
print(f'{num1} * {num2} = {num1*num2}')
print(f'{num1} / {num2} = {num1/num2}')
print(f'{num1} // {num2} = {num1//num2}')
print(f'{num1} % {num2} = {num1%num2}')
print(f'{num1} ** {num2} = {num1**num2}')

#실습 2
print(f'{num1} > {num2} => {num1>num2}')
print(f'{num1} < {num2} => {num1<num2}')
print(f'{num1} >= {num2} => {num1>=num2}')
print(f'{num1} <= {num2} => {num1<=num2}')
print(f'{num1} == {num2} => {num1==num2}')
print(f'{num1} != {num2} => {num1!=num2}')

#실습 3
maximum_value = float(input("최대값 입력 : "))
minimum_value = float(input("최소값 입력 : "))

print(f'{num1} > {num2} and {num1} > {maximum_value} =>', num1 > num2 and num1 > maximum_value)
print(f'{num1} > {num2} and {num1} > {minimum_value} =>', num1 > num2 and num1 > minimum_value)
print(f'{num1} > {num2} or {num1} > {maximum_value} =>', num1 > num2 or num1 > maximum_value)
print(f'{num1} > {num2} or {num1} > {minimum_value} =>', num1 > num2 or num1 > minimum_value)
print(f'not {num1} =>', not num1)

print(f'{num1} > {num2} and {num1} > {maximum_value} => {num1 > num2 and num1 > maximum_value}')
print(f'{num1} > {num2} and {num1} > {minimum_value} => {num1 > num2 and num1 > minimum_value}')
print(f'{num1} > {num2} or {num1} > {maximum_value} => {num1 > num2 or num1 > maximum_value}')
print(f'{num1} > {num2} or {num1} > {minimum_value} => {num1 > num2 or num1 > minimum_value}')
print(f'not {num1} => {not num1}')

