import alphabet


def word_to_num(password: str):
    len_of_pass = len(password)
    word_as_num = 0
    for i in range(len_of_pass):
        word_as_num += (alphabet.ALPHABET_BY_LETTER[password[len_of_pass - 1 - i]]) * (alphabet.ALPHABET_LENGTH ** i)
    return word_as_num


def num_to_word(num: int):
    num_as_word = ""
    while num // alphabet.ALPHABET_LENGTH != 0:
        num_as_word += alphabet.ALPHABET_BY_NUM[num % alphabet.ALPHABET_LENGTH]
        num = num//alphabet.ALPHABET_LENGTH
    num_as_word += alphabet.ALPHABET_BY_NUM[num % alphabet.ALPHABET_LENGTH]
    return num_as_word[::-1]


def convert_fivegram_to_num(fivegrams: list):
    fivegrams_as_nums = []
    for i in range(len(fivegrams)):
        fivegrams_as_nums.append(word_to_num(fivegrams[i]))
    return fivegrams_as_nums

def convert_num_to_fivegram(fivegram_nums: list):
    orig_fivegram = []
    for i in range(len(fivegram_nums)):
        orig_fivegram.append(num_to_word(fivegram_nums[i]))
    return orig_fivegram


def encrypt(password: str):
    raise NotImplementedError

def decrypt(password_as_num: int):
    raise NotImplementedError
