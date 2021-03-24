import ipdb

def sum(x):
    r = 0
    for i in x:
        r += i

    return r

def mul(x):

    r = 1
    for i in x :
        r *= i

    return r

ipdb.set_trace()
x = [1,2,3,4,5]
r = sum(x)
m = mul(x)