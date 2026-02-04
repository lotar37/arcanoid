s = open("./data/24_26549.txt").readline()
a = s.split("2025")
a[-1]=""
a_len = [len("".join(a[i:i+50])) for i in range(len(a)-50) if "".join(a[i:i+50]).count("Y")>=140]
print(max(a_len)+200+3)