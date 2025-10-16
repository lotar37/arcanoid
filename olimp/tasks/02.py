def foo(n,k):
    smb = "0123456789ABCDEF"
    s = ""
    while n>0:
        s += smb[n%k]
        n //= k

    return s[::-1]


def alhebrInSystem(a,b,system=2,action="+"):
    
    if action == "+":
        n = a + b
    elif action == "-":
        n = abs(a - b)
    return True

while True:
    print("\n введите N и M:", end=" ")
    N,M = [int(i) for i in input().split()]    
    print(f"\n--------------N-{N}--------------")
    for i in 2,4,8,16:
        print(str(i)+"x"+foo(N, i),end="  ")

    #print("Бх4 + Мх4:"+
    print(f"\n--------------M-{M}--------------")
    for i in 4,8:
        print(str(i)+"x"+foo(M, i),end="  ")

    print("\n------sum-4------dif-8--------------")

    print("----",foo(N+M,4)," --- ",foo(N-M,8))
