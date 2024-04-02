for n in range(1204300,1204381):
    s = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                s += i
            if (n // i) % 2 == 0:
                s += n // i
    if s % 10 == 0 and s > 0:
        print(n,s)

print(5*6**5 + 5 * 6**4 + 5*6**3 + 4*6**2 + 3*6+1, 6**6 )