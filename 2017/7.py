import sys

with open('7_input.txt', 'r') as fp:
    puzzle_input = fp.read()

puzzle_lines = puzzle_input.split('\n')

programs = []

for line in puzzle_lines:
    program = []
    items = line.split(' ')
    for item in items:
        nocomma_item = ''
        for letter in item:
            if letter != ',':
                nocomma_item += letter
        if nocomma_item[0] != '(':
            if nocomma_item[0] != '-':
                program.append(nocomma_item)
    programs.append(program)

start = programs[0]
lowest_seen = start[0]
previous = None

def scan(lowest):
    for program in programs:
        for ind in program[1:]:
            if ind == lowest:
                lowest_seen = program[0]
    print (lowest_seen)
    return lowest_seen

while 0 == 0:
    if previous != lowest_seen:
        previous = lowest_seen
        lowest_seen = scan(lowest_seen)
    else:
        print (f'Base program is {lowest_seen} !')
        sys.exit()