import copy
def solution(key, lock):
    wide_lock = wider_matrix(lock)
    lock_size = len(lock)
    key_size = len(key)
    for i in range(4):
        key = rotate_matrix(key)
        for dx in range(lock_size*2):
            for dy in range(lock_size*2):
                tmp_wide_lock = copy.deepcopy(wide_lock)
                for x in range(key_size):
                    for y in range(key_size):
                        tmp_wide_lock[x+dx][y+dy] += key[x][y]
                if check(tmp_wide_lock):
                    return True
    return False



def rotate_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    r_matrix = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            r_matrix[j][n-i-1] = matrix[i][j]

    return r_matrix  

def wider_matrix(matrix):
    n = len(matrix)
    r_matrix = [[0] * n*3 for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            r_matrix[i+n][j+n] = matrix[i][j]
    
    return r_matrix

def check(matrix):
    n = len(matrix) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if matrix[i][j] != 1:
                return False
    return True

if __name__ == "__main__":
    assert solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]) == True