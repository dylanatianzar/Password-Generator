import alphabet
import vignere

def main():
    pw = input("Enter a password to encrypt:")
    pw = pw.strip()
    if (set(pw) - set(alphabet.ALPHABET_CHARACTERS)):
        print("There are invalid characters in password. The only allowed characters are:\{\n0-9, A-Z, a-z, !,@,#\}")
    else:
        keyword = input("Enter a keyword:")
        keyword = keyword.strip()
        if set(keyword) - set(alphabet.ALPHABET_CHARACTERS):
            print("There are invalid characters in keyword. The only allowed characters are:\{\n0-9, A-Z, a-z, !,@,#\}")
        else:
            indexed_password = vignere.convert_word_to_index(pw)
            indexed_keyword = vignere.make_keyword_same_size_as_pw(pw, keyword)
            indexed_keyword = vignere.convert_word_to_index(indexed_keyword)
            encrypted = vignere.encrypt(indexed_password,indexed_keyword)
            print("Here is your new encrypted password:" + encrypted)


if __name__ == "__main__":
    main()