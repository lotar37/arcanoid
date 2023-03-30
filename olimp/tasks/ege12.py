s = "2" + "8"*99 + "2"

while s.find("81")>-1 or s.find("882")>-1 or s.find("8883")>-1:
    if s.find("81")>-1:
        s = s.replace("81","2",1)
    elif s.find("882")>-1:
        s = s.replace("882","3",1)
    else:
        s = s.replace("8883","1",1)

print(s)