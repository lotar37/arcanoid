d = int(input())
arr = []
def foo(a:list,n):
    print(a)
    s = sum(a)
    if s == d:
        print("+".join([str(st) for st in a]))
        return 0
    for i in range(n,d-n+1):
        if s + i > d:
            break
        foo(a+[i],i)
foo(arr,1)