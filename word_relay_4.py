class WordRelay:
    def __init__(self):
        self.player_1_score = 0  # 플레이어1의 누적점수
        self.player_2_score = 0  # 플레이어2의 누적점수
        self.num = 1  # play 메소드에서 플레이어1,2의 누적점수를 넣을때 순서를 구분하기 위해 쓸 변수
        self.last_cha = ""  # 전 단어의 끝 말과 다음단어의 첫 말을 비교할 때 사용할 끝말이다.
        self.word_list = []   # 입력한 단어를 모으는 리스트, 이전에 나왔던 단언인지 확인하기 위함이다.
        self.korean_alphabet = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢ"

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

    def came_out_before(self, word):
        """
        나왔던 단어들은 word_list에 append해서
        게임에서 순서가 넘어갈때마다 확인할 예정
        """
        if word not in self.word_list:
            return True
        else:
            return False

    def compare_end_first(self, word):
        # 전 순서의 끝말과 현재 순서의 첫말이 같은지를 판단하는 코드
        if self.last_cha == word[0]:
            return True
        else:
            return False

    def add_score(self):
        """
        끝말잇기에 성공할 경우  50점을 얻는다.
        self.num이 홀수인 경우에는 플레이어1의 점수가 올라가고
        self.num이 짝수인 경우에는 플레이어2의 점수가 올라간다.
        """
        if self.num % 2 == 1:
            self.player_1_score += 50
        elif self.num % 2 == 0:
            self.player_2_score += 50


    def sub_score(self):
        """
        규칙에 어긋난 단어를 입력하면 30점이 깎인다.
        self.num이 홀수인 경우에는 플레이어1의 점수가 깎이고
        self.num이 짝수인 경우에는 플레이어2의 점수가 깎인다.
        """
        if self.num % 2 == 1:
            self.player_1_score -= 30
        elif self.num % 2 == 0:
            self.player_2_score -= 30

    def invalid_word(self, word):
        """
        소ㄴ기", "역ㅏ동" 같이 글자에 자음만 혹은 모음만 있은 경우를 걸러내기 위한 조건
        """
        for i in range(len(word)):
            if word[i] in self.korean_alphabet:
                return False

    def first_condition(self, word):
        """
        self.num = 1 일 때의 if문에 쓰이는 조건.
        첫 번째 순서이기 때문에 끝말과 첫글자가 일치해야 하는 조건과
        이전에 나왔던 단어인지를 확인하는 조건은 포함되지 않는다.
        """
        return (self.determine_korean(word)) and (self.is_under_10(word)) and (self.invalid_word(word) != False)

    def after_num_1_condition(self, word):
        """
        self.num이 1보다 클 때 if문에 쓰이는 조건.
        전 단어의 끝말과 입력 단어의 첫 말이 같은지,
        이전에 나왔던 단어인지,
        한국어만 허용되는지,
        글자수가 10보다 작은지,
        유효하지 않은 단어인지
        위의 조건들을 판단하여 규정에 옳은 단어일때만 True를 반환한다.
        """
        return (self.compare_end_first(word)) and (self.came_out_before(word)) and (self.determine_korean(word)) and (self.is_under_10(word)) and (self.invalid_word(word) != False)


    def play(self):
        while True:
            word = str(input("단어를 입력하세요: "))
            if word == "종료":
                print("끝말잇기를 종료합니다.")
                break
            if self.num == 1:  # 첫 순서는 비교할 전 순서의 끝말이 없기 때문에 그 조건을 제외한 나머지 조건들만 설정
                if self.first_condition(word):
                    self.word_list.append(word)
                    self.add_score()
                    self.num += 1   #self.num이 1씩 증가하면서 플레이어1과 플레이어2가 번갈아가며 단어를 입력한다.
                    self.last_cha = word[-1]  # 현재 단어의 끝말을 변수에 저장하여 다음 순서에서 첫말과 비교할 예정
                    print(f"현재단어: {word}")
                else:
                    self.sub_score()
                    print(f"플레이어1 점수: {self.player_1_score}")
                    print(f"플레이어2 점수: {self.player_2_score}")
                    continue
                print(f"플레이어1 점수: {self.player_1_score}")
                print(f"플레이어2 점수: {self.player_2_score}")

            else:  # self.num이 1이 아닌경우 실행되는 코드
                if self.after_num_1_condition(word):
                    self.word_list.append(word)
                    self.last_cha = word[-1]
                    print(f"현재단어: {word}")
                    self.add_score()
                    self.num += 1
                else:
                    self.sub_score()
                print(f"플레이어1 점수: {self.player_1_score}")
                print(f"플레이어2 점수: {self.player_2_score}")


if __name__ == "__main__":
    WordRelay().play()