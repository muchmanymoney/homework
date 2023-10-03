import re

from calc_view import CalcView


class CalcModel:
    def __init__(self):
        self.view = CalcView

    def insert_formula(self):
        while True:
            formula = input("수학식을 입력해주세요: ")
            only_num = re.split("[+,-,*,/]", formula)   # re.split함수를 이용해 식에서 연산기호(+-*/)를 제외한 부분만 남긴다.
            only_operator = formula   # 입력받은 식에서 위의 코드의 결과를 제외시킨 연산자를 얻기 위해
            _break_num = 0   # 식에 오류가 있으면 continue를 실행하여 다시 입력받기 위해...
            for num in only_num:
                if num.isdigit() == False:   # 입력받은 식에서 연산기호를 제외한 부분에 숫자가 아닌 다른것이 껴있다면 실행되는 조건문
                    self.view.show_error_message()
                    _break_num = 1
                    break

            if _break_num == 1:
                continue

            if _break_num == 0:   # _break_num이 1로 바뀌지 않았다는 것은 입력받은 식에 오류가 없다는 의미이므로 식을 return하고 while문을 빠져나온다.
                break
        return formula




    @staticmethod
    def calculate_text_fomula(formula):
        only_num = re.split("[+,-,*,/]", formula)   # re.split함수를 이용해 식에서 연산기호(+-*/)를 제외한 숫자만 남긴다.
        only_operator = formula    # 입력받은 식에서 위의 코드의 결과를 제외시킨 연산자를 얻기 위해
        _result = only_num[0]  # 두번째 for문에서는 only_num[1]부터 들어가므로 only_num[0]을 미리 넣어준다.
        for num in only_num:
            only_operator = only_operator.replace(num, '')  # 입력받은 식에서 숫자 부분만 제외하여 연산자를 얻는다.

        for i in range(len(only_operator)):
            # eval함수 내의 + 연산자는 str형과 int형의 덧셈을 허용하지 않기 때문에 str()로 감싸주어 str + str 형으로 만들어 준다.
            _result = str(eval(_result + only_operator[i] + only_num[i + 1]))

        return _result


