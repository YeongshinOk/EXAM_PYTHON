# --------------------------------------------------------
# [실습1] "Hello World" 100번 출력
# --------------------------------------------------------
# 반복문 => for in 반복문 ==================================
# - 여러개의 데이터를 가지고 있는 데이터에서 한 개씩 원소/요소를
#   읽어와줌
# for 요소저장변수명 in 여러개 데이터 가진 타입:
# <---->요소/원소 반복할 코드
# <---->요소/원소 반복할 코드
#for x in range(1,101):
#    print("Hello World " * x)

for count in range(100):
    print("Hello World")
# --------------------------------------------------------
msg = "Happy New Year 2024! Good Luck^^"

# msg를 구성하는 문자 한개씩 화면에 출력해주세요!
# H
# a
# p
# p
# y
#
# N
# e

#for idx in range(len(msg)):
#    print(msg[idx])

for ele in msg:
    print(ele)

# [실습2] 좋아하는 음식명을 리스트에 저장하기 (단, 10개)
foods = ['Pizza','Ramen','Brot','Milch','Bibimbap','Fleisch','BBQ','Cheese','Donkatsu','Malatang']

for zxc in foods:
    print(zxc)

for cnt in foods: print(cnt)

#for cnt in foods: print(cnt) print(cnt) 두개는 안됨
