input = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"
puzzle_input_strings = input.split("\t")
bank_list = []
for str in puzzle_input_strings:
    bank_list.append(int(str))
list_memory = []
redistributions = 0


def get_highest_bank(bank_list):
    highest_bank = 0
    highest_blocks = 0
    for bank, blocks in enumerate(bank_list):
        if blocks > highest_blocks:
            highest_bank = bank
            highest_blocks = blocks
        if blocks == highest_blocks:
            if bank < highest_bank:
                highest_bank = bank
                highest_blocks = blocks
    return highest_bank

def redistribute_blocks(bank_list, highest_bank):
    new_bank_list = bank_list
    stash = bank_list[highest_bank]
    target = highest_bank + 1
    new_bank_list[highest_bank] = 0
    while stash > 0:
        if target == 16:
            target = 0
        new_bank_list[target] += 1
        stash -= 1
        target += 1
    return new_bank_list

while 1 < 2:
    if bank_list not in list_memory:
        memory = bank_list.copy()
        list_memory.append(memory)
        highbank = get_highest_bank(bank_list)
        new_bank_list = redistribute_blocks(bank_list, highbank)
        bank_list = new_bank_list
        redistributions += 1
    else:
        print (f'{redistributions} cycles performed before a loop was detected!')
        looped_list = bank_list.copy()
        break


redistributions = 0
highbank = get_highest_bank(bank_list)
new_bank_list = redistribute_blocks(bank_list, highbank)
bank_list = new_bank_list
redistributions += 1
while 0 == 0:
    if bank_list != looped_list:
        highbank = get_highest_bank(bank_list)
        new_bank_list = redistribute_blocks(bank_list, highbank)
        bank_list = new_bank_list
        redistributions += 1
    else:
        print (f'{redistributions} cycles performed until loop repeated!')
        break