import copy

g = int(input())
p = int(input())

docking = [True for _ in range(g)]

plane = [int(input()) for _ in range(p)]

result = 0

def dfs(docking, plane_order, cnt):
    global result
    can_docking = [i for i in range(plane[plane_order])]
    result = max(cnt, result)
    for _ in can_docking:
        if docking[_]:
            cp_docking = copy.deepcopy(docking)
            cp_docking[_] = False
            print(cp_docking)
            dfs(cp_docking, plane_order+1, cnt+1)

dfs(docking, 0, 0)
print(result)
            
