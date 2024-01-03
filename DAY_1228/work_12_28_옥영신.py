#1
email = 'kim1234@naver.com'
e_front = print(f'@ 앞 부분 : {email[:7]}')
print('-'*50)

domain = 'http://www.naver.com'
d_name = print(f'도메인 이름 : {domain[-9:]}')
print('-'*50)

name = '홍길동'
n_vor = print(f'이름 : {name[1:]}')
print('-'*50)

alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
a_upper = print(f'대문자 : {alphabet[::2]}')
a_lower = print(f'소문자 : {alphabet[1::2]}')
print('-'*50)

reg = "ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ"
r_digit = print(f'숫자 : {reg[3::4]}')
print('-'*50)

id_num = "881120-1068234"
bd_id = print(f'생년월일 : {id_num[:6]}')
pv_id = print(f'뒷 번호 : {id_num[7:]}')
print('-'*50)

#2
num = int(input("[입력] 정수 입력 : "))
print(f"[출력] 10진수 {num}\n16진수 : {hex(num)}\n8진수 : {oct(num)}\n2진수 : {bin(num)}")
print('-'*50)

#3
w1 = input("[입력]")
w2 = input("[입력]")
w3 = input("[입력]")

print(f'코드 값이 가장 큰 단어 : {max(w1,w2,w3)}\n코드 값이 가장 작은 단어 : {min(w1,w2,w3)}')
print('-'*50)

#4
msg = "오늘은 행복한 목요일입니다"
word = input("단어 입력 : ")
print(f'\'{word}\'단어 메시지 존재 여부 : {word in msg}')
print('-'*50)

#5
daneo = input("단어 입력 : ")
d_code_0 = ord(daneo[0])
d_code_1 = ord(daneo[1])
d_code_2 = ord(daneo[2])

d_codevalue = print(f"'{daneo}' 코드값 : {bin(d_code_0)} {bin(d_code_1)[2:]} {bin(d_code_2)[2:]}")


