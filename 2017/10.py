import functools
import operator

numbers_list = []
for i in range(256):
    numbers_list.append(i)

with open("input_10.txt", "r") as fp:
    input = fp.read()
lengths = input.split(",")

ascii_lengths = []
for chr in input:
    ascii_lengths.append(ord(chr))
extras = [17, 31, 73, 47, 23]
for extra in extras:
    ascii_lengths.append(extra)

curr = 0
skip_size = 0

def reverse_section(list, curr, length):
    sublist = []
    for i in range(curr, (curr+int(length))):
        if i > 255:
            i -= 256
        sublist.append(list[i])
    sublist.reverse()
    counter = 0
    for i in range(curr, (curr+int(length))):
        if i > 255:
            i -= 256
        list[i] = sublist[counter]
        counter += 1
    return list

for length in lengths:
    numbers_list = reverse_section(numbers_list, curr, length)
    curr += int(length) + skip_size
    if curr > 255:
        curr -= 256
    skip_size += 1

solution = int(numbers_list[0]) * int(numbers_list[1])
print(f"The product of the first two list entries is {solution} !")

curr = 0
skip_size = 0
numbers_list = []
for i in range(256):
    numbers_list.append(i)

for i in range(64):
    for length in ascii_lengths:
        numbers_list = reverse_section(numbers_list, curr, length)
        curr += int(length) + skip_size
        while curr > 255:
            curr -= 256
        skip_size += 1

groups = []
start = 0
stop = 16
while stop <= 256:
    groups.append(numbers_list[start:stop])
    start += 16
    stop += 16

XOR_groups = []
for group in groups:
    XOR_groups.append(functools.reduce(operator.xor, group))

solution2 = ""
for value in XOR_groups:
    solution2 += hex(value)[2:]

print(f'The Knot Hash is {solution2} !')

