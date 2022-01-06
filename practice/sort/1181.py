n = int(input())
strings = [input() for _ in range(n)]
strings = list(set(strings))
strings.sort(key=lambda x: (len(x), x))

for string in strings:
    print(string)