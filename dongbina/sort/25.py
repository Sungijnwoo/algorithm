from collections import Counter
def solution(N, stages):
    param = Counter(stages)
    failure = []
    parents = len(stages)
    for i in range(1, N+1):
        fail = param[i]
        sucess = parents - param[i]
        if parents == 0:
            failure.append((i, 0))
        else:
            failure.append((i, fail/parents))
        parents = sucess
    result = sorted(failure, key=lambda x: -x[1])
    
    return [i[0] for i in result]

if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 2, 4, 3, 3]))
    print(solution(4, [4, 4, 4, 4, 4]))