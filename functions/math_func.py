def f(x):
    out = 0
    if x <= -2:
        out = 1-(x+2)**2
    elif x > 2:
        out = (x-2)**2 + 1
    else:
        out = -x/2
    return out