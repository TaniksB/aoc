from functions import spreadsheet_to_list

with open("/home/yolo/workspace/private/aoc/2017/input_2.txt") as fp:
    input = fp.read()
    
inplist = spreadsheet_to_list(input)

checksum_total = 0

for num in inplist:
    highest = -999
    lowest = 999
    for digit in num:
        idigit = int(digit)
        if idigit > highest:
            highest = idigit
        if idigit < lowest:
            lowest = idigit
    checksum = highest - lowest
    checksum_total += checksum

print (f'Sum of checksums is: {checksum_total}')