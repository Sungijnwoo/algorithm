import copy
sudoku = [list(map(int, input().split())) for _ in range(9)]
result = []
def check(y, x):
    horizontal = sudoku[y]
    vertical = [sudoku[i][x] for i in range(9)]
    square = [sudoku[i][j] for i in range((y%3)*3, (y%3)*3+3) for j in range((x%3)*3, (x%3)*3+3)]
    for i in range(1, 10):
        if horizontal.count(i) >= 2:
            return False
        if vertical.count(i) >= 2:
            return False
        if square.count(i) >= 2:
            return False
    return True


def find_blank():
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None, None
 

def dfs():
    y, x = find_blank()
    if y == None and x == None:
        for i in range(9):
            print(*sudoku[i])
        exit(0)
    for i in range(1, 10):
        sudoku[y][x] = i
        if not check(y, x):
            continue
        else:
            dfs()


dfs()

