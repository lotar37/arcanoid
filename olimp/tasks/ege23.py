
def fun(n):
    if n == 13:
        return 1
    elif n > 13:
        return 0
    else:
        return fun(n+1) + fun(n*2) + fun(n*3)


print(fun(1))