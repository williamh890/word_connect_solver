import re
import sys


def remove_dup_letter_words(words):
    words = list(words)
    for word in reversed(words):
        unique_word = set(list(word))
        #print(len(unique_word), len(word))
        if len(unique_word) != len(word):
            words.remove(word)

    return words


def word_connect_solver(letters, words):
    expression = r"^([" + re.escape(letters) + r"]{3,6})$"

    pattern = re.compile(expression)

    possible_words = set()
    for word in words:
        if pattern.match(word):
            possible_words.add(word)

    possible_words = remove_dup_letter_words(possible_words)

    return sorted(list(set(possible_words)), key=lambda k: len(k))


def load_full_dictionary():
    print("Loading in words...")
    with open("words_all.txt", 'r') as dictionary:
        words = dictionary.read().split()
    print("Done loading words.\n")

    return words


def run():
    print("|-------- Word connect solver --------|")
    print("|-------- Type 'QUIT' to exit --------|\n")

    words = load_full_dictionary()

    while True:
        try:
            letters = input("Enter letters: ")
        except:
            print("Error reading letters")
            continue

        if letters == "QUIT":
            break
        else:
            possible_words = word_connect_solver(letters, words)

        print("\nFound words for letters [{}]:".format(letters))

        to_print = ""
        for w in possible_words:
            to_print += w + ', '

        print(to_print[:-1] + '\n')
    exit()

if __name__ == "__main__":
    try:
        letters = sys.argv[1]
    except:
        run()

    with open("words.txt", "r+") as words_file:
        words = words_file.read().split()

    possible_words = word_connect_solver(sys.argv[1], words)
    print(possible_words)
