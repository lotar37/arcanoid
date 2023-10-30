s = ">" + ("9" * 27) + ("3"*7)
print(len(s),s)

while s.find(">99"):
    print(123)
    s = s.replace(">99","<33")
print(len(s),s)
