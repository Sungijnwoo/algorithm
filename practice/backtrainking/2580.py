sudoku = [list(map(int, input().split())) for _ in range(9)]

def check(y, x):
    horizontal = sudoku[y]
    vertical = [sudoku[i][x] for i in range(9)]
    square = [sudoku[i][j] for i in range((y%3)*3, (y%3)*3+3) for j in range((x%3)*3, (x%3)*3+3)]
    print(square)
check(0, 0)