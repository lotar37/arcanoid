a = open("./data/24_21161.txt").readline().split(".")
sUp = "ABCDEFGHKIJ"
# a = "A dfsdf s.f sdfasdf sdfasdf.D sdfasdasdfa.sdakfasd".split(".")
# print(a)
a.pop(-1)
# print(a)
a = [s for s in a if s != ""]
a = [len(s) for s in a if s[0].isupper() and s[1:].islower() and s[-1] != " " and s.count("  ") == 0]
# print(a)
print(max(a)+1)