def how_many(aDict):
    num=0
    for key in aDict.keys():
        num += len(aDict[key])
    print(num)
    return num
