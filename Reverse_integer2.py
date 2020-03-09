x = -123
def rev(x):
    if x >= 2**31-1 or x <= -2**31:
        return 0
    else:
        string = str(x)
        if x>=0:
            revst = string[::-1]
        else:
            temp = string[1:]
            temp2 = temp[::-1]
            revst= "-"+temp2
        if int(revst)>=2**31-1 or int(revst) <= -2**31:
            return 0
        else:
            return int(revst)
print(rev(+23456))
