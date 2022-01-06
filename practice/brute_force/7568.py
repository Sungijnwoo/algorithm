n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
ranks =[0 for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        left = people[i]
        right = people[j]

        if left[0] < right[0] and left[1] < right[1]:
            ranks[i] += 1
        elif left[0] > right[0] and left[1] > right[1]:
            ranks[j] += 1

for rank in ranks:
    print(rank+1, end=" ")
