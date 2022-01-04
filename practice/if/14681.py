hour, minute = map(int, input().split())

minute -= 45

if minute < 0:
    hour -= 1
    minute += 60
if hour < 0:
    hour += 24
print(hour, minute)