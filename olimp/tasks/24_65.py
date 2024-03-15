f = open("./data/inf_22_10_20_24.txt")
print(sum([1 if s.count("E") > s.count("A") else 0 for s in f]))

