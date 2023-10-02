from racing_view import RacingView
from racing_model_3 import CarRacingModel

# 대부분 model의 메소드를 사용하므로 model에서 자세히 설명 하겠습니다.

class RacingController:
    def __init__(self):
        self.model = CarRacingModel
        self.view = RacingView

    def insert_name(self):
        return self.model.input_name(self)

        # return input("경주할 자동차의 이름을 입력해주세요. 이름은 쉽표(,)로 구분합니다: ").split(",")

    def determine_round(self):
        return self.model.decide_round(self)


    def get_random_num(self, name):
        return self.model.obtain_random_num(name)

    def make_temp_list(self, name, random_num):
        return self.model.append_temp_list(name, random_num)

    def make_car_list(self, name, zero_one_list, car_list):
        return self.model.append_car_list(self, name, zero_one_list, car_list)


    def increase_position_after_1(self, name, car_list, zero_one_list):
        self.model.add_position_after_1(self, name, car_list, zero_one_list)

    def get_winner_name(self, name, car_list):
        self.model.obtain_winner_name(self, name, car_list)

