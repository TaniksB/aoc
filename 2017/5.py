with open ("input_5.txt", "r") as fp:
    puzzle_input = fp.read()

command_strings_list = puzzle_input.split("\n")
command_list = []
for command in command_strings_list:
    command_list.append(int(command))

location = 0
step_counter = 0
vexit = len(command_list)

while 1 < 2:
    if location < vexit:
        old_location = location
        location += command_list[location]
        if command_list[old_location] < 3:
            command_list[old_location] += 1
        else:
            command_list[old_location] -= 1
        step_counter += 1
    else:
        print (f'{step_counter} steps required to escape!')
        break