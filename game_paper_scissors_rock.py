# 가위바위보 게임입니다.
class PaperScissorsRock:
    def __init__(self):
        pass
    def play(self):
        for i in range(999):
            total_list = ["가위", "바위", "보"]
            computer_choice = random.choice(total_list)
            player_choice = str(input('"가위" "바위" "보" 중 하나를 입력하세요: '))

            if player_choice == "가위" and computer_choice == "가위":
                # draw += 1
                print("컴퓨터는 가위입니다. 비겼습니다.")

            if player_choice == "가위" and computer_choice == "바위":
                # lose += 1
                print("컴퓨터는 바위입니다. 졌습니다.")

            if player_choice == "가위" and computer_choice == "보":
                # win += 1
                print("컴퓨터는 보입니다. 이겼습니다.")

            if player_choice == "바위" and computer_choice == "가위":
                # win += 1
                print("컴퓨터는 가위입니다. 이겼습니다.")

            if player_choice == "바위" and computer_choice == "바위":
                # draw += 1
                print("컴퓨터는 바위입니다. 비겼습니다.")

            if player_choice == "바위" and computer_choice == "보":
                # lose += 1
                print("컴퓨터는 보입니다. 졌습니다.")

            if player_choice == "보" and computer_choice == "가위":
                # lose += 1
                print("컴퓨터는 가위입니다. 졌습니다.")

            if player_choice == "보" and computer_choice == "바위":
                # win += 1
                print("컴퓨터는 바위입니다. 이겼습니다.")

            if player_choice == "보" and computer_choice == "보":
                # draw += 1
                print("컴퓨터는 보입니다. 비겼습니다.")

            wanna_quit = str(input("끝내고 싶으신가요?(y/n)"))
            if wanna_quit == "y":
                print("게임을 종료합니다.^^")
                break


if __name__ == "__main__":
    import random
    game = PaperScissorsRock()
    game.play()