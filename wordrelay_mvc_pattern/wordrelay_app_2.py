from wordrelay_ctrl import WordRelayController


class Application:
    def __init__(self):
        self.ctrl = WordRelayController()  # MVC패턴에서 컨트롤러 클래스 컴포지션
        self.order_variable = "a"  # "a"와 "b"가 번갈아 나오면서 순서가 바뀔 예정
        self.word_list = []   # 나왔던 단어를 append 할 예정, 단어 입력시 이 리스트에 있는지 확인
        self.player_a_score = 0
        self.player_b_score = 0


    def play(self):
        current_word = ""   # 단어 입력시 참고하기 위해 전 순서에서 입력한 단어를 저장하는 변수
        user_a = self.ctrl.insert_name()  # 유저의 이름을 입력 받는다.
        user_b = self.ctrl.insert_name()
        self.ctrl.show_name_a(user_a)
        self.ctrl.show_name_b(user_b)

        while True:

            if self.order_variable == "a":
                _score = 0   # 입력한 단어가 결격 사유가 있을시 50점이 깎일 예정
                self.ctrl.current_word_and_turn(current_word, user_a)   # 전 순서의 단어와 누구 차례인지 view에서 출력한다.
                word = self.ctrl.insert_word()   # 단어입력

                if word == "종료":
                    print("게임을 종료합니다.")
                    break

                _score = self.ctrl.check_word(word, self.word_list)  # 단어가 결격사유가 있으면 50점을 리턴 받는다.
                if _score is not None:   # 유효하지 않은 단어를 입력시 실행될 조건문
                    self.player_a_score -= _score  # 리턴받은 50점을 점수에서 깎는다.
                    self.ctrl.show_score(user_a, self.player_a_score)   # 유저a의 점수를 view에서 출력
                    continue
                else:   # 유효한 단어를 입력했을시 실행될 else문
                    self.ctrl.prepare_next_phase(word, self.word_list)   # 끝말을 self.last_cha에 저장, 나왔던 단어를 word_list에 append
                    self.player_a_score += 100
                    self.ctrl.show_score(user_a, self.player_a_score)    # 유저a의 점수를 view에서 출력
                    self.order_variable = "b"    # 조건들에 맞는 유효한 단어를 입력했기 때문에 유저b로 순서가 넘어간다.
                    current_word = word

            elif self.order_variable == "b":
                _score = 0
                self.ctrl.current_word_and_turn(current_word, user_b)    # 전 순서의 단어와 누구 차례인지 view에서 출력한다.
                word = self.ctrl.insert_word()    # 단어입력
                if word == "종료":
                    print("게임을 종료합니다.")
                    break
                _score = self.ctrl.check_word(word, self.word_list)
                if _score is not None:   # 단어가 결격사유가 있어서 50점을 리턴 받았을때 실행되는 조건문
                    self.player_b_score -= _score    # 리턴받은 50점을 점수에서 깎는다.
                    self.ctrl.show_score(user_b, self.player_b_score)   # 유저b의 name과 score를 출력
                    continue
                else:    # 올바른 단어를 입력했을때 실행될 else문
                    self.ctrl.prepare_next_phase(word, self.word_list)   # 끝말을 self.last_cha에 저장, 나왔던 단어를 word_list에 append
                    self.player_b_score += 100
                    self.ctrl.show_score(user_b, self.player_b_score)    # 유저b의 name과 score를 출력
                    self.order_variable = "a"    # 올바른 단어를 입력했기 때문에 순서가 유저a로 넘어감
                    current_word = word

                self.ctrl.show_all_score(user_a, self.player_a_score, user_b, self.player_b_score)


if __name__ == "__main__":
    Application().play()
