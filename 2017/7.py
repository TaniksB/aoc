import sys

with open('input_7.txt', 'r') as fp:
    puzzle_input = fp.read()


def scan():
    Circus = Tower()
    lines = puzzle_input.split("\n")
    for line in lines:
        for index, character in enumerate(line):
            if character == " ":
                parent = line[:index]
                break
        open = index + 1
        for index, character in enumerate(line[open:]):
            if character == ")":
                close = index + open
                weight = int(line[open+1:close])
                break
        children = []
        if ">" in line[close:]:
            hmm = line[close+5:].split(",")
            for hmmm in hmm:
                children.append(hmmm.strip(" "))
        Circus.add(parent, weight, children)
    Circus.get_relationships()
    Circus.get_head()
    print(Circus)



class program:
    def __init__(self, name, weight, parent=None):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.children = []

class Tower:
    def __init__(self):
        self.list = []
        self.head = None

    def get_head(self):
        for program in self.list:
            if program.parent is None:
                self.head = program

    def add(self, parent, weight, children):
        parent_obj = program(parent, weight)
        # if self.head is None or parent_obj.parent is None:
        #     self.head = parent_obj
        parent_obj.children = children
        self.list.append(parent_obj)
        

    def get_relationships(self):
        for candidate1 in self.list:
            for candidate2 in self.list:
                if candidate1.name in candidate2.children:
                    candidate1.parent = candidate2
    
    def __repr__(self):
        return (f'Bottom Program is {self.head.name} whose parent is {self.head.parent}')


scan()