class StringUtility:
    def __init__(self, words):
        self.words = words

    def reverse_string(self):
        rev_string = self.words[::-1]
        print(rev_string)

    def alphabet_frequency(self):
        final_dict = {}
        alpha_num = 0
        for str_1 in self.words:
            if str_1.isalpha() == True:
                alpha_num = self.words.count(str_1)
                final_dict[str_1] = alpha_num
        print(final_dict)

    def count_vowels(self):
        vowels = "aeiouy"
        value = 0
        for vow in self.words:
            if vow in vowels:
                value += 1
        print(value)

if __name__ == "__main__":

    word = "Yesterday all my troubles seemed so far away"

    util = StringUtility(word)

    util.reverse_string()
    util.alphabet_frequency()
    util.count_vowels()

