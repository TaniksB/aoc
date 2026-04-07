with open("input_4.txt", "r") as fp:
    puzzle_input = fp.read()

valid_num = 0
phrase_list = puzzle_input.split("\n")

for phrase in phrase_list:
    word_list = phrase.split(" ")
    check_list = []
    for word in word_list:
        sorted_word_list = sorted(word)
        sorted_word = ""
        for letter in sorted_word_list:
            sorted_word += letter
        if sorted_word in check_list:
            check_list.append("break")
        else:
            check_list.append(sorted_word)
    if "break" not in check_list:
        valid_num += 1

print (f'{valid_num} valid passphrases found!')