def main(N: int, K: int):
    cnt = 0
    while N != 1:
        cnt += 1
        if N % K == 0:
            N = N // K
        else:
            N -= 1
    
    return cnt


if __name__ == "__main__":
    assert main(17, 4) == 3
    assert main(25, 5) == 2
