import sys
from functions import get_most_frequent_value

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
    Circus.get_stack_weights(Circus.head)
    print(Circus)
    print(Circus.verify_stack_weights())



class program:
    def __init__(self, name, weight, parent=None):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.children = []
        self.stack_weight = 0

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
        # Also replaces the strings in children with the proper objects
        for candidate1 in self.list:
            for candidate2 in self.list:
                for index, name in enumerate(candidate2.children):
                    if candidate1.name == name:
                        candidate1.parent = candidate2
                        candidate2.children[index] = candidate1
    
    def get_stack_weights(self, start):
        start.stack_weight += start.weight
        for child in start.children:
            start.stack_weight += Tower.get_stack_weights(start, child)
        return start.stack_weight
    
    def verify_stack_weights(self):
        # This will crumble if an unbalanced program has only 2 children?
        end = 0
        curr = self.head
        while end == 0:
            suspect = curr
            weights = []
            for child in curr.children:
                weights.append(child.stack_weight)
            goal = get_most_frequent_value(weights)
            for child in curr.children:
                if child.stack_weight != goal:
                    curr = child
                    oldgoal = goal
                    break
            if suspect == curr:
                end = 1
        return f'Program {suspect.name} with a stack weight of {suspect.stack_weight} should have a stack weight of {suspect.weight - (suspect.stack_weight - oldgoal)}!'
    
    
    def __repr__(self):
        string = (f'Bottom Program is {self.head.name} with a stack weight of {self.head.stack_weight}')
        # for child in self.head.children:
        #     string += (f'\n Child {child.name} has a stack weight of {child.stack_weight}')
        return string


scan()