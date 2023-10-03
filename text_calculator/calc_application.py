from calc_controller import CalcController


class CalcApplication:
    def __init__(self):
        self.ctrl = CalcController()

    def execute(self):
        _formula = self.ctrl.input_formula()    # 문자열 수식을 입력 받습니다.
        result = self.ctrl.calculate_string_formula(_formula)   # 문자열 계산 결과를 얻습니다.
        self.ctrl.display_result(_formula, result)   # 계산 결과 display


if __name__ == "__main__":
    CalcApplication().execute()


