


class CalcView:

    def show_result(self, _formula, result):
        print(f"{_formula} 식의 결과값은 {result} 입니다.")

    @staticmethod
    def show_error_message():
        print("숫자와 연산기호 외에는 사용할 수 없습니다.")
