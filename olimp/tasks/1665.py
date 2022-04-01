#a = input()
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b = []
for i in range(4):
    b += arr[i]
#b = [b + arr[j] for j in range(4)]
print(b)
if sum(b)%4>0:
    print("No solution")
    exit()
num = sum(b)//4
