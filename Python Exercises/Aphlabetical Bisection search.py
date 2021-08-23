
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    x = int(len(aStr)/2)
    for letters in range(len(aStr)):
        if(aStr[x] == char):
            return True
        else:
            if(aStr[x] > char):
                x-=1
            elif(aStr[x] < char):
                x+=1

T = isIn('s',"abcdefgiklmnpqrs")
print(T)
