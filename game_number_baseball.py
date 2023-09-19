import random

class NumberBaseball:
    def __init__(self):
        pass


    def play(self):
        final_num=0
        for i in range(999):
            num = str(random.randint(102, 999))
            if num[0] != num[1] and num[1] != num[2] and num[0] != num[2]:
                final_num = num
                break

        for chance in range(1,11):
            strike = 0
            ball = 0
            print(f"{chance}번째 기회입니다.")
            player_num = str(input("세자리 숫자를 입력하세요: "))
            if final_num == player_num:
                print("당신이 이겼습니다. 게임을 종료합니다.")
                break
            if chance == 10 and final_num != player_num:
                print(f"당신이 졌습니다. 정답은 {final_num}입니다.")
                break

            # 아웃비교
            if player_num[0] not in final_num and player_num[1] not in final_num and player_num[2] not in final_num:
                print("아웃입니다.")

            #스트라이크 비교: 같은 자리수에 같은 숫자이면 스트라이크
            if final_num[0] == player_num[0]:
                strike += 1
            if final_num[1] == player_num[1]:
                strike += 1
            if final_num[2] == player_num[2]:
                strike += 1
            print(f"{strike} 스트라이크입니다.")

            # 볼 비교 : 자리수는 다르지만 같은 숫자가 있는 경우 볼
            if player_num[0] in final_num and player_num[0] != final_num[0]:
                ball += 1
            if player_num[1] in final_num and player_num[1] != final_num[1]:
                ball += 1
            if player_num[2] in final_num and player_num[2] != final_num[2]:
                ball += 1
            print(f"{ball} 볼입니다.")


if __name__ == "__main__":
    game = NumberBaseball()
    game.play()