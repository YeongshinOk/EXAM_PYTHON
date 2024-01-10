# ------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해지지 않은 경우에 사용
# - 반복의 횟수가 정해진 경우에도 사용 가능함
# ------------------------------------------
# [ 요청 ] 사용자로부터 좋아하는 음식명을 입력 받아 주세요.
#            => input()
#           단, 사용자가 종료라는 음식명 입력 전까지 입력 받으세요.
#           => 몇 번 입력 받아야 입력이 끝날지 알 수 없음
# --------------------------------------------

if False:
    favfood = input("Enter all your fav dish :").split()

    while fav in favfood:
        print(fav)





# ------------------------------------------
# [ 요청 ] 사용자로부터 좋아하는 음식명을 입력 받아 주세요.
#            => input()
#           단, Top 5로 가장 좋아하는 음식 5개만 입력 받으세요.
# --------------------------------------------
TEST = False

if TEST:
    myFoods=[]

    for cnt in range(5):
        food = input(f"{cnt+1}번째 좋아하는 음식명 입력 :")
        myFoods.append(food)

    print('당신은',end='')
    for food in myFoods:
        print(food, end=', ' if myFoods[-1] != food else '')
    print('음식을 좋아하는 군요!')


    strFoods=''
    for cnt in range(5):
        food = input(f'{cnt+1}번째 좋아하는 음식명 입력 :')
        strFoods = strFoods + food + (', ' if cnt != 4 else ' ')
        print(f'strFoods => {strFoods}')
    print(f'당신은 {strFoods} 음식을 좋아하는 군요!')

# ---------------------------------------------------------
# 기본 while 문법
# while 조건식 :
#       실행코드
#       실행코드
# ---------------------------------------------------------
# 타이머 프로그램 만들기 => 다운 카운팅 : 10 9 8 7  ....  1
downCnt = 10
while downCnt>0: # while downCnt>=1:
    print(f'다운 카운팅 {downCnt}초')
    #downCnt = downCnt-1
    downCnt -= 1

downcnt = range(10,0,-1)
for i in downcnt:
    print(f'다운카운팅 {i}초')

upCnt = 1
while upCnt<11:
    print(f'업 카운팅 {upCnt}초')
    upCnt += 1

# for 구문으로 다운 업 카운트 만들어보기

downcnt = range(10,0,-1)
for i in downcnt:
    print(f'다운카운팅 {i}초')

upcnt = range(1,11)
for k in upcnt:
        print(f'업카운팅 {k}초')


