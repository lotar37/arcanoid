# count = 0
# minimum = int('91EEE',16) + int('90E4E',15)
# for x in '0123456789ABCDE':
#     for y in '0123456789ABCDE':
#         if (int('90'+x+"4"+y,15) + int('91'+x+y+"2",16))%56:
#             if (int('90'+x+"4"+y,15) + int('91'+x+y+"2",16)) < minimum:
#                 minimum = int('90'+x+"4"+y,15) + int('91'+x+y+"2",16)
#
# print(minimum//56)


a = sum([k[0] - k[1] for k in [[int(j) for j in input().split()] for i in range(4)] ])
print(a)
