puzzle_input = 312051

import sys

class square:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        self.man_dist = 0

    def calculate_man_dist(self):
        if self.x >= 0:
            x = self.x
        else:
            x = -self.x
        if self.y >= 0:
            y = self.y
        else:
            y = -self.y
        self.man_dist = x + y

counter = 2
crd_x = 1
crd_y = 0
step_counter = 0
steps = 1
snail = []
mode = 0 # 0 = up, 1 = left, 2 = down, 3 = right
newmode = None
while counter <= puzzle_input:
        num = square(counter, crd_x, crd_y)
        num.calculate_man_dist()
        snail.append(num)
        if mode == 0:
            crd_y += 1
        if mode == 1:
            crd_x -= 1
        if mode == 2:
            crd_y -= 1
        if mode == 3:
            crd_x += 1
        step_counter += 1
        if step_counter == steps:
            if mode % 2 == 0:
                steps += 1
            step_counter = 0
            mode += 1
        if mode == 4:
            mode = 0
        counter += 1
        print (f'Number {num.num} with coordinates x{num.x} y{num.y} has a Manhattan Distance of {num.man_dist}!')
sys.exit()