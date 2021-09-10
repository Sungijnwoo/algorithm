from collections import deque

n = int(input())
q = deque([[['ST', 'PH'], [1], 1]])     #commands, stack, register
cnt = 0

# PH : 레지스터의 값을 복사해 스택에 넣음
# PL : 스택에서 하나 빼 레지스터로 넣음
# AD : 스택에서 맨위 두개빼서 합쳐서 스택에 넣음
# ZE : 레지스터를 0으로 만듦 -> N==0인 경우 제외하고 안 쓸 예정
# ST : 레지스터를 1로 만듦
# DI : 디스플레이하고 종료

def compiler(n):
    if n == 0:
        print("ZE X")
        print('DI X')
        return
    elif n == 1:
        print('ST X')
        print('DI X')
        return

    visited = [[0 for _ in range(256)] for l in range(512)] # 숫자, 레지스터

    while q:
        commands, stack, register = q.popleft()
        visited[sum(stack)][register] = 1
        if sum(stack) == n and len(commands) + len(stack) - 1 <= 36:
            for i in commands:
                print(i, 'A') if i != 'AD' else print(i)
            for i in range(len(stack)-1):
                print('AD')
            print('PL A')
            print('DI A')
            return
        elif sum(stack) < n and len(commands) + len(stack) + 2 <= 40:
            #AD
            if len(stack) >= 2:
                AD = commands + ['AD']
                last1 = stack[-1]
                last2 = stack[-2]
                AD_stack = stack[:-2] + [last1+last2]
                q.append([AD, AD_stack, register])
            #PH
            if not visited[sum(stack)+register][register]:
                PH = commands + ['PH']
                PH_stack = stack + [register]
                q.append([PH, PH_stack, register])
            #PL
            if stack and not visited[sum(stack[:-1])][stack[-1]]:
                PL = commands + ["PL"]
                PL_register = stack[-1]
                q.append([PL, stack[:-1], PL_register])

compiler(n)


        

        
