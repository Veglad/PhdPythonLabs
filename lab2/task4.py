import re

if __name__ == '__main__':
    print("**** Task 4 - Swap 9th and 11th word in the sentence ***")
    SENTENCE = "Програміст — фахівець, що займається програмуванням, виконує розробку програмного забезпечення (в простіших випадках — окремих програм) для програмованих пристроїв, які, як правило містять один процесор чи більше"

    list_of_words = re.findall(r"\w+", SENTENCE)
    word9 = list_of_words[9]
    word11 = list_of_words[11]
    print("Words:\n ", list_of_words)
    print("9th word: ", word9)
    print("11th word: ", word11)

    indexOf9 = re.search(r"\W{}\W".format(word9), SENTENCE).start() + 1
    indexOf11 = re.search(r"\W{}\W".format(word11), SENTENCE).start() + 1

    updated = SENTENCE[0:indexOf9] + word11 + SENTENCE[indexOf9 + len(word9):indexOf11] + word9 + SENTENCE[indexOf11 + len(word11):]

    print("Sentence:\n ", SENTENCE)
    print("Updates sentence:\n ", updated)
