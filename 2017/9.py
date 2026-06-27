with open("input_9.txt", "r") as fp:
    input = fp.read()

# remove ignored characters
clean_input = ""
skip = False
for i in range(len(input)):
    if skip == True:
        skip = False
        continue
    if input[i] != "!":
        clean_input += input[i]
    else:
        skip = True
input = clean_input

garbage = False
level = 0
total = 0
garbage_count = 0
for chr in input:
    if chr == "<" and garbage == False:
        garbage = True
    elif chr == ">" and garbage == True:
        garbage = False
    elif chr == "{" and garbage == False:
        level += 1
    elif chr == "}" and garbage == False:
        total += level
        level -= 1
    elif garbage == True:
        garbage_count += 1

print(f"The total score is {total} , level after finishing is {level} . Garbage count is {garbage_count} !")