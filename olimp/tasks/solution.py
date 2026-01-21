A, B, n, m = (int(s) for s in input().split())
if n == 0 or m == 0:
    print(0,0)
else:
    # Если общее количество ног и голов 2:1 значит по максимальному количеству
    # людей
    if 2*n == m:
        print(n,0)
        # если соотношение ног и голов как у человека, но предыдущая ветка
        # не сработала, то решение не может сложиться
    elif 2*A == B:
        print(-1)
    else:
        ab = (2*n-m)/(2*A - B)
        if ab - int(ab) > 0:
            print(-1)
        else:
            human = n - ab*A
            if ab>=0 and human >=0:
                print(int(human), int(ab))
            else:
                print(-1)