with open('input_8.txt', 'r') as fp:
    puzzle_input = fp.read()

actions = puzzle_input.split('\n')


def build_register_map(actions):
    register_map = {}
    for action in actions:
        register = action.split(' ')[0]
        if register not in register_map:
            register_map[register] = 0
    return register_map

def compute_instructions(map, actions):
    highscore = -999
    for action in actions:
        parts = action.split(' ')
        register = parts[0]
        mode = parts[1]
        value = parts[2]
        compare_reg = parts[4]
        operator = parts[5]
        compare_val = parts[6]

        if mode == "dec":
            value = -int(value)

        if operator == "==":
            if map[compare_reg] == int(compare_val):
                map[register] += int(value)
        elif operator == ">=":
            if map[compare_reg] >= int(compare_val):
                map[register] += int(value)
        elif operator == ">":
            if map[compare_reg] > int(compare_val):
                map[register] += int(value)
        elif operator == "<=":
            if map[compare_reg] <= int(compare_val):
                map[register] += int(value)
        elif operator == "<":
            if map[compare_reg] < int(compare_val):
                map[register] += int(value)
        elif operator == "!=":
            if map[compare_reg] != int(compare_val):
                map[register] += int(value)

        if map[register] > highscore:
            highscore = map[register]
    return map, highscore

def get_highest_value(map):
    highest = -999
    for key in map:
        if map[key] > highest:
            highest = map[key]
    return highest

register_map = build_register_map(actions)
computed_map, highscore = compute_instructions(register_map, actions)
final_highest = get_highest_value(computed_map)
print(f'Highest value after finishing was {final_highest}, highest overall was {highscore}!')
