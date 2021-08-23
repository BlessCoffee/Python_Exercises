def biggest_in_a_dict(aDict):
    for values in aDict.keys():
        x = 0
        num = len(aDict[values])
        if num > x:
            x = num
            biggest = values
    return biggest
