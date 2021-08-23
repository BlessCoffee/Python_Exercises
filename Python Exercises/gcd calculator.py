"""
def gcdIter(a, b):
    if a > b:
        while a != 0:
            x = a%b
            if x == 0:
                return b
            a = b
            b = x

    else:
        while b != 0:
            x = b%a
            if x == 0:
                return a
            b = a
            a = x


x = gcdIter(153,12)

print(x)
"""

def gcdRecur(a,b):

    if a > b:
        x = a%b
        if x == 0:
            return b
        num = gcdRecur(b,x)
        return num
    elif b > a:
        x = b%a
        if x == 0:
            return a
        num = gcdRecur(a,x)
        return num



x = gcdRecur(12,153)
print(x)
