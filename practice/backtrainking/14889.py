from itertools import combinations
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def cal_score(teams):
    noc = combinations(teams, 2)
    total = 0
    for case in noc:
        total += graph[case[0]][case[1]]
        total += graph[case[1]][case[0]]
    return total

teams = []
balance = 1e9
visited = []
def dfs():
    global balance
    if len(teams) == n // 2:
        left = cal_score(teams)
        another_teams = [i for i in range(n) if i not in teams]
        right = cal_score(another_teams)
        balance = min(balance, abs(left-right))
        # print(teams, another_teams)
        return
    for i in range(n):
        if i not in teams:
            teams.append(i)
            dfs()
            teams.pop()

dfs()
print(balance)

noc = combinations([i for i in range(n)], n//2)
for case in noc:
    print(case)