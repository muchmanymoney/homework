import random

from racing_view import RacingView
from racing_car import Car

class IllegalArgumentException(Exception):
    pass
    # def __init__(self, message):
    #     super().__init__(message)


class CarRacingModel:
    def __init__(self):
        self.view = RacingView
        pass


    def input_name(self):   # 이름을 입력 받는다.
        while True:  # 올바른 조건의 이름이 들어올 때 까지 반복해야 하므로 while True문 사용
            _name = []   # 이름을 저장할 리스트
            _break_num = 0   # _break_num이 1일때 continue를 이용해 while True 반복문의 새 phase를 시작한다.
            # split함수를 이용하면 여러 이름을 콤마로 구분하여 받을수 있다.
            _name = input("경주할 자동차의 이름을 입력해주세요. 이름은 쉽표(,)로 구분합니다: ").split(",")
            for i in range(len(_name)):   # 유저의 수만큼 for문이 실행된다.
                if len(_name[i]) > 5:   # 글자의 크기가 5보다 크면 _break_num이 1이 되고 break로 for문을 빠져나온다.
                    self.view.length_must_under_5()
                    _break_num = 1
                    break
            if _break_num == 1:  # 글자수가 5보다 커서 다시 입력 받으려고 조건문을 통해 continue 실행
                continue
            if _break_num == 0:  # 글자수가 5보다 작아 for문을 무사히 통과 했다면 while문은 빠져나온다.
                break

        return _name   # while문을 빠져나왔다면 조건에 합당한 이름이므로 return으로 반환한다.




    def decide_round(self):
        while True:
            try:
                _round_num = input("라운드 수를 입력해 주세요: ")
                if _round_num.isdigit() == False:  # isdigit은 숫자이면 True를, 숫자가 아니면 False를 return한다.
                    raise IllegalArgumentException("[ERROR] 라운드 수는 반드시 숫자 이어야 합니다.")

                break
            except IllegalArgumentException as e:
                self.view.show_error_message(e)

        return int(_round_num)


    @staticmethod
    def obtain_random_num(name):   # 0에서 9 까지의 수를 랜덤하게 유저의 수만큼 생성
        return random.choices(range(0,10), k=len(name))

    @staticmethod
    def append_temp_list(name, random_num):
        temp_list = []   # 생성한 랜덤의 수를 4 이상이면 1, 4보다 작으면 0으로 temp_list에 저장 --> zero_one_list에 저장
        for n in range(len(name)):
            if random_num[n] >= 4:
                temp_list.append(1)
            elif random_num[n] < 4:
                temp_list.append(0)
        return temp_list

    def append_car_list(self, name, zero_one_list, car_list):
        for n in range(len(name)):   # 유저의 수 만큼 for문이 실행됨
            car = Car(name[n])   # 첫번째 라운드일때 이므로 car객체 생성
            car.position += zero_one_list[n]
            car_list.append(car)
            print(f"{name[n]}:","-"*car.position)   # 과제에 올려주신 형태로 게임이 display 될 예정
        self.view.use_line_changer()
        return car_list

    def add_position_after_1(self, name, car_list, zero_one_list):  # 두번째 라운드, 첫번째 라운드에서 이미 객체가 생성된 상태
        for k in range(len(name)):
            car_list[k].position += zero_one_list[k]
            print(f"{name[k]}:", "-" * car_list[k].position)
        self.view.use_line_changer()

    def obtain_winner_name(self, name, car_list):
        position_list = []
        name_list = []
        for i in range(len(name)):
            position_list.append(car_list[i].position)    # position_list에 유저car객체의 모든 최종 position 값을 유저 순서대로 모은다.
        for n in range(len(name)):
            if position_list[n] == max(position_list):
                name_list.append(name[n])   # position_list의 n번째 원소가 최대값이면 그 순서에 해당하는 이름을 name_list에 어펜드 한다.
        self.view.congratulate_winner(name_list)


