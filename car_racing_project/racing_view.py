


class RacingView:
    def __init__(self):
        pass

    @staticmethod
    def length_must_under_5():
        return print("글자수는 5 이하여야 합니다.")

    @staticmethod
    def show_error_message(e):
        return print(f"문자입력 에러발생: {e}")

    @staticmethod
    def use_line_changer():
        return print("")  # 라운드를 구분하기 위해

    @staticmethod
    def congratulate_winner(name_list):
        return print(f"우승자는 {name_list}입니다. 축하합니다.")



