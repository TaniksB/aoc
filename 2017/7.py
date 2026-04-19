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
layers = [None]
layers.append(lowest_seen)

def scan(layers, programs):
    for program in programs:
        for ind in program[1:]:
            if layers[-1] == ind:
                layers.append(program[0])
                return layers
    print (f'Base program is {layers[-1]}!')
    sys.exit()

while 0 == 0:
    scan(layers, programs)


