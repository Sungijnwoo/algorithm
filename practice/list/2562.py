numbers = []
max_number = 0
max_idx = 0
for i in range(9):
    if (n:=int(input())) > max_number:
        max_number = n
        max_idx = i + 1

print(max_number)
print(max_idx)

