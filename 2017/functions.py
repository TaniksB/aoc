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