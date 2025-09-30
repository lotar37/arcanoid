s = open("./data/24_223.txt").readline()
print(len(s.split("TIK")) + len(s.split("TOK")) - 2)