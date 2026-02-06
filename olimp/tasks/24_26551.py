ST = open("./data/24_26551.txt").readline()
nechet = "13579BD"
ST = ''.join("*" if s in nechet else s if s in "0123456789ABCD" else " " for s in ST)
# prev = ""
# while len(ST) != len(prev):
#     prev = ST
#     ST = ST.replace("  ", " ")
a = [s.rstrip("*") for s in ST.split()]
print(ST.split()[:10])
print(max(len(s.lstrip("0")) for s in a))



   # da1241241  b232352   34345345c