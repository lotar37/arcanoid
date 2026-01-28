for A in range(100):
    n = False
    for x in range(1,57):
        for y in range(1,401):
            if x - 3*y >= A:
                n = True
                break
        if n:
            break
    else:
        print(A)
        break