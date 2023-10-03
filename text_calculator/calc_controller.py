from calc_model import CalcModel
from calc_view import CalcView


class CalcController:
    def __init__(self):
        self.model = CalcModel()
        self.view = CalcView()


    def input_formula(self):   # 문자열 수식을 입력 받습니다.
        return self.model.insert_formula()

    def calculate_string_formula(self, formula):   # 입력받은 수식을 계산합니다.
        return self.model.calculate_text_fomula(formula)

    def display_result(self, _formula, result):   # 계산 결과를 출력합니다.
        self.view.show_result(_formula, result)
