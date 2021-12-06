def solution(s):
    start = len(s) // 2
    min_len = len(s)

    for i in range(start, 0, -1):
        li = [s[i:i+start] for i in range(0, len(s), start)]
        dic = []
        start_str = li[0]
        cnt = 1
        for j in li[1:]:
            if j != start_str:
                dic.append((start_str, cnt))
                start_str = j
                cnt = 1
            else:
                cnt += 1
        dic.append((start_str, cnt))
        length = 0
        for key, value in dic:
            length += len(key)
            if value != 1: 
                length += len(str(value))
        min_len = min(min_len, length)
        start -= 1
    
    return min_len

if __name__ == "__main__":
    solution("aabbaccc")