def spreadsheet_to_list(input):
    glist = []
    sublist = []
    breakers = (" ", "\t")
    str = ""
    for x in input:
        if x == "\n":
            sublist.append(str)
            glist.append(sublist)
            sublist = []
            str = ""
        else:
            if x not in breakers:
                str += x
            else:
                sublist.append(str)
                str = ""
    sublist.append(str)
    glist.append(sublist)
    return glist

def get_most_frequent_value(input):
    if len(input) == 0:
        return None
    stats = {}
    for value in input:
        if value in stats:
            stats[value] += 1
        else:
            stats[value] = 1
    highest = input[0]
    for value in input:
        if stats[highest] < stats[value]:
            highest = value
    return highest

