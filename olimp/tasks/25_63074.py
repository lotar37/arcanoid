for i in range(10):
    n =  10 ** 6 + 4239 * 100 + i * 10 + 7
    if n % 3147 == 0:
        print(n)
    for j in range(10):
        n = 10 ** 7 + j * 10 ** 6 + 4239 * 100 + i * 10 + 7
        if n % 3147 == 0:
            print(n)
        for k in range(10):
            n = 10 ** 8 + k * 10 ** 7 + j * 10 ** 6 + 4239 * 100 + i * 10 + 7
            if n % 3147 == 0:
                print(n)
            for l in range(10):
                n = 10**9 + l* 10**8 + k*10**7 + j * 10**6 + 4239* 100 + i*10 + 7
                if n % 3147 == 0:
                    print(n)