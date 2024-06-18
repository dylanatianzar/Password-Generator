import alphabet

def convert_word_to_index(word: str):
    return [alphabet.ALPHABET_BY_LETTER[word[i]] for i in range(len(word))]


def make_keyword_same_size_as_pw(password: str, keyword: str):
    number_of_appends = len(password)//len(keyword) + 1
    appended = number_of_appends*keyword
    return appended[:len(password)]


def encrypt(orig_password: list, keyword_as_index: list):
    encrypted = [(orig_password[i] + keyword_as_index[i])%alphabet.ALPHABET_LENGTH
                 for i in range(len(orig_password))]
    encrypted_to_num = [alphabet.ALPHABET_BY_NUM[encrypted[i]] for i in range(len(encrypted))]
    return ''.join(encrypted_to_num)


def decrypt(encrypted_password: list, keyword_as_index: list):
    decrypted = [(encrypted_password[i]-keyword_as_index[i])%alphabet.ALPHABET_LENGTH
                 for i in range(len(encrypted_password))]
    decrypted_to_num = [alphabet.ALPHABET_BY_NUM[decrypted[i]] for i in range(len(decrypted))]
    return ''.join(decrypted_to_num)