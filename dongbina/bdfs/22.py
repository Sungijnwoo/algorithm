from collections import deque

def solution(board):
    left, right = (0, 0), (0, 1)
    cnt = 0
    q = deque([(left, right, cnt)])

    noc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = []
    while q:
        print(q)
        (left_y, left_x), (right_y, right_x), cnt = q.popleft()

        if (left_y == len(board)-1 and left_x == len(board)-1) or (right_y == len(board)-1 and right_x == len(board)-1):
            return cnt
        diff_y, diff_x = right_y - left_y, right_x - left_x
        
        # rotate
        for dy, dx in noc:
            if noc == (diff_y, diff_x) or noc == (-diff_y, -diff_x):
                continue
            # right standard
            left_n_y = right_y + dy
            left_n_x = right_x + dx
            check_n_y = left_y + dy
            check_n_x = left_x + dx
            if 0 <= left_n_y < len(board) and 0 <= left_n_x < len(board) and board[left_n_y][left_n_x] == 0:
                if 0 <= check_n_y < len(board) and 0 <= check_n_x < len(board) and board[check_n_y][check_n_x] == 0:
                    if ((left_n_y, left_n_x), (right_y, right_x)) not in visited:
                        q.append(((left_n_y, left_n_x), (right_y, right_x), cnt+1))
                        visited.append(((left_n_y, left_n_x), (right_y, right_x)))
            # left standard
            right_n_y = check_n_y
            right_n_x = check_n_x
            check_n_y = left_n_y
            check_n_x = left_n_x
            if 0 <= right_n_y < len(board) and 0 <= right_n_x < len(board) and board[right_n_y][right_n_x] == 0:
                if 0 <= check_n_y < len(board) and 0 <= check_n_x < len(board) and board[check_n_y][check_n_x] == 0:
                    if ((left_y, left_x), (right_n_y, right_n_x)) not in visited:
                        q.append(((left_y, left_x), (right_n_y, right_n_x), cnt+1))
                        visited.append(((left_y, left_x), (right_n_y, right_n_x)))

        # parellel
        for dy, dx in noc:
            left_n_y = left_y + dy
            left_n_x = left_x + dx
            right_n_y = right_y + dy
            right_n_x = right_x + dx

            if 0 <= left_n_y < len(board) and 0 <= left_n_x < len(board) and board[left_n_y][left_n_x] == 0:
                if 0 <= right_n_y < len(board) and 0 <= right_n_x < len(board) and board[right_n_y][right_n_x] == 0:
                    if board[left_n_y][left_n_x] == 0 and board[right_n_y][right_n_x] == 0:
                        if ((left_n_y, left_n_x), (right_n_y, right_n_x)) not in visited:
                            q.append(((left_n_y, left_n_x), (right_n_y, right_n_x), cnt+1))
                            visited.append(((left_n_y, left_n_x), (right_n_y, right_n_x)))
    
if __name__ == "__main__":
    print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))