from copy import deepcopy
def rotate(key):
    N = len(key)
    temp = [[0 for i in range(N)] for j in range(N)]
    
    for i in range(N):
        for j in range(N-1, -1, -1):
            temp[i][N-j-1] = key[j][i]

    return temp

def check(lock):
    lock_length = len(lock) // 3
    for i in range(lock_length, lock_length*2):
        
def solution(key, lock):
    n = len(lock)
    m = len(key)
    extend_lock = [[0 for i in range(n*3)] for j in range(n*3)]

    
    for i in range(n):
        for j in range(n):
            extend_lock[i+n][j+n] = lock[i][j]
    
    for _ in range(4):
        tmp_lock = deepcopy(extend_lock)
        if _ != 0:
            key = rotate(key)
        for x in range(n*2):
            for j in range(n*2):
        



if __name__ == "__main__":
    solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])