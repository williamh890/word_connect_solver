import re
import sys

words = ""

with open("words.txt", "r+") as words_file:
    words = words_file.read()


def remove_dup_letter_words(words):
    for word in reversed(words):
        unique_word = set(list(word))
        #print(len(unique_word), len(word))
        if len(unique_word) != len(word):
            words.remove(word)

    return words


def word_connect_solver(letters):
    expression = r"\n([" + re.escape(letters) + r"]{2,5})\n"

    possible_words = list(set(re.findall(expression, words)))

    possible_words = remove_dup_letter_words(possible_words)

    return sorted(list(set(possible_words)), key=lambda k: len(k))

if __name__ == "__main__":
    letters = "deb"

    possible_words = word_connect_solver(sys.argv[1])

    print(possible_words)
