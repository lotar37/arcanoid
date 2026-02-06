s = open("./data/24_19254.txt").readline()
a = s.split("FSRQ")
# print(len(a))
a_len = [len(st) for st in a]
a_sum = [sum(a_len[i:i+81]) for i in range(len(a_len)- 80)]
#максимальная сумма + 80 вхождений + 3 и +3 в начале и конце
print(max(a_sum)+320+6)