class WordRelayView:
    def __init__(self):
        pass


    def display_name_a(self, user_a):
        return print(f"첫 번째 플레이어는 {user_a} 입니다.")

    def display_name_b(self, user_b):
        return print(f"두 번째 플레이어는 {user_b} 입니다.")

    def current_word_and_order(self, current_word, user):
        print("--------------------------------------------------")
        print(f"현재 단어는 {current_word}입니다.")
        print(f"{user} 차례입니다.")
        print("--------------------------------------------------")

    def display_score(self, user, score):
        print("--------------------------------------------------")
        print(f"{user}의 현재 스코어는 {score}입니다.")
        print("--------------------------------------------------")

    def display_all_score(self, user_a, player_a_score, user_b, player_b_score):
        print("--------------------------------------------------")
        print(f"(현재 점수) {user_a}: {player_a_score}점,   {user_b}: {player_b_score}점")
        print("--------------------------------------------------")

