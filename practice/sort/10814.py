n = int(input())
members = []
for _ in range(n):
    age, name = input().split()
    members.append((int(age), name, _))
members.sort(key=lambda x: (x[0], x[2]))

for age, name, turn in members:
    print(age, name)