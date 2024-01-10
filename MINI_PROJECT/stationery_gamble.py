import random

def stationery_gamble():
    print("\n100원당 한 판, 500원당 여섯 판")
    #게임 시작을 위한 숫자 입력
    inserted_coin = int(input("\n게임을 시작하려면 100원을 넣으세요 : "))
    if inserted_coin != 100:
        print('\n잘못된 입력입니다. 다시 입력하세요.')
        stationery_gamble()

    draw_count = 0 # 비긴 횟수 카운트. 세 번 비기면 사용자가 패배하는 룰.

    while True:
        # 사용자의 선택: 가위(1), 바위(2), 보(3)
        user_choice = int(input("\n가위(1), 바위(2), 보(3) 중 하나를 선택하세요 : "))
        if user_choice not in [1, 2, 3]:
            print('\n잘못된 입력입니다. 다시 입력하세요.')
            continue

        # 컴퓨터의 선택을 무작위로 결정
        computer_choice = random.randint(1, 3)

        # 가위바위보 결과 판정
        if user_choice == computer_choice:
            draw_count += 1
            if draw_count == 3: # 세 번 비기면 사용자 패배
                print("\n세 번 비겼습니다. 게임에서 졌습니다.")
                stationery_gamble()
            print('\n비겼습니다. 다시 선택하세요.')
            continue
        else:
            draw_count = 0  # 비긴 횟수 초기화 왜인지는 모르겠는데 초기화 안하면 오류남..

        # 이기는 수
        if (user_choice == 1 and computer_choice == 3) or \
           (user_choice == 2 and computer_choice == 1) or \
           (user_choice == 3 and computer_choice == 2):
            print('\n가위바위보에 이기셨습니다.')

            # 사용자가 이긴 경우, 메달 지급 확률 결정
            random_chance = random.random()
            if random_chance < 0.70: # 70% 확률로 꽝
                print("\n꽝! 다음 기회에")
                stationery_gamble()
            elif random_chance < 0.95: # 25% 확률로 1개의 메달
                print('\n축하합니다! 1개의 메달을 받았습니다.')
                stationery_gamble()
            elif random_chance < 0.99: # 4% 확률로 2~10개의 메달
                medals = random.randint(2, 10)
                print(f'\n축하합니다! {medals}개의 메달을 받았습니다.')
                stationery_gamble()
            elif random_chance < 0.997: #0.7% 확률로 11~20개의 메달
                medals = random.randint(11, 20)
                print(f'\n축하합니다! {medals}개의 메달을 받았습니다.')
                stationery_gamble()
            else:   #0.3% 확률로 21~30개의 메달
                medals = random.randint(21, 30)
                print(f'\n축하합니다! {medals}개의 메달을 받았습니다.')
                stationery_gamble()
        else:
            # 사용자가 진 경우
            print("\n졌습니다. 게임을 종료합니다.")
            stationery_gamble()

# 게임 함수 호출
stationery_gamble()





# import random
# while True:
#     print("짱켄뽀 게임에 오신 것을 환영합니다.")
#     i = input("코인을 넣어주세요\n백원당 한판 오백원당 여섯판 : "))
#
#     if i.isdecimal:
#         i=int(i)
#
#     else:
#         print('잘못된 입력입니다.')
#
# while i>0:
#     print(i)
#     # i
#     #
#     #     if i.isdecimal:
#     #         pass
#     #     else:
#     #         print('잘못된 입력입니다.')
#     # while i > 0:
#
# # for i == 0:
# #
# #     if not i == 0:
# #
# #
# #     a = [가위, 바위, 보]
# #
# #     idx random.randint(3)