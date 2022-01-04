time = {i: i+1 for i in range(1, 10)}
time[0] = time[9] + 1
dial = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
s = input()

total_time = 0
for i in s:
    for key, value in dial.items():
        if i in value:
            total_time += time[key]
            break

print(total_time)

