def left_shift(sequince,k):
    temp = sequince[0]
    for i in range(k):
        sequince[i] = sequince[i+1]
    sequince[k] = temp

def check(s):
    if s[0] == "О" or s[len(s)-1] == "О":
        return False
    else:
        return True

def generateCand(seq,s):
    cand = ""
    for i in seq:
        cand += s[i]
    return cand

def print_all_permutation(sequince, s):
    a = []

    k = len(sequince) - 1
    n = k

    print(sequince)
    while k>0:
        left_shift(sequince,k)
        if sequince[k] != k:
            candidate = generateCand(sequince,s)
            # print(sequince,candidate)
            if candidate not in a and check(candidate):
                a.append(candidate)
            k = n
        else:
            k = k -1
    print(len(a))
sequince = [0,1,2,3,4,5,6,7,8]
# print_all_permutation(sequince, "СПО")
print_all_permutation(sequince, "СПОРТЛОТО")
