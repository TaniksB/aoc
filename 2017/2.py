from functions import spreadsheet_to_list

with open("/home/adrian_nagel/workspace/private/aoc/2017/input_2.txt") as fp:
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

div_sum = 0
for line in inplist:
    for num_a in line:
        for num_b in line:
            if int(num_a) % int(num_b) == 0:
                if num_a != num_b:
                    print (num_a, num_b)
                    div_sum += int(num_a) / int(num_b)

print (f'Sum of checksums is: {checksum_total}')
print (f'Sum of even divisions is: {int(div_sum)}')