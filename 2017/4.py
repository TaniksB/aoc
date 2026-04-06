with open("input_4.txt", "r") as fp:
    puzzle_input = fp.read()

valid_num = 0
phrase_list = puzzle_input.split("\n")

for phrase in phrase_list:
    word_list = phrase.split(" ")
    check_list = []
    for word in word_list:
        if word in check_list:
            check_list.append("break")
        else:
            check_list.append(word)
    if "break" not in check_list:
        valid_num += 1

print (f'{valid_num} valid passphrases found!')