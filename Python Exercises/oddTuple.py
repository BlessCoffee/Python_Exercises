def oddTuple(aTup):

    x = ()
    for i in range(len(aTup)):

        if(len(aTup[i])%2 == 1):
            x += (aTup[i],)
    print(x)
    return x

oddTuple(('I', 'am', 'a', 'test', 'tuple', 'apple', 'cool', 'dude', 'bruh'))
