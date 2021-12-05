from collections import defaultdict

convert = defaultdict(int)
N = int(input())

alpha_list = [list(input()) for i in range(N)]
q = defaultdict(int)

for i in alpha_list:
    for x, j in enumerate(i):
        q[j] += 10**(len(i)-x-1)

q = sorted(q.items(), key=lambda x: x[1], reverse=True)

num = 9
result = 0
while q:
    alpha, number= q.pop(0)
    result += number * num
    num -= 1
print(result)

# def cvt(i):
#     return convert[i]

# alpha_list = [list(map(cvt, i)) for i in alpha_list]
# number_list = [int(''.join(i)) for i in alpha_list]

# print(sum(number_list))
    


