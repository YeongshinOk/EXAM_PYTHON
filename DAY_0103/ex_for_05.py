# ----------------------------------------------------------
# [실습] 알고 싶은 단을 입력 받고 해당 단을 출력해주세요.
# - input()
# - 특정 단의 구구단을 출력 => 반복문 사용 하기
# ----------------------------------------------------------
multiple = input('알고 싶은 단을 입력하세요 :')
multiple = int(multiple)
if multiple:
    for cal in range(1,10):
        print(f'{multiple} * {cal} = {multiple*cal}')
else:
    print("입력된 데이터가 없습니다.")


if multiple and multiple.isdecimal():
    for cal in range(1,10):
        print(f'{multiple} * {cal} = {multiple*cal}')
else:
    print("입력된 데이터가 없습니다.")

if multiple:
    if multiple.isdecimal():
        for cal in range(1,10):
            print(f'{multiple} * {cal} = {multiple*cal}')
    else:
        print("숫자만 입력 가능합니다.")
else:
    print("입력된 데이터가 없습니다.")

# ------------------------------------------------------------------
# [실습] 2단 ~ 9단까지 모두 출력 하세요. 반복문 사용하기!!!
# - 중첩 for 반복문
# ------------------------------------------------------------------

for dan in range(2,10):
    print(f'---{dan}단---')
    for mul in range(1,10):
        print(f'{dan} * {mul} = {dan*mul}')

for mul in range(1,10):
    for dan in range(2,10):
        if mul:
            print(f'{dan} * {mul} = {dan*mul:2}', end='\n' if dan == 9 else '   ')
        else mul:
            print(f'---{dan:^4}단---', end='\n' if dan == 9 else '  ')

