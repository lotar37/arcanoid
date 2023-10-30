def foo1(num):
    if num > 15 or num == 11:
        return 0
    if num == 15:
        return 1
    return foo1(num + 1) + foo1(num*2) + foo1(num*3)
def foo2(num):
    if num > 25:
        return 0
    if num == 25:
        return 1
    return foo2(num + 1) + foo2(num*2) + foo2(num*3)

print(foo1(2) * foo2(15))