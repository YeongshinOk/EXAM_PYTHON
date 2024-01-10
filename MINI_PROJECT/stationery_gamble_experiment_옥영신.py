import random

#함수 이름 : 문방구 도박
def stationery_gamble():
    #게임 참여 자극 멘트
    print("\n100원당 한 판, 500원당 여섯 판")

    #게임 시작을 위한 숫자 입력
    inserted_coin = input("\n게임을 시작하려면 숫자로 금액을 투입하세요 : ")

    #숫자가 아닐 시 다시 시작
    if not inserted_coin.isdecimal():
        print('\n잘못된 입력입니다. 다시 입력하세요.')
        stationery_gamble()

    #숫자일 시 정수로 바꾸고 투입 금액 알림
    else:
        inserted_coin = int(inserted_coin)
        print(f'\n{inserted_coin}원 투입하셨습니다.')

        #투입 금액 저장
        total_payment = inserted_coin

        #추가 투입 금액 반복
        while True:
            additional_coin = input("\n금액을 추가로 투입하시겠습니까?\n현재 금액으로 게임을 시작하시려면 0을 입력해주세요 : ")

            #숫자 아닐 시 다시 입력
            if not additional_coin.isdecimal():
                print(f'\n잘못된 입력입니다. 다시 입력하세요. 현재 투입된 금액 {total_payment}원')
                continue

            #기존 투입된 금액과 추가 투입 금액의 합산 반복
            elif additional_coin.isdecimal() and int(additional_coin) != 0:
                additional_coin=int(additional_coin)
                total_payment += additional_coin
                print(f'\n{total_payment}원 투입하셨습니다.')
                continue

            #"0" 입력 시 투입된 금액에 따라 게임 횟수 계산
            elif int(additional_coin) == 0:
                repeat_count = (total_payment // 100) + (total_payment // 500)
                print(f'\n{repeat_count}회 게임 할 수 있습니다.')

                #게임 횟수만큼 반복
                for i in range(repeat_count,-1,-1):

                    if i > 0 :
                        #투입 금액을 0으로 만들어 게임횟수만큼 반복이 끝나면 돈을 다시 투입해야 게임을 할 수 있다.
                        total_payment = 0

                        draw_count = 0 # 비긴 횟수 카운트. 세 번 비기면 사용자가 패배하는 룰.

                        while True:

                            # 사용자의 선택: 가위(1), 바위(2), 보(3)
                            user_choice = input("\n가위(1), 바위(2), 보(3) 중 하나를 선택하세요 : ")
                            if user_choice not in ['1', '2', '3']:
                                print('\n잘못된 입력입니다. 다시 입력하세요.')
                                continue

                            # elif user_choice.isdecimal():

                                # 컴퓨터의 선택을 무작위로 결정
                            computer_choice = random.randint(1, 3)

                                #user_choice를 정수로 타입 변환
                            user_choice = int(user_choice)

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
                                    break
                                elif random_chance < 0.95: # 25% 확률로 1개의 메달
                                    print('\n축하합니다! 1개의 메달을 받았습니다.')
                                    break
                                elif random_chance < 0.99: # 4% 확률로 2~10개의 메달
                                    medals = random.randint(2, 10)
                                    print(f'\n축하합니다! {medals}개의 메달을 받았습니다.')
                                    break
                                elif random_chance < 0.997: #0.7% 확률로 11~20개의 메달
                                    medals = random.randint(11, 20)
                                    print(f'\n축하합니다! {medals}개의 메달을 받았습니다.')
                                    break
                                else:   #0.3% 확률로 21~30개의 메달
                                    medals = random.randint(21, 30)
                                    print(f'\n축하합니다! {medals}개의 메달을 받았습니다.')
                                    break
                            else:
                                # 사용자가 진 경우
                                print("\n졌습니다. 게임을 종료합니다.\n")
                                break
                    else:   #게임 횟수 반복이 모두 끝나면 다시 첫 화면으로 회귀
                        stationery_gamble()

# 게임 함수 호출
stationery_gamble()


