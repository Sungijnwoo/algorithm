while True:
    triangle = list(map(int, input().split()))
    triangle = [i**2 for i in triangle]
    if not all(triangle):
        break

    max_length = max(triangle)
    triangle.remove(max_length)

    if triangle[0] + triangle[1] == max_length:
        print("right")
    else:
        print("wrong")