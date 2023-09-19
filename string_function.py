#문자 순서를 거꾸로 바꾸는 함수
def reverse_string(word):
    rev_string = word[::-1]
    print(rev_string)

def alphabet_frequency(word):
    final_dict = {}
    alpha_num = 0
    for str_1 in word:
        if str_1.isalpha() == True:
            alpha_num = word.count(str_1)
            final_dict[str_1] = alpha_num
    print(final_dict)

def count_vowels(word):
    vowels = "aeiouy"
    value = 0
    for vow in word:
        if vow in vowels:
            value += 1
    print(value)


if __name__ == "__main__":

    string_word = "hello world python!!"
    reverse_string(string_word)
    alphabet_frequency(string_word)
    count_vowels(string_word)