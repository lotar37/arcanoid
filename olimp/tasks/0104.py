from random import randint

a1 = [str(s) for s in range(4)]
a2 = a1 + ["*", "?", "*", "?", "*", "?"]
a1 += ["3", "4","5", "6"]
print(a1, a2)
s = "".join([a1[randint(0, len(a1) - 1)] for ss in range(10)])
mask = "".join([a2[randint(0, len(a2) - 1)] for ss in range(5)])
while mask.find("**") > -1:
    mask = mask.replace("**","*")
print(s,mask,[ss.split("*") for ss in mask.split("?")])

