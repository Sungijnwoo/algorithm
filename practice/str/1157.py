from collections import defaultdict

s = input().upper()
params = defaultdict(int)

for i in s:
    params[i] += 1

max_number = max(list(params.values()))

result = []
for key, value in params.items():
    if value == max_number:
        result.append(key)

if len(result) > 1:
    print("?")
else:
    print(result[0]) 
