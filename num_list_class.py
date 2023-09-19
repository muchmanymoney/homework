class MathListFunc:
    def __init__(self, num_list):
        self.num_list = num_list

    def odd_num(self):
        odd_list = []
        for num in self.num_list:
            if num % 2 ==1:
                odd_list.append(num)
        print(odd_list)

    def even_num(self):
        even_list = []
        for num in self.num_list:
            if num % 2 == 0:
                even_list.append(num)
        print(even_list)

    def max_value(self):
        max_num = 0
        for num in self.num_list:
            if num > max_num:
                max_num = num
        print(max_num)

    def min_value(self):
        min_num = self.num_list[0]
        for num in self.num_list:
            if num < min_num:
                min_num = num
        print(min_num)

    def sum_elemnet(self):
        result = 0
        for num in self.num_list:
            result += num
        print(result)


if __name__ == "__main__":
    number = [5, 7, 2, 8, 9, 1, 3, 4]
    obj = MathListFunc(number)
    obj.min_value()
    obj.max_value()
    obj.sum_elemnet()
    obj.odd_num()
    obj.even_num()