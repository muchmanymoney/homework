from wordrelay_model import WordRelayModel
from wordrelay_view import WordRelayView


class WordRelayController:
    def __init__(self):
        self.model = WordRelayModel()
        self.view = WordRelayView()

    def insert_name(self):
        return str(input("플레이어의 이름을 입력하세요: "))

    def insert_word(self):
        return str(input("단어를 입력하세요: "))


    def prepare_next_phase(self, word, word_list):
        self.model.set_next_phase(word, word_list)


    def check_word(self, word, word_list):
        return self.model.check(word, word_list)

    def show_name_a(self, user_a):
        return self.view.display_name_a(user_a)

    def show_name_b(self, user_b):
        return self.view.display_name_b(user_b)

    def current_word_and_turn(self, current_word, user):
        self.view.current_word_and_order(current_word, user)

    def show_score(self, user, score):
        self.view.display_score(user, score)

    def show_all_score(self, user_a, player_a_score, user_b, player_b_score):
        self.view.display_all_score(user_a, player_a_score, user_b, player_b_score)



