import sys, math

# n = 최소, m = 최대
n, m = map(int, sys.stdin.readline().split())

# arr : 정답 배열
arr = [1 for _ in range(n,m+1)]

# square : 제곱수들
square = [v ** 2 for v in range(2, int(math.sqrt(m)) + 1)]

for i in square:
    # idx = 처음 시작되는 인덱스
    idx = (math.ceil(n / i) * i) - n
    # 범위를 만족하면 지워준다
    while idx <= m - n:
        arr[idx] = 0
        idx += i
ans = 0
for i in range(len(arr)):
    if arr[i] == 1:
        ans += 1
        
# 정답출력
print(ans)