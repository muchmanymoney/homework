


class WordRelayModel:
    def __init__(self):
        self.korean_alphabet = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢ"
        self.last_cha = ""


    def determine_korean(self, word):
        """
        1. isalpha()를 통해 한글, 영어만 남고 특수문자, 숫자, 띄어쓰기는 걸러진다.
        2. 한글과 영어만 남아있는 상황에서 isascii()가 False인 경우이므로 영어도 걸러진다.
        1과 2의 과정을 거치면 한글만 남게 된다.
        """
        if (word.isalpha() == True) and (word.isascii() == False):
            return True
        else:
            return False

    def is_under_10(self, word):
        # 글자수를 10 이하로 설정하는 코드
        if len(word) <= 10:
            return True
        else:
            return False

    def came_out_before(self, word, word_list):
        """
        나왔던 단어들은 word_list에 append해서
        게임에서 순서가 넘어갈때마다 확인할 예정
        """
        if word not in word_list:
            return True
        else:
            return False

    def compare_end_first(self, word):
        # 전 순서의 끝말과 현재 순서의 첫말이 같은지를 판단하는 코드

        if self.last_cha == "":   # 비교할 단어의 끝말이 없는 첫 순서를 위한 조건문
            return True

        if self.last_cha == word[0]:
            return True
        if self.last_cha != word[0] and self.last_cha != "":
            return False

    def invalid_word(self, word):
        """
        소ㄴ기", "역ㅏ동" 같이 글자에 자음만 혹은 모음만 있은 경우를 걸러내기 위한 조건
        """
        for i in range(len(word)):
            if word[i] in self.korean_alphabet:
                return False


    def set_next_phase(self, word, word_list):
        """
        다음 순서로 넘어가기 위해 현재 단어의 끝말을 저장하고,
        중복한 단어를 걸러내기 위하여 현재 단어를 word_list에 append함
        """
        self.last_cha = word[-1]
        word_list.append(word)

    def check(self, word, word_list):
        """
        조건을 충족하는 단어인지 확인하는 메소드.
        조건에 맞으면 아무것도 return하지 않고
        조건에 맞지 않으면 50을 return함
        """

        if not self.compare_end_first(word):
            print(f"잘못된 단어를 입력하셨습니다. {self.last_cha}로 시작하는 단어를 입력해야 합니다.")
            print("벌점 50점")
            return 50

        elif not self.came_out_before(word, word_list):
            print(f"이전에 나왔던 단어입니다. 현재까지 나왔던 단어 목록은")
            print(f"{word_list} 입니다.")
            print("벌점 50점")
            return 50

        elif not self.determine_korean(word):
            print(f"한국어가 아닙니다. 영어, 숫자, 특수문자, 공백은 사용할 수 없습니다.")
            print("벌점 50점")
            return 50

        elif not self.is_under_10(word):
            print(f"글자수는 10자 이하여야 합니다.")
            print("벌점 50점")
            return 50

        elif (self.invalid_word(word) == False):
            print(f"글자에 자음만 혹은 모음만 포함된 단어는 입력할 수 없습니다.")
            print("벌점 50점")
            return 50

