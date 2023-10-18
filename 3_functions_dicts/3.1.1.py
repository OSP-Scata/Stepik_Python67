def f(x):
    if x <= -2:
        f = 1 - (x+2)**2;
    elif x > 2:
        f = (x-2)**2+1;
    else:
        f = -x/2;
    return f