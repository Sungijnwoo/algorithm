n = int(input())
wines = [int(input()) for _ in range(n)]

def total(drink):
    return sum([wines[i] for i in drink])


def check(drink):
    possible = 1
    before_diff = -1
    for x, i in enumerate(drink[:-1]):
        diff = drink[x+1]-drink[x]
        if before_diff == diff:
            possible += 1
        else:
            possible = 1
        if possible == 2:
            return False
        before_diff = diff
    return True


drink = []
max_drink = 0
def dfs(idx):
    if drink:
        global max_drink
        max_drink = max(max_drink, total(drink))
    for i in range(idx,n):
        if i not in drink:
            drink.append(i)
            if check(drink):
                dfs(i)
            drink.pop()

dfs(0)
print(max_drink)


