s = list(input())
s = list(map(int, s))

result = s[0]
for i in s[1:]:
    mul = i * result
    plus = i + result
    result = max(mul, plus)

print(result)
