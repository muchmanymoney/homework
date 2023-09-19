# 리스트에서 홀수만 선택

def odd_num(numbers):
    odd_list = []
    for i in numbers:
        if i % 2 == 1:
            odd_list.append(i)
    print(odd_list)

# 리스트에서 짝수만 선택

def even_num(numbers):
    even_list = []
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)


# 최대값

def max_value(num_list):
    max_num = 0
    for num in num_list:
        if num > max_num:
            max_num = num
    print(max_num)

# 최솟값
def min_value(num_list):
    min_value = num_list[0]
    for num in num_list:
        if num < min_value:
            min_value = num
    print(min_value)

def sum_element(num_list):
    result = 0
    for num in num_list:
        result += num
    print(result)


if __name__=="__main__":
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_num(number)
    even_num(number)
    max_value(number)
    min_value(number)
    sum_element(number)