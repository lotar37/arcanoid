d = int(input())
arr = []
def foo(a:list,n):
    s = sum(a)
    if s == d and len(a) > 1:
        print("+".join([str(st) for st in a]))
        return 0
    for i in range(n,d+1):
        if s + i > d:
            break
        foo(a+[i],i)
foo(arr,1)